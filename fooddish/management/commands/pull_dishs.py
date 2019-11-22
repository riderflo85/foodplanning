import os, json
from django.core.management.base import BaseCommand
from fooddish.models import Fooddish


class Command(BaseCommand):
    help = "Ajout de plusieurs plats dans la base de données"

    def handle(self, *args, **options):
        directory = os.path.dirname(__file__)
        json_file = os.path.join(directory, "../..", "dishs_base.json")

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

                for i in data['name']:
                    Fooddish(name=i).save()

                    self.stdout.write(
                        f"{self.style.SUCESS(i)} ajouté à la base de données"
                    )

            self.stdout.write(self.style.SUCCESS('Les plats ont correctement \
été ajoutés dans la base de données'))

        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl se peut que les aliments existe déjà.'))
