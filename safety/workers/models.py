from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
import qrcode

# Create your models here.
class Worker(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    is_available=models.BooleanField()
    primary_phone=models.CharField(max_length=10)
    secondary_phone=models.CharField(max_length=10)
    address=models.TextField()
    image_profile=models.ImageField(null=True, blank=True)
    qr_code=models.ImageField(upload_to='qr_code' ,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # qr.add_data(self.first_name)
        qr.add_data('http://54.255.181.141:8000/workers/')
        qr.make(fit=True)
        img =qr.make_image(fill_color='white' ,back_color='black') 
        fname = f'qr_code-{self.first_name}.png'
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        self.qr_code.save(fname, File(buffered), save=False)
        super().save(*args, **kwargs)

