from django.db import models

from constants import STATUS
from models import ParentModel
from students.models import Student

class Transaction(ParentModel):
    mobile = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    transid = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    student = models.ForeignKey(Student, default=None, null=True, on_delete=models.CASCADE, related_name="transactions")
    school_id = models.UUIDField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank=True, choices=STATUS, default="PENDING")
    paid_by = models.CharField(max_length=100, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    thirdPartyTransID = models.CharField(max_length=255, blank=True, null=True)
    orgAccountBalance = models.CharField(max_length=255, blank=True, null=True)
    invoiceNumber = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"
