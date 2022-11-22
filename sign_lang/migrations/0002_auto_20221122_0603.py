# Generated by Django 3.2 on 2022-11-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_lang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250, verbose_name='제목')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('label', models.CharField(choices=[(65, 'A'), (66, 'B'), (67, 'C'), (68, 'D'), (69, 'E'), (70, 'F'), (71, 'G'), (72, 'H'), (73, 'I'), (74, 'J'), (75, 'K'), (76, 'L'), (77, 'M'), (78, 'N'), (79, 'O'), (80, 'P'), (81, 'Q'), (82, 'R'), (83, 'S'), (84, 'T'), (85, 'U'), (86, 'V'), (87, 'W'), (88, 'X'), (89, 'Y'), (90, 'Z')], default='A', max_length=2, verbose_name='번역')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VideoObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250, verbose_name='제목')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('text', models.CharField(max_length=250, verbose_name='번역')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='ImageTranslation',
        ),
        migrations.DeleteModel(
            name='VideoTranslation',
        ),
    ]
