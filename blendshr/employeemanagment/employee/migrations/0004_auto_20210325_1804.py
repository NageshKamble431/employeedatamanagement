# Generated by Django 3.1.3 on 2021-03-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210325_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeleavecategory',
            name='IsFirstHalfDay',
        ),
        migrations.RemoveField(
            model_name='employeeleavecategory',
            name='IsLastHalfDay',
        ),
        migrations.AddField(
            model_name='employeeleavecategory',
            name='Is_First_Half_Day',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeeleavecategory',
            name='Is_Last_Half_Day',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
    ]
