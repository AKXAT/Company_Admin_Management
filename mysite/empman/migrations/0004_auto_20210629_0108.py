# Generated by Django 3.2.4 on 2021-06-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empman', '0003_auto_20210626_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='company_created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='employee_created',
            field=models.DateField(),
        ),
    ]
