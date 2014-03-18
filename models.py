from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()
    paid = models.BooleanField()
    paid_date = models.DateField(null=True)
    paid_amount = models.IntegerField(null=True)
    join_date = models.DateField(null=True)
    officer = models.BooleanField()
    officer_position = models.CharField(max_length=40, null=True)
    uofl_user_id = models.CharField(max_length=10)
    personal_url = models.URLField(null=True)
    fun_fact = models.TextField(null=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name 
