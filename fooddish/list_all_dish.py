from .models import Fooddish


def list_all_dish():
    """ Listing all dishs in database """
    dish_sorted = [('default', 'Choisissez un plat'),]
    dishs = Fooddish.objects.all()

    for i in dishs:
        dish = (i.pk, i.name)
        dish_sorted.append(dish)

    return dish_sorted
