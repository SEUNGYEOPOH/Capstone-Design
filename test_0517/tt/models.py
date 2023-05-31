from django.db import models

# Create your models here.
class S3Image(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    c_date = models.DateTimeField(blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    