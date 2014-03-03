from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    paid = models.BooleanField()
    paid_date = models.DateField()
    paid_amount = models.IntegerField()
    join_date = models.DateField()
    officer = models.BooleanField()
    officer_position = models.CharField(max_length=20)
    uofl_user_id = models.CharField(max_length=10)
    personal_url = models.URLField()
    fun_fact = models.TextField()
