# Generated by Django 3.1.10 on 2023-01-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0006_auto_20230112_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='ownername',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]