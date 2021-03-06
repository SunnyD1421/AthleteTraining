# Generated by Django 3.1.7 on 2021-04-19 03:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0002_auto_20210418_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lifting',
            old_name='ath_id',
            new_name='ath_user',
        ),
        migrations.RenameField(
            model_name='liftingschedule',
            old_name='ath_id',
            new_name='ath_user',
        ),
        migrations.RenameField(
            model_name='throwing',
            old_name='ath_id',
            new_name='ath_user',
        ),
        migrations.RenameField(
            model_name='throwingschedule',
            old_name='ath_id',
            new_name='ath_user',
        ),
        migrations.AlterUniqueTogether(
            name='lifting',
            unique_together={('ath_user', 'lift_date')},
        ),
        migrations.AlterUniqueTogether(
            name='throwing',
            unique_together={('ath_user', 'throw_date')},
        ),
    ]
