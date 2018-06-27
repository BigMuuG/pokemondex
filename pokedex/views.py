from django.views import generic
from .models import Pokemon, Moves, Abilities, Types
# from django.core.paginator import Paginator


def unique(list1):

    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


class IndexView(generic.ListView):
    template_name = 'pokedex/pokemon_list.html'
    queryset = Pokemon.objects.all()
    paginate_by = 45
    paginate_orphans = 8
    context_object_name = 'pokemon_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pokemon_nav'] = Pokemon.objects.only('id', 'name')
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        return context


class PokemonDetailView(generic.DetailView):
    model = Pokemon
    template_name = 'pokedex/pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PokemonDetailView, self).get_context_data(**kwargs)
        context['pokemon_nav'] = Pokemon.objects.only('id', 'name')
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        stats_list = self.object.pstats.all()
        context['stats'] = []
        for i in stats_list:
            context['stats'].append(i)

        context['pokemon_abilities'] = self.object.pokemonabilities_set.all()

        context['first_type'] = self.object.pokemontypes_set.first().type
        context['second_type'] = self.object.pokemontypes_set.last().type

        context['flavor'] = self.object.flavortext.get().flavor_text

        ordered_moves = self.object.distinctpokemonmoves_set.order_by(
            'level', 'move_id')

        context['level_moves'] = ordered_moves.filter(move_method=1)
        context['breed_moves'] = ordered_moves.filter(move_method=2)
        context['tutor_moves'] = ordered_moves.filter(move_method=3)
        context['machine_moves'] = ordered_moves.filter(move_method=4)

        if self.object.evolutions.first():
            evolutions_stage_one = []
            evolutions_stage_two = []
            evolutions_stage_three = []
            evolution_set = self.object.evolutions.first().first.evolutions.all()
            last_evolutions = evolution_set.first()
            j = 0
            for i in evolution_set:
                if (j > 0) & (i.first != last_evolutions.first):
                    evolutions_stage_one.append(i.first)
                elif j == 0:
                    evolutions_stage_one.append(i.first)
                if i.second:
                    if (j > 0) & (i.second != last_evolutions.second):
                        evolutions_stage_two.append(i.second)
                    elif j == 0:
                        evolutions_stage_two.append(i.second)

                if i.third:

                    if (j > 0) & (i.third != last_evolutions.third):
                        evolutions_stage_three.append(i.third)

                    elif j == 0:
                        evolutions_stage_three.append(i.third)

                j += 1
                last_evolutions = i
            context['evolutions_stage_one'] = evolutions_stage_one
            context['evolutions_stage_two'] = evolutions_stage_two
            context['evolutions_stage_three'] = evolutions_stage_three

            # Special pokemon evolutions:
            # evee, mime, jynx, electabuzz, magmar, tyrogue, chansey, tangela

        return context


class MoveDetailView(generic.DetailView):
    model = Moves
    template_name = 'pokedex/move_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MoveDetailView, self).get_context_data(**kwargs)
        context['pokemon_nav'] = Pokemon.objects.only('id', 'name')
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Relates the view's current context Move to a list of corresponding Pokemon
        pokemonmoves = self.object.distinctpokemonmoves_set.all()
        p_moves = []
        j = 1
        for i in pokemonmoves:
            p_moves.append(i)
            if (pokemonmoves[j-1] != pokemonmoves.last()):
                if (i.pokemon == pokemonmoves[j].pokemon):
                    p_moves.remove(i)
            j += 1
        context['pokemonmoves'] = p_moves

        context['flavor'] = self.object.flavortext.get().flavor_text
        return context


class AbilityDetailView(generic.DetailView):
    model = Abilities
    template_name = 'pokedex/ability_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AbilityDetailView, self).get_context_data(**kwargs)
        context['pokemon_nav'] = Pokemon.objects.only('id', 'name')
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Relates the view's current context Ability to a list of corresponding Pokemon
        context['pokemonabilities'] = self.object.pokemonabilities_set.all()

        context['flavor'] = self.object.flavortext.get().flavor_text
        return context


class TypeDetailView(generic.DetailView):
    model = Types
    template_name = 'pokedex/type_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TypeDetailView, self).get_context_data(**kwargs)
        context['pokemon_nav'] = Pokemon.objects.only('id', 'name')
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Relates the view's current context Type to a list of corresponding Pokemon
        context['pokemontypes'] = self.object.pokemontypes_set.all()

        return context
