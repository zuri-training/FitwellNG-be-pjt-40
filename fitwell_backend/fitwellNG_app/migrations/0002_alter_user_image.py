# Generated by Django 3.2.4 on 2021-07-02 10:14

from django.db import migrations, models
import fitwellNG_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('fitwellNG_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=fitwellNG_app.models.get_image_path, verbose_name='Image'),
        ),
    ]
