from django.db import models

class Student(models.Model):
    GENDER_CHOICES=[('Male','Male'),
                    ('Female','Female'),
                    ('Other','Other')]

    name=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
