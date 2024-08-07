# Generated by Django 4.1.13 on 2024-06-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Breed', models.CharField(max_length=50)),
                ('Country_of_Origin', models.CharField(max_length=50)),
                ('Fur_Color', models.CharField(max_length=50)),
                ('Height_inches', models.CharField(max_length=50)),
                ('Color_of_Eyes', models.CharField(max_length=50)),
                ('Longevity_yrs', models.CharField(max_length=50)),
                ('Character_Traits', models.CharField(max_length=150)),
                ('Common_Health_Probles', models.TextField(max_length=1000)),
            ],
        ),
    ]
