# Generated by Django 4.2.13 on 2024-06-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_listing_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='brands',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('ford', 'Ford'), ('mercedes', 'Mercedes'), ('volkswagen', 'Volkswagen'), ('volvo', 'Volvo'), ('renault', 'Renault'), ('skoda', 'Skoda'), ('citroen', 'Citroen'), ('peugeot', 'Peugeot'), ('fiat', 'Fiat'), ('nissan', 'Nissan'), ('toyota', 'Toyota'), ('mazda', 'Mazda'), ('subaru', 'Subaru'), ('kia', 'Kia'), ('honda', 'Honda'), ('hyundai', 'Hyundai'), ('lexus', 'Lexus'), ('jaguar', 'Jaguar'), ('porsche', 'Porsche'), ('bentley', 'Bentley'), ('dodge', 'Dodge'), ('kia', 'Kia'), ('mitsubishi', 'Mitsubishi'), ('suzuki', 'Suzuki'), ('Peugot', 'Peugot')], default=None, max_length=24),
        ),
    ]
