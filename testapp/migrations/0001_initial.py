# Generated by Django 2.0 on 2019-09-09 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('eaddr', models.CharField(max_length=64)),
                ('esal', models.IntegerField()),
                ('ecell_no', models.IntegerField()),
            ],
        ),
    ]