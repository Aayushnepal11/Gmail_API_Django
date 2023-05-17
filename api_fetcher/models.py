from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class DataFile(models.Model):
    filename = models.CharField(max_length=120, unique=True, blank=False)
    files = models.FileField(blank=False,editable=True, validators=[FileExtensionValidator(allowed_extensions=[".csv", ".json"])])

    class Meta: 
        verbose_name="Data Files"
        verbose_name_plural="Data Files"
        
    def __str__(self):
        return self.filename
