from uuid import UUID

from _decimal import Decimal
from django.db.models import Sum
from rest_framework import serializers

from academic_year.serializers import AcademicYearSerializer
from appcollections.models import Collection
from classes.serializers import ClassesSerializer
from currencies.serializers import CurrencySerializer
from payment_in_kinds.models import PaymentInKind
from receipts.models import Receipt
from school.models import School
from school.serializer import SchoolSerializer
from schoolgroups.serializers import SchoolGroupSerializer
from streams.serializers import StreamsSerializer
from students.models import Student
from students.serializers import StudentSerializer
from term.serializers import TermSerializer
from .models import Invoice, Structure, Uninvoice, Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'



class InvoiceSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', required=False, read_only=True)
    term_details  = TermSerializer(source='term', required=False, read_only=True)
    currency_details  = CurrencySerializer(source='currency', required=False, read_only=True)
    paid = serializers.SerializerMethodField(read_only=True)
    due = serializers.SerializerMethodField(read_only=True)

    def get_paid(self, obj):
        invoice = obj
        try:
            student = invoice.student
            if isinstance(student, UUID):  # Check if student is a UUID object
                student = Student.objects.get(id=student)  # Fetch student object if it's a UUID

            school = School.objects.get(id=student.school_id)  # Fetch school using student object
            term = invoice.term
            year = invoice.year
            voteheads = invoice.votehead


            collections_amount_paid = Collection.objects.filter(
                votehead=voteheads,
                student=student,
                receipt__term=term,
                receipt__year=year,
                receipt__is_reversed=False,
                school_id=school.id
            ).aggregate(total_amount_paid=Sum('amount'))['total_amount_paid'] or 0.0

            total_PIK = PaymentInKind.objects.filter(
                votehead=voteheads,
                student=student,
                receipt__term=term,
                receipt__year=year,
                receipt__is_posted=True,
                school_id=school.id
            ).aggregate(total_amount_paid=Sum('amount'))['total_amount_paid'] or 0.0

            total_amount_paid = collections_amount_paid + total_PIK


            return total_amount_paid

        except School.DoesNotExist:
            return {'error': f"School not found"}
        except Exception as exception:
            return {'error': f"Bad Request {exception}"}


    def get_due(self, obj):
        invoice = obj
        try:
            student = invoice.student
            if isinstance(student, UUID):  # Check if student is a UUID object
                student = Student.objects.get(id=student)  # Fetch student object if it's a UUID
            school = School.objects.get(id=student.school_id)  # Fetch school using student object
            term = invoice.term
            year = invoice.year
            voteheads = invoice.votehead
            amountRequired = invoice.amount

            collections_amount_paid = Collection.objects.filter(
                votehead=voteheads,
                student=student,
                receipt__term=term,
                receipt__year=year,
                receipt__is_reversed=False,
                school_id=school.id
            ).aggregate(total_amount_paid=Sum('amount'))['total_amount_paid'] or 0.0

            total_PIK = PaymentInKind.objects.filter(
                votehead=voteheads,
                student=student,
                receipt__term=term,
                receipt__year=year,
                receipt__is_posted=True,
                school_id=school.id
            ).aggregate(total_amount_paid=Sum('amount'))['total_amount_paid'] or 0.0

            total_amount_paid = collections_amount_paid + total_PIK

            return amountRequired - Decimal(total_amount_paid)

        except School.DoesNotExist:
            return {'error': f"School not found"}
        except Exception as exception:
            return {'error': f"Bad Request {exception}"}

    class Meta:
        model = Invoice
        fields = '__all__'


class StructureSerializer(serializers.ModelSerializer):
    structure_year_details = AcademicYearSerializer(source='structure_year', required=False, read_only=True)
    structure_class_details = ClassesSerializer(source='structure_class', required=False, read_only=True)
    structure_term_details = TermSerializer(source='structure_term', required=False, read_only=True)
    student_details = StudentSerializer(source='student', required=False, read_only=True)
    classes_details = ClassesSerializer(source='classes', required=False, read_only=True)
    stream_details = StreamsSerializer(source='stream', required=False, read_only=True)
    group_details = SchoolGroupSerializer(source='group', required=False, read_only=True)
    class Meta:
        model = Structure
        fields = '__all__'


class UninvoiceStudentSerializer(serializers.ModelSerializer):
    structure_year_details = AcademicYearSerializer(source='structure_year', required=False, read_only=True)
    structure_class_details = ClassesSerializer(source='structure_class', required=False, read_only=True)
    structure_term_details = TermSerializer(source='structure_term', required=False, read_only=True)
    structure_stream_details = StreamsSerializer(source='structure_stream', required=False, read_only=True)  # Corrected here
    student_details = StudentSerializer(source='student', required=False, read_only=True)

    class Meta:
        model = Uninvoice
        fields = '__all__'
