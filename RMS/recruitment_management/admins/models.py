from django.db import models
from students.models import Student

class PlacementDrive(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.company_name

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    placement_drive = models.ForeignKey(PlacementDrive, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} - {self.placement_drive.company_name}"
