# Generated by Django 4.2.13 on 2024-06-25 14:41

from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_photo'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brands',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('ford', 'Ford'), ('mercedes', 'Mercedes'), ('volkswagen', 'Volkswagen'), ('volvo', 'Volvo'), ('renault', 'Renault'), ('skoda', 'Skoda'), ('citroen', 'Citroen'), ('peugeot', 'Peugeot'), ('fiat', 'Fiat'), ('hyundai', 'Hyundai'), ('nissan', 'Nissan'), ('toyota', 'Toyota'), ('mazda', 'Mazda'), ('subaru', 'Subaru'), ('kia', 'Kia'), ('honda', 'Honda'), ('hyundai', 'Hyundai'), ('lexus', 'Lexus'), ('jaguar', 'Jaguar'), ('porsche', 'Porsche'), ('bentley', 'Bentley'), ('dodge', 'Dodge'), ('kia', 'Kia'), ('mitsubishi', 'Mitsubishi'), ('suzuki', 'Suzuki'), ('Peugot', 'Peugot')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='White', max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='vin',
            field=models.CharField(default='', max_length=17),
            preserve_default=False,
        ),
    ]
