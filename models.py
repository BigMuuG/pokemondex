# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abilities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    is_main_series = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abilities'


class MoveMethods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_methods'


class Moves(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    damage_class_id = models.IntegerField(blank=True, null=True)
    effect_id = models.IntegerField(blank=True, null=True)
    effect_chance = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.TextField(blank=True, null=True)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    base_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonAbilities(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    ability = models.ForeignKey(Abilities, models.DO_NOTHING)
    slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_abilities'
        unique_together = (('pokemon', 'ability'),)


class PokemonMoves(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(Moves, models.DO_NOTHING)
    move_method = models.ForeignKey(MoveMethods, models.DO_NOTHING)
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'
        unique_together = (('pokemon', 'move', 'level', 'move_method'),)


class PokemonStats(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    stat = models.ForeignKey('Stats', models.DO_NOTHING)
    base_stat = models.IntegerField(blank=True, null=True)
    effort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_stats'
        unique_together = (('pokemon', 'stat'),)


class PokemonTypes(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey('Types', models.DO_NOTHING)
    slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_types'
        unique_together = (('pokemon', 'type'),)


class Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_class_id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    is_battle_only = models.IntegerField(blank=True, null=True)
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'
