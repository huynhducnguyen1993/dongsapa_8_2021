# Generated by Django 3.2.3 on 2021-07-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0016_auto_20210721_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dexuat',
            name='hangmuc',
            field=models.CharField(choices=[('0', 'Hàng Hóa'), ('1', 'Mua Sắm Thiết Bị'), ('2', 'Khác')], max_length=20, verbose_name='Trạng Thái Gửi Duyệt'),
        ),
    ]
