from django.db import models

# Define choices for student branches
STUDENT_BRANCH_CHOICES = [
    ('civil', 'Civil Engineering'),
    ('electrical', 'Electrical Engineering'),
    ('mechanical', 'Mechanical Engineering'),
    ('electronic', 'Electronic Engineering'),
]

class Student(models.Model):
    stuname = models.CharField(max_length=100,null=True, blank=True)
    stuemail = models.EmailField(max_length=150,null=True, blank=True)
    stuage = models.IntegerField()
    stuphoto = models.ImageField(upload_to='photos/', null=True, blank=True)
    stubranch = models.CharField(max_length=100, choices=STUDENT_BRANCH_CHOICES,null=True, blank=True)
    stucontact = models.CharField(max_length=20,null=True, blank=True)  # Changed to CharField for flexibility

    def __str__(self):
        return self.stuname
