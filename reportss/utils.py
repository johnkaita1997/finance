from _decimal import Decimal
from django.db.models import Sum

from appcollections.models import Collection
from grants.models import Grant
from payment_in_kinds.models import PaymentInKind
from voucher_items.models import VoucherItem


def getBalance(account_type, month, financial_year, school_id):
    if month == 1:
        month = 12
    else:
        month = int(month) - 1

    querysetGrants = Grant.objects.filter(
        deleted=False,
        receipt_date__month=month,
        school_id=school_id,
    )

    collectionQuerySet = Collection.objects.filter(
        school_id=school_id,
        receipt__transaction_date__month=month,
        receipt__is_reversed=False
    )

    pikQuerySet = PaymentInKind.objects.filter(
        receipt__is_posted=True,
        school_id=school_id,
        transaction_date__month=month,
    )

    expensesQuerySet = VoucherItem.objects.filter(
        voucher__is_deleted=False,
        school_id=school_id,
        voucher__paymentDate__month=month,
    )

    if financial_year and financial_year != "" and financial_year != "null":
        collectionQuerySet = collectionQuerySet.filter(receipt__financial_year=financial_year)
        pikQuerySet = pikQuerySet.filter(receipt__financial_year=financial_year)
        expensesQuerySet = expensesQuerySet.filter(voucher__financial_year=financial_year)
        querysetGrants = querysetGrants.filter(financial_year=financial_year)

    collectionAmount = collectionQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    pikAmount = pikQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    grantAmount = querysetGrants.aggregate(Sum('overall_amount'))['overall_amount__sum'] or Decimal(0.0)
    total_amount = Decimal(collectionAmount) + Decimal(pikAmount) + Decimal(grantAmount)

    collectionQuerySet = list(collectionQuerySet)
    pikQuerySet = list(pikQuerySet)
    querysetGrants = list(querysetGrants)

    cash_at_hand = Decimal(0.0)
    cash_at_bank = Decimal(0.0)

    for grant in querysetGrants:
        if grant.paymentMethod.is_cash == True:
            cash_at_hand += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_bank == True:
            cash_at_bank += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_cheque == True:
            cash_at_bank += Decimal(grant.overall_amount)


    for collection in collectionQuerySet:
        if collection.receipt.payment_method.is_cash == True:
            cash_at_hand += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_bank == True:
            cash_at_bank += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_cheque == True:
            cash_at_bank += Decimal(collection.amount)

    for pik in pikQuerySet:
        cash_at_hand += Decimal(pik.amount)

    for voucheritem in expensesQuerySet:
        if voucheritem.voucher.payment_Method.is_cash == True:
            cash_at_hand -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_Method.is_bank == True:
            cash_at_bank -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_method.is_cheque == True:
            cash_at_bank -= Decimal(voucheritem.amount)

    return {
        "total": total_amount,
        "cash": cash_at_hand,
        "bank": cash_at_bank,
    }









def getBalancesByAccount(accounttype, financial_year, school_id):

    querysetGrants = Grant.objects.filter(
        deleted=False,
        school_id=school_id,
        bankAccount__account_type=accounttype,
    )

    collectionQuerySet = Collection.objects.filter(
        school_id=school_id,
        receipt__bank_account__account_type=accounttype,
        receipt__is_reversed=False
    )

    pikQuerySet = PaymentInKind.objects.filter(
        receipt__is_posted=True,
        school_id=school_id,
        receipt__bank_account__account_type=accounttype,
    )

    expensesQuerySet = VoucherItem.objects.filter(
        voucher__is_deleted=False,
        school_id=school_id,
        voucher__bank_account__account_type=accounttype,
    )

    if financial_year and financial_year != "" and financial_year != "null":
        collectionQuerySet = collectionQuerySet.filter(receipt__financial_year=financial_year)
        pikQuerySet = pikQuerySet.filter(receipt__financial_year=financial_year)
        expensesQuerySet = expensesQuerySet.filter(voucher__financial_year=financial_year)
        querysetGrants = querysetGrants.filter(financial_year=financial_year)

    collectionAmount = collectionQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    pikAmount = pikQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    grantsAmount = querysetGrants.aggregate(Sum('overall_amount'))['overall_amount__sum'] or Decimal(0.0)

    total_amount = Decimal(collectionAmount) + Decimal(pikAmount) + Decimal(grantsAmount)

    collectionQuerySet = list(collectionQuerySet)
    pikQuerySet = list(pikQuerySet)
    querysetGrants = list(querysetGrants)

    cash_at_hand = Decimal(0.0)
    cash_at_bank = Decimal(0.0)

    for grant in querysetGrants:
        if grant.paymentMethod.is_cash == True:
            cash_at_hand += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_bank == True:
            cash_at_bank += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_cheque == True:
            cash_at_bank += Decimal(grant.overall_amount)

    for collection in collectionQuerySet:
        if collection.receipt.payment_method.is_cash == True:
            cash_at_hand += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_bank == True:
            cash_at_bank += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_cheque == True:
            cash_at_bank += Decimal(collection.amount)

    for pik in pikQuerySet:
        cash_at_hand += Decimal(pik.amount)

    for voucheritem in expensesQuerySet:
        if voucheritem.voucher.payment_Method.is_cash == True:
            cash_at_hand -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_Method.is_bank == True:
            cash_at_bank -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_method.is_cheque == True:
            cash_at_bank -= Decimal(voucheritem.amount)

    return {
        "total": total_amount,
        "cash": cash_at_hand,
        "bank": cash_at_bank,
    }






def getBalancesByFinancialYear(financial_year, school_id):

    querysetGrants = Grant.objects.filter(
        deleted=False,
        school_id=school_id,
    )


    collectionQuerySet = Collection.objects.filter(
        school_id=school_id,
        receipt__is_reversed=False
    )

    pikQuerySet = PaymentInKind.objects.filter(
        receipt__is_posted=True,
        school_id=school_id,
    )

    expensesQuerySet = VoucherItem.objects.filter(
        voucher__is_deleted=False,
        school_id=school_id,
    )

    if financial_year and financial_year != "" and financial_year != "null":
        collectionQuerySet = collectionQuerySet.filter(receipt__financial_year=financial_year)
        pikQuerySet = pikQuerySet.filter(receipt__financial_year=financial_year)
        expensesQuerySet = expensesQuerySet.filter(voucher__financial_year=financial_year)
        querysetGrants = querysetGrants.filter(financial_year=financial_year)

    collectionAmount = collectionQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    pikAmount = pikQuerySet.aggregate(Sum('amount'))['amount__sum'] or Decimal(0.0)
    grantsAmount = querysetGrants.aggregate(Sum('overall_amount'))['overall_amount__sum'] or Decimal(0.0)

    total_amount = Decimal(collectionAmount) + Decimal(pikAmount) + Decimal(grantsAmount)

    collectionQuerySet = list(collectionQuerySet)
    pikQuerySet = list(pikQuerySet)
    querysetGrants = list(querysetGrants)

    cash_at_hand = Decimal(0.0)
    cash_at_bank = Decimal(0.0)

    for grant in querysetGrants:
        if grant.paymentMethod.is_cash == True:
            cash_at_hand += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_bank == True:
            cash_at_bank += Decimal(grant.overall_amount)
        elif grant.paymentMethod.is_cheque == True:
            cash_at_bank += Decimal(grant.overall_amount)

    for collection in collectionQuerySet:
        if collection.receipt.payment_method.is_cash == True:
            cash_at_hand += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_bank == True:
            cash_at_bank += Decimal(collection.amount)
        elif collection.receipt.payment_method.is_cheque == True:
            cash_at_bank += Decimal(collection.amount)

    for pik in pikQuerySet:
        cash_at_hand += Decimal(pik.amount)

    for voucheritem in expensesQuerySet:
        if voucheritem.voucher.payment_Method.is_cash == True:
            cash_at_hand -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_Method.is_bank == True:
            cash_at_bank -= Decimal(voucheritem.amount)
        elif voucheritem.voucher.payment_method.is_cheque == True:
            cash_at_bank -= Decimal(voucheritem.amount)

    return {
        "total": total_amount,
        "cash": cash_at_hand,
        "bank": cash_at_bank,
    }