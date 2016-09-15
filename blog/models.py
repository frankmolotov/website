from django.db import models


class Count(models.Model):
    count_of_users = models.CharField(max_length=100, null=True, default='257329')
    capital = models.CharField(max_length=100, null=True, default='1452900')


class Register(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # validators should be a list
    registration_date = models.DateTimeField(
        blank=True, null=True)
    count_of_users = models.ForeignKey(Count, null=True)

    def submit(self):
        self.save()


