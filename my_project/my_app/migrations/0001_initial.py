# Generated by Django 4.0.5 on 2023-02-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField()),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_branch', models.CharField(default='cse', max_length=10)),
            ],
        ),
    ]
