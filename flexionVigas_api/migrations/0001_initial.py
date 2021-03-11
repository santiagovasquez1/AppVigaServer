# Generated by Django 3.1.5 on 2021-03-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VigaRectangular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('r', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('d', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cuantiaTemp', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('cuantiaMin', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('cuantiaMax', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('cuantiaReq', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('asTemp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('asMin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('asMax', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('asReq', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('asReq2', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Mu', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('phiFlexion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('phiMn', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('phiMnMax', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
