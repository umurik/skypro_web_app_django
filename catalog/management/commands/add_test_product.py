from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name="Тестовая категория")
        products = [
            {
                "name": "Тестовый прод. 1",
                "description": "Продукт для тестов",
                "image": "catalog/data/images/test_image.png",
                "category": category,
                "price": 1021,
            },
            {
                "name": "Тестовый прод. 2",
                "description": "Продукт для тестов",
                "image": "catalog/data/images/test_image.png",
                "category": category,
                "price": 2021,
            },
        ]

        for product in products:
            prod, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added: {prod.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Doesn't added: {prod.name}"))
