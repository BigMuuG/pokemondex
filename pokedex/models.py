from django.db import models


# Manager for ordering
class Ordering(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')


class Abilities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    is_main_series = models.IntegerField(blank=True, null=True)

    objects = Ordering()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'abilities'


class AbilityFlavorText(models.Model):
    ability = models.ForeignKey(
        Abilities, models.DO_NOTHING, primary_key=True, related_name='flavortext')
    version_group_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ability_flavor_text'


class EvoOrdering(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('first', 'second', 'third')


class Evolutions(models.Model):
    pokemon = models.ForeignKey(
        'Pokemon', models.DO_NOTHING, related_name='evolutions', blank=True, null=True)
    first = models.ForeignKey(
        'Pokemon', models.DO_NOTHING, related_name='firstevo', blank=True, null=True)
    second = models.ForeignKey(
        'Pokemon', models.DO_NOTHING, related_name='secondevo', blank=True, null=True)
    third = models.ForeignKey(
        'Pokemon', models.DO_NOTHING, related_name='thirdevo', blank=True, null=True)

    objects = EvoOrdering()

    # def __str__(self):
    #     if not self.second_id:
    #         return '{}'.format(self.first_id)

    #     elif not self.third_id:
    #         return '{}, {}'.format(self.first_id, self.second_id)

    #     return '{}, {}, {}'.format(self.first_id, self.second_id, self.third_id)

    class Meta:
        managed = False
        db_table = 'evolutions'


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
    move = models.ForeignKey('Moves', models.DO_NOTHING,
                             primary_key=True, related_name='flavortext')
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

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'move_methods'


class Moves(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation_id = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    # type_id = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    damage_class_id = models.IntegerField(blank=True, null=True)
    effect_id = models.IntegerField(blank=True, null=True)
    effect_chance = models.TextField(blank=True, null=True)

    objects = Ordering()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'moves'


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    first_evo_id = models.IntegerField()
    second_evo_id = models.IntegerField()
    third_evo_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    base_experience = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_padded_id(self):
        return str(self.id).zfill(3)

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonAbilities(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    ability = models.ForeignKey(Abilities, models.DO_NOTHING, primary_key=True)
    slot = models.IntegerField(blank=True, null=True)

    def __str__(self):
        id = '{} {}'.format(self.pokemon, self.ability)
        return id

    class Meta:
        managed = False
        db_table = 'pokemon_abilities'
        unique_together = (('pokemon', 'ability'),)


class PokemonFlavorText(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, primary_key=True, related_name='flavortext')
    version_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_flavor_text'


class PokemonMoves(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(Moves, models.DO_NOTHING, primary_key=True)
    move_method = models.ForeignKey(
        MoveMethods, models.DO_NOTHING, primary_key=True)
    level = models.IntegerField(primary_key=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        id = '{} {}'.format(self.pokemon, self.move)
        return id

    class Meta:
        managed = False
        db_table = 'pokemon_moves'
        unique_together = (('pokemon', 'move', 'level', 'move_method'),)


class DistinctPokemonMoves(models.Model):
    pokemon = models.ForeignKey('Pokemon', models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey('Moves', models.DO_NOTHING)
    move_method = models.ForeignKey('MoveMethods', models.DO_NOTHING)
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        id = '{} {}'.format(self.pokemon, self.move)
        return id

    class Meta:
        managed = False
        db_table = 'distinct_pokemon_moves'
        unique_together = (('pokemon', 'move', 'level', 'move_method'),)


class PokemonStats(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, primary_key=True, related_name='pstats')
    stat = models.ForeignKey('Stats', models.DO_NOTHING, primary_key=True)
    base_stat = models.IntegerField(blank=True, null=True)
    effort = models.IntegerField(blank=True, null=True)

    def __str__(self):
        id = '{} {}'.format(self.pokemon, self.stat)
        return id

    class Meta:
        managed = False
        db_table = 'pokemon_stats'
        unique_together = (('pokemon', 'stat'),)


class TypeOrdering(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('pokemon', 'slot')


class PokemonTypes(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    slot = models.IntegerField(blank=True, null=True)

    objects = TypeOrdering()

    def __str__(self):
        id = '{} {}'.format(self.pokemon, self.type)
        return id

    def get_name(self):
        return '{}'.format(self.pokemon)

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

    objects = Ordering()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'stats'


class TypeEfficacy(models.Model):
    damage_type = models.ForeignKey(
        'Types', models.DO_NOTHING, primary_key=True)
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

    objects = Ordering()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'types'
