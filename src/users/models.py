from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path
# Define choices for governorates
GOVERNORATE_CHOICES = [
    ('Cairo', 'Cairo'),
    ('Alexandria', 'Alexandria'),
    ('Giza', 'Giza'),
    ('Shubra El-Kheima', 'Shubra El-Kheima'),
    ('Port Said', 'Port Said'),
    ('Suez', 'Suez'),
    ('Luxor', 'Luxor'),
    ('Aswan', 'Aswan'),
    ('Damietta', 'Damietta'),
    ('Faiyum', 'Faiyum'),
    ('Minya', 'Minya'),
    ('Qena', 'Qena'),
    ('Qalyoubia', 'Qalyoubia'),
    ('Sohag', 'Sohag'),
    ('Hurghada', 'Hurghada'),
    ('Ismailia', 'Ismailia'),
    ('Mansoura', 'Mansoura'),
    ('Tanta', 'Tanta'),
    ('Zagazig', 'Zagazig'),
    ('Asyut', 'Asyut'),
    ('Beni Suef', 'Beni Suef'),
    ('Banha', 'Banha'),
    ('Kafr El Sheikh', 'Kafr El Sheikh'),
    ('Mahalla', 'Mahalla'),
    ('Damanhur', 'Damanhur'),
    ('El-Minya', 'El-Minya'),
    ('El Arish', 'El Arish'),
    ('Ras Gharib', 'Ras Gharib'),
    ('Port Safaga', 'Port Safaga'),
]

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)  # 10,1,8,3
    address_2 = models.CharField(max_length=128, blank=True)  # Additional details if any
    city = models.CharField(max_length=64)  # Shubra El-Kheima
    state = models.CharField(max_length=100, choices=GOVERNORATE_CHOICES)  # Qalyoubia
    zip_code = models.CharField(max_length=10, blank=True)  # 3753450

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)  # Adjust max_length as needed for phone numbers
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'



