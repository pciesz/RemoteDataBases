# Generated by Django 2.1.2 on 2018-11-24 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20181028_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='issuingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='issuer', to='user.User'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='receivingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to='user.User'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='visitation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='invoice.Visitation'),
        ),
    ]