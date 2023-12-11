from django.db import models
from django.db.models import JSONField

from academic_year.models import AcademicYear
from classes.models import Classes
from term.models import Term
from models import ParentModel
from utils import currentAcademicYear


# models.py
class FeeStructure(ParentModel):
    academic_year = models.ForeignKey(AcademicYear, default=currentAcademicYear, null=True, on_delete=models.CASCADE, related_name="fee_structures")
    classes = models.ForeignKey(Classes, null=True, default=None, on_delete=models.CASCADE, related_name="fee_structures")
    term = models.ForeignKey(Term, null=True, default=None, on_delete=models.CASCADE, related_name="fee_structures")
    instructions = models.CharField(max_length=255, blank=True, null=True)
    school_id = models.UUIDField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.school_id}"