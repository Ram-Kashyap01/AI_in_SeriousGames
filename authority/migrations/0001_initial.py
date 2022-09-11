# Generated by Django 3.1.7 on 2022-03-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceType', models.CharField(choices=[('Games', 'Games'), ('Techniques', 'Techniques'), ('Articles', 'Articles')], max_length=200)),
                ('resourceTitle', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('algorithmUsed', models.CharField(choices=[('Artificial Neural Networks', 'Artificial Neural Networks'), ('Naive Based Classifier', 'Naive Based Classifier'), ('Case Based Reasoning', 'Case Based Reasoning'), ('Support Vector Machines', 'Support Vector Machines'), ('Decision Trees', 'Decision Trees'), ('Fuzzy Logic', 'Fuzzy Logic'), ('Markov Systems', 'Markov Systems'), ('Goal Oriented Behavior', 'Goal Oriented Behavior'), ('Rule-based Systems', 'Rule-based Systems'), ('Finate-State Machines', 'Finate-State Machines')], max_length=200)),
                ('techniqueUsed', models.CharField(max_length=200)),
                ('techniqueDescription', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='res/')),
                ('requestStatus', models.CharField(default='admin', max_length=200)),
                ('userId', models.IntegerField(default=0, max_length=200)),
            ],
        ),
    ]