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


@register.filter
def heightconv(value):

    value = int((value*10)/2.54)
    return "{}\' {:02d}\'\'".format(value // 12, value % 12)


@register.filter
def weightconv(value):

    value = (value/10)/2.2
    return "{:0.1f} lbs".format(value)
