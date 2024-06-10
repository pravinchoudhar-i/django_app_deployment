from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MasterLog(models.Model):
	timeStamp = models.DateTimeField(auto_now_add=True)
	activity = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	status = models.BooleanField(default=1)

	def __str__(self):
		return self.activity