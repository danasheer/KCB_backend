# Generated by Django 4.1.6 on 2023-04-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0003_rename_floor_employee_department_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computer",
            name="invontorynumber",
            field=models.CharField(max_length=255),
        ),
    ]
