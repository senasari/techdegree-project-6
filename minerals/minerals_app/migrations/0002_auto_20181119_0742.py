# Generated by Django 2.1.3 on 2018-11-19 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minerals_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineral',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='cleavage',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='color',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='crystal_habit',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='crystal_symmetry',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='crystal_system',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='diaphaneity',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='formula',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='image_caption',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='luster',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='mohs_scale_hardness',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='optical_properties',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='refractive_index',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='specific_gravity',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='streak',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='strunz_classification',
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='unit_cell',
        ),
    ]
