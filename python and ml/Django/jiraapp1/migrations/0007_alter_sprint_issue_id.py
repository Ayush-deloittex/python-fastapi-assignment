# Generated by Django 3.2.16 on 2022-11-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jiraapp1', '0006_sprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='issue_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jiraapp1.issues'),
        ),
    ]