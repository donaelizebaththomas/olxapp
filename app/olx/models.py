from django.db import models

class vehicle(models.Model):
    model_type=models.CharField(max_length=20)
    model_name=models.CharField(max_length=20)
    year=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='image',null=True,blank=True) #to upload image
    # pdf=models.FileField(upload_to='book/pdf') #to upload pdf files or documents

    # To display book title in admin homepage
    def __str__(self):
        return self.model_name