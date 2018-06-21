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


class AbilityFlavorText(models.Model):
    ability = models.ForeignKey(Abilities, models.DO_NOTHING, primary_key=True)
    version_group_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ability_flavor_text'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EvolutionTriggerProse(models.Model):
    evolution_trigger_id = models.IntegerField(blank=True, null=True)
    local_language_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolution_trigger_prose'


class Machines(models.Model):
    machine_number = models.IntegerField(blank=True, null=True)
    version_group_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    move_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines'


class MoveFlavorText(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    version_group_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_flavor_text'


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
    name = models.TextField(blank=True, null=True)
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


class PokemonEvolution(models.Model):
    id = models.IntegerField(primary_key=True)
    evolved_pokemon_id = models.IntegerField()
    evolution_trigger_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_evolution'
        unique_together = (('id', 'evolved_pokemon_id'),)


class PokemonFlavorText(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    version_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_flavor_text'


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


class TypeEfficacy(models.Model):
    damage_type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    target_type_id = models.IntegerField()
    damage_factor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_efficacy'
        unique_together = (('damage_type', 'target_type_id'),)


class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'
