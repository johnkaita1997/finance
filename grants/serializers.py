from rest_framework import serializers

from bank_accounts.serializers import BankAccountSerializer
from currencies.serializers import CurrencySerializer
from payment_methods.serializers import PaymentMethodSerializer
from school.serializer import SchoolSerializer
from term.serializers import TermSerializer
from .models import Grant


class GrantSerializer(serializers.ModelSerializer):
    bankAccount_details = BankAccountSerializer(source='bankAccount', required=False, read_only=True, many=False)
    currency_details = CurrencySerializer(source='currency', required=False, read_only=True, many=False)
    paymentMethod_details = PaymentMethodSerializer(source='paymentMethod', allow_null=True, required=False, read_only=True, many=False)
    term_details = TermSerializer(source='term',required=False, read_only=True, many=False)
    school_details = SchoolSerializer(source='school',required=False, read_only=True, many=False)
    items_list = serializers.ListField(child=serializers.DictField(), allow_null=True, required=False, write_only=True)
    items = serializers.SerializerMethodField(read_only=True)
    # students = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Grant
        fields = '__all__'

    def get_items(self, obj):
        from grant_items.serializers import GrantItemSerializer
        try:
            items = obj.grant_items.all()
        except AttributeError:
            items = []
        return GrantItemSerializer(items, many=True).data


    def get_students(self, obj):
        try:
            students = obj.students
        except AttributeError as exception:
            print(f"Atttribute error {exception}")
            students = []
        return students





