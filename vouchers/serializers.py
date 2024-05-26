from rest_framework import serializers


from academic_year.serializers import AcademicYearSerializer
from bank_accounts.serializers import BankAccountSerializer
from classes.serializers import ClassesSerializer
from expense_categories.serializers import ExpenseCategorySerializer
from payment_methods.serializers import PaymentMethodSerializer
from staff.serializers import StaffSerializer
from suppliers.serializers import SupplierSerializer
from term.serializers import TermSerializer
from .models import Voucher



class VoucherSerializer(serializers.ModelSerializer):

    bank_account_details = BankAccountSerializer(source='bank_account', required=False, read_only=True, many=False)
    payment_Method_details = PaymentMethodSerializer(source='payment_Method', required=False, read_only=True, many=False)
    expenseCategory_details = ExpenseCategorySerializer(source='expenseCategory', required=False, read_only=True, many=False)

    supplier_details = SupplierSerializer(source='supplier', required=False, read_only=True, many=False)
    staff_details = StaffSerializer(source='staff', required=False, read_only=True, many=False)

    payment_values = serializers.ListField(child=serializers.DictField(), write_only=True)
    attachmens_values = serializers.ListField(child=serializers.DictField(), allow_null=True, required=False, write_only=True)

    payment_items = serializers.SerializerMethodField(read_only=True)
    attachments_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Voucher
        fields = '__all__'

    def get_payment_items(self, obj):
        from voucher_items.serializers import VoucherItemSerializer
        try:
            payment_items = obj.voucher_items.all()
        except AttributeError  as exception:
            print(f"Found error {exception}")
            payment_items = []
        return VoucherItemSerializer(payment_items, many=True).data



    def get_attachments_items(self, obj):
        from voucher_attachments.serializers import Voucherattachmentserializer
        try:
            attachments_items = obj.voucher_attachments.all()
        except AttributeError as exception:
            print(f"Found error {exception}")
            attachments_items = []
        return Voucherattachmentserializer(attachments_items, many=True).data




