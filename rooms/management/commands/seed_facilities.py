from django.core.management.base import BaseCommand
# from django_seed import Seed
from rooms.models import Facility

class Command(BaseCommand):
    
    help = "This comman creates facilities"
    
    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help = "How many users do you want to create"
        )
        
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(Facilitiy, number, {
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} facility created!!"))
    """
        
    def handle(self, *args, **options):
        facilities = [
            "Parivate entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym"
        ]
        
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} Facilities created!'))
            