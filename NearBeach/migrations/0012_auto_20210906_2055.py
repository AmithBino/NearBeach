# Generated by Django 3.2.5 on 2021-09-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0011_auto_20210825_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag_assignment',
            name='opportunity',
        ),
        migrations.RemoveField(
            model_name='tag_assignment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='tag_assignment',
            name='requirement',
        ),
        migrations.RemoveField(
            model_name='tag_assignment',
            name='task',
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_colour',
            field=models.CharField(default='#651794', max_length=7),
        ),
        migrations.AddField(
            model_name='tag_assignment',
            name='object_enum',
            field=models.CharField(choices=[('requirement', 'Requirement'), ('requirement_item', 'Requirement Item'), ('project', 'Project'), ('task', 'Task'), ('kanban_board', 'Kanban Board'), ('kanban_card', 'Kanban Card'), ('request_for_change', 'Reuqest for Change'), ('customer', 'Customer'), ('organisation', 'Organisation')], default='requirement', max_length=40),
        ),
        migrations.AddField(
            model_name='tag_assignment',
            name='object_id',
            field=models.IntegerField(default=0),
        ),
    ]
