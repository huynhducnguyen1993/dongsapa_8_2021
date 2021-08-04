# Generated by Django 3.2.3 on 2021-07-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khachhang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='khachhanglon',
            name='baogia',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Báo Giá'),
        ),
        migrations.AddField(
            model_name='khachhanglon',
            name='huytheo',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Hủy Theo'),
        ),
        migrations.AddField(
            model_name='khachhanglon',
            name='kyhopdong',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Ký Hợp Đồng'),
        ),
        migrations.AddField(
            model_name='khachhanglon',
            name='thuongthaohopdong',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Thương Thảo Hợp Đồng'),
        ),
        migrations.AddField(
            model_name='khachhanglon',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]