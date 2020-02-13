from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    
    help = "This comman tells me that he loves me"
    
    """
    def add_arguments(self, parser):
        
        
        parser.add_argument(
            "--times", help = "How many times do you want me to tell you that I love"
        )
    """
        
    def handle(self, *args, **options):
        amenities = [          	
            "에어컨",
            "난방",
            "헤어드라이어",
            "옷장/서랍장",
            "다리미",
            "TV",
            "벽난로",
            "게스트 전용 출입문",
            "샴푸",
            "무선인터넷",
            "업무 가능 공간/책상",
            "조식, 커피, 차",
        ]
        
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))
            