from django.core.management.base import BaseCommand
from library.models import Book
from faker import Faker

class Command(BaseCommand):
    help = 'Generate random books'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(30):
            Book.objects.create(
                title=f"{fake.word().title()} Programming {i+1}",
                author=fake.name(),
                isbn=str(fake.random_number(digits=13, fix_len=True))
            )
        self.stdout.write(self.style.SUCCESS("✅ 30개의 책 생성 완료!"))
