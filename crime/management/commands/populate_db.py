import pytz
import random
from crime.models import Category, Log
from users.models import Profile
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    def add_arguments(self, parser):
        parser.add_argument('--report', type=int, help='The number of reports to be created')

    def handle(self, *args, **options):
        names = ['Sex', 'Vandalism', 'Theft', 'homocide','Aggravated', 'Assault', 'Raids', 'Terrorism']
        other = ['Trafficking', 'Vandalism', 'Theft', 'homocide','Killing', 'Assault', 'Raids', 'Terrorism']
        words = [
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
            'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which dont look even slightly believable.',
            'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.',
            'Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
            'Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.',
        ]
        places = ['Meru', 'Lafey', 'Anio', 'El Wak', 'Bur Mayo', 'Damasa', 'Finno', 'Madera', 'Ramu', 'Takaba', 'Waragalla', 'Arabia', 'Rhamu']

        surname = [
            Profile.objects.get_or_create(user='James'), Profile.objects.get_or_create(user='John'),
            Profile.objects.get_or_create(user='Robert'), Profile.objects.get_or_create(user='Michael'),
            Profile.objects.get_or_create(user='William'), Profile.objects.get_or_create(user='David'),
            Profile.objects.get_or_create(user='Richard'), Profile.objects.get_or_create(user='Joseph'),
            Profile.objects.get_or_create(user='Thomas'), Profile.objects.get_or_create(user='Charles'),
            Profile.objects.get_or_create(user='Angeline'), Profile.objects.get_or_create(user='Milka'),
            Profile.objects.get_or_create(user='Suleiman'), Profile.objects.get_or_create(user='Ahmed'),
            Profile.objects.get_or_create(user='Zulpha'), Profile.objects.get_or_create(user='Khadija'),
        ]

        categories = [
            Category.objects.get_or_create(name='Robbery'), Category.objects.get_or_create(name='Drugs'),
            Category.objects.get_or_create(name='Arson'), Category.objects.get_or_create(name='Kidnapping'),
            Category.objects.get_or_create(name='Domestic Abuse'), Category.objects.get_or_create(name='Assault'),
            Category.objects.get_or_create(name='Raids'), Category.objects.get_or_create(name='Terrorism'),
        ]
        report = options['report'] if options['report'] else 1000
        for i in range(0, report):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            log = Log.objects.create(
                case=random.choice(names) + ' ' + random.choice(other),
                details=random.choice(words),
                location=random.choice(places),
                author=random.choice(surname),
                type=random.choice(categories)[0],
                num_reported=random.randint(34, 789),
            )
            log.date_posted = dt
            log.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
