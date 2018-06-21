from django.views import generic
from .models import Pokemon, Moves, Abilities, Types


class IndexView(generic.ListView):
    template_name = 'pokedex/pokemon_list.html'
    queryset = Pokemon.objects.all().prefetch_related('pokemontypes_set')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Getting types for each pokemon
        temp_object_list = []
        for i in self.queryset:
            temp_object_list.append(i.pokemontypes_set.all())

        temp_object_list2 = []
        j = 0
        for i in temp_object_list:
            if(i.count() == 2):
                temp_object_list2.append(
                    [i.first().type.name, i.last().type.name])

            else:
                temp_object_list2.append([i.first().type.name, "NULL"])

            j += 1

        context['pokemon_list'] = zip(self.queryset, temp_object_list2)

        return context


class PokemonDetailView(generic.DetailView):
    model = Pokemon
    template_name = 'pokedex/pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PokemonDetailView, self).get_context_data(**kwargs)
        context['moves_nav'] = Moves.objects.all()
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        stats_list = self.object.pstats.all()
        context['stats'] = []
        for i in stats_list:
            context['stats'].append(i)

        # context['stat_values'] = []
        # for i in stats_list:
        #     context['stats'].append(i.stat)

        context['first_type'] = self.object.pokemontypes_set.first().type
        context['second_type'] = self.object.pokemontypes_set.last().type

        context['flavor'] = self.object.flavortext.get().flavor_text
        return context


class MoveDetailView(generic.DetailView):
    model = Moves
    template_name = 'pokedex/move_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MoveDetailView, self).get_context_data(**kwargs)
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # MySQL DISTINCT ON incompatibility workaround
        context['pokemonmoves'] = Pokemon.objects.filter(id__in=Moves.objects.get(
            id=self.object.id).pokemonmoves_set.values_list('pokemon', flat=True).distinct()
        )

        context['flavor'] = self.object.flavortext.get().flavor_text
        return context


class AbilityDetailView(generic.DetailView):
    model = Abilities
    template_name = 'pokedex/ability_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AbilityDetailView, self).get_context_data(**kwargs)
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Relates the view's current context Ability to a list of corresponding Pokemon
        context['pokemonabilities'] = Abilities.objects.get(
            id=self.object.id).pokemonabilities_set.all()

        context['flavor'] = self.object.flavortext.get().flavor_text
        return context


class TypeDetailView(generic.DetailView):
    model = Types
    template_name = 'pokedex/type_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TypeDetailView, self).get_context_data(**kwargs)
        context['moves_nav'] = Moves.objects.only('id', 'name')
        context['types_nav'] = Types.objects.only('id', 'name')
        context['abilities_nav'] = Abilities.objects.only('id', 'name')

        # Relates the view's current context Type to a list of corresponding Pokemon
        context['pokemontypes'] = Types.objects.get(
            id=self.object.id).pokemontypes_set.all()

        return context
