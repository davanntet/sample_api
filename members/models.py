from django.db import models
from django.forms import ModelForm
# Create your models here.
class members(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"




class form_members(ModelForm):
    class Meta:
        model = members
        fields = "__all__"