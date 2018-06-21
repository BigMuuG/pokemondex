from django import template

register = template.Library()


@register.filter
def pokemon_sprite(value):
    return 'pokedex/full_size_pokemon{0:03d}.png'.format(value)


@register.filter
def addstr(value, arg):
    value = str(value)
    arg = str(arg)
    if arg:
        return value + arg
    else:
        return


@register.filter
def divp(value, arg):

    value = int(value)
    arg = int(arg)
    if arg:
        return 100 * value / arg
    else:
        return
