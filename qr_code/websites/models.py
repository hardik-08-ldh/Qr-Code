from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
# Create your models here.

class Website(models.Model):
    name=models.CharField(max_length=100)
    qr_code=models.ImageField(upload_to='qr_code',blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.name)
        canvas=Image.new('RGB',(qrcode_img.pixel_size, qrcode_img.pixel_size),'white')
        # rgb mode size 290*290 and color white
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.name}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        # to prevent inf loop
        canvas.close()
        super().save(*args,**kwargs)