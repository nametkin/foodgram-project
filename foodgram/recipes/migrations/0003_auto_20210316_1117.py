# Generated by Django 3.1.7 on 2021-03-16 08:17

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210315_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='_real_author_name',
            field=models.CharField(default='# not defined #', editable=False, max_length=150),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='tags',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Завтрак'), (2, 'Обед'), (3, 'Ужин')], default=2, max_length=5),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]