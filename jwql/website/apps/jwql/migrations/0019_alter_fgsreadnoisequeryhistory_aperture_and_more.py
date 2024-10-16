# Generated by Django 4.1.7 on 2024-03-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwql', '0018_nircamclawstats_doy_nircamclawstats_total_bkg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fgsreadnoisequeryhistory',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisequeryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='ngroups',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='nints',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='read_pattern',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='readnoise_diff_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='readnoise_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='subarray',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fgsreadnoisestats',
            name='uncal_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisequeryhistory',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisequeryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='ngroups',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='nints',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='read_pattern',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='readnoise_diff_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='readnoise_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='subarray',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='mirireadnoisestats',
            name='uncal_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawqueryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='filter',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='obs',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='proposal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='pupil',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamclawstats',
            name='skyflat_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisequeryhistory',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisequeryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='ngroups',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='nints',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='read_pattern',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='readnoise_diff_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='readnoise_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='subarray',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nircamreadnoisestats',
            name='uncal_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisequeryhistory',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisequeryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='ngroups',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='nints',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='read_pattern',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='readnoise_diff_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='readnoise_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='subarray',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirissreadnoisestats',
            name='uncal_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisequeryhistory',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisequeryhistory',
            name='instrument',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='aperture',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='detector',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='expstart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='ngroups',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='nints',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='read_pattern',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='readnoise_diff_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='readnoise_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='subarray',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nirspecreadnoisestats',
            name='uncal_filename',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='thumbnail_path',
            field=models.CharField(default='', help_text='Path to the proposal thumbnail', max_length=1000),
        ),
    ]
