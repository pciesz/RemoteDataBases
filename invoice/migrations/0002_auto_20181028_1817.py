# Generated by Django 2.1.2 on 2018-10-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_role_rolegroup'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='user',
        ),
        migrations.AddField(
            model_name='invoice',
            name='issuingUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='issuer', to='user.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='receivingUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='user.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitation',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.VisitationState'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='visitation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='invoice.Visitation'),
            preserve_default=False,
        ),
    ]