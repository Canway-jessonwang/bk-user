# Generated by Django 3.2.5 on 2022-05-20 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20210326_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_expiration_date',
            field=models.DateField(blank=True, default=datetime.date(2100, 1, 1), null=True, verbose_name='账号过期时间'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='category_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='用户目录ID'),
        ),
        migrations.AlterIndexTogether(
            name='profile',
            index_together={('category_id', 'account_expiration_date')},
        ),
    ]