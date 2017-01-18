from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone

class Poll(models.Model):
	id = models.AutoField(primary_key=True)
	id_curse=models.IntegerField()
	enum=models.CharField(max_length=1000)
	feedback=models.TextField()
	expiration_date=models.DateTimeField(default=timezone.now)
	
        def __str__(self):
            return self.enum
