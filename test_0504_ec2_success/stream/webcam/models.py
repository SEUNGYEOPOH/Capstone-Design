from django.db import models

# Create your models here.
class WebcamDetect(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cam_name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    c_date = models.DateTimeField(blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    