from .models import Fooddish


def list_all_dish():
    """ Listing all dishs in database """

    dishs = Fooddish.objects.all().values('id', 'name')
    return dishs
