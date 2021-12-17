from django.db import models
from django.contrib.auth.models import User




class Profile (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField("نام" , max_length=100, blank = True)
    last_name = models.CharField("نام خانوادگی" , max_length=150, blank = True)
    national_code = models.CharField("کد ملی" , max_length=40, blank = True)
    mobile_number = models.CharField("شماره موبایل" , max_length=100, blank = True)
    email = models.EmailField("آدرس الکترونیکی" , max_length=200, blank = True)
    pay_number = models.CharField("شماره کارت" , max_length=100, blank = True )
    profile_image = models.ImageField(upload_to='profile_user/', blank = True )

    def get_photo_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        else:
            return "/static/images/User-Icon.jpg"
    def __str__(self):
        return f'کاربر {self.id}'



