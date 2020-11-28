# Generated by Django 3.1.3 on 2020-11-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ploting', '0003_auto_20201128_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='first_payment_by_cheque',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='second_payment_by_cheque',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='third_payment_by_cheque',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='plot',
            name='agreement1',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='agreement2',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='agreement3',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='agreement4',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='first_payment_cheque',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='initial_information1',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil1',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil10',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil11',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil12',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil13',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil14',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil15',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil16',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil17',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil18',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil19',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil2',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil20',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil3',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil4',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil5',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil6',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil7',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil8',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil9',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mul_dolil_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation1',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation2',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation3',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation4',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation5',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='mutuation_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='second_payment_cheque',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='plot',
            name='third_payment_cheque',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='agreement',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='initial_information',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
    ]
