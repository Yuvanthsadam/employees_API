from django.db import models


# class Company(models.Model):
#     company_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.company_name


class User(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name
