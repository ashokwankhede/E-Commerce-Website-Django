# Generated by Django 3.2.7 on 2022-10-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221017_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.vendor'),
        ),
    ]
