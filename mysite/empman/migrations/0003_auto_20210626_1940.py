# Generated by Django 2.2.5 on 2021-06-26 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empman', '0002_auto_20210626_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='employee_company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empman.companyModel'),
        ),
    ]