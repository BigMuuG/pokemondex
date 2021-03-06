# Generated by Django 2.0.6 on 2018-06-25 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('generation_id', models.IntegerField(blank=True, null=True)),
                ('is_main_series', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_id', models.IntegerField(blank=True, null=True)),
                ('second_id', models.IntegerField(blank=True, null=True)),
                ('third_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evolutions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvolutionTriggerProse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolution_trigger_id', models.IntegerField(blank=True, null=True)),
                ('local_language_id', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evolution_trigger_prose',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_number', models.IntegerField(blank=True, null=True)),
                ('version_group_id', models.IntegerField(blank=True, null=True)),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('move_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'machines',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoveMethods',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'move_methods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('species_id', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('base_experience', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('damage_class_id', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('is_battle_only', models.IntegerField(blank=True, null=True)),
                ('game_index', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('generation_id', models.IntegerField(blank=True, null=True)),
                ('damage_class_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AbilityFlavorText',
            fields=[
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='flavortext', serialize=False, to='pokedex.Abilities')),
                ('version_group_id', models.IntegerField(blank=True, null=True)),
                ('language_id', models.IntegerField(blank=True, null=True)),
                ('flavor_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ability_flavor_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DistinctPokemonMoves',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pokedex.Pokemon')),
                ('level', models.IntegerField()),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'distinct_pokemon_moves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('generation_id', models.IntegerField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.Types')),
                ('power', models.IntegerField(blank=True, null=True)),
                ('pp', models.IntegerField(blank=True, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('target_id', models.IntegerField(blank=True, null=True)),
                ('damage_class_id', models.IntegerField(blank=True, null=True)),
                ('effect_id', models.IntegerField(blank=True, null=True)),
                ('effect_chance', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'moves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PokemonAbilities',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pokedex.Pokemon')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.Abilities')),
                ('slot', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon_abilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PokemonFlavorText',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='flavortext', serialize=False, to='pokedex.Pokemon')),
                ('version_id', models.IntegerField(blank=True, null=True)),
                ('language_id', models.IntegerField(blank=True, null=True)),
                ('flavor_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon_flavor_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PokemonMoves',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pokedex.Pokemon')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.Moves')),
                ('move_method', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.MoveMethods')),
                ('level', models.IntegerField(primary_key=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon_moves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PokemonStats',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='pstats', serialize=False, to='pokedex.Pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.Stats')),
                ('base_stat', models.IntegerField(blank=True, null=True)),
                ('effort', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon_stats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PokemonTypes',
            fields=[
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pokedex.Pokemon')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='pokedex.Types')),
                ('slot', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokemon_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeEfficacy',
            fields=[
                ('damage_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pokedex.Types')),
                ('target_type_id', models.IntegerField()),
                ('damage_factor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'type_efficacy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoveFlavorText',
            fields=[
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='flavortext', serialize=False, to='pokedex.Moves')),
                ('version_group_id', models.IntegerField(blank=True, null=True)),
                ('language_id', models.IntegerField(blank=True, null=True)),
                ('flavor_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'move_flavor_text',
                'managed': False,
            },
        ),
    ]
