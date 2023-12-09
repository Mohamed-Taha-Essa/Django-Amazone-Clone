import os ,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from products.models import Product, ProductImages, Brand, Review  
import random
from django.utils.text import slugify


fake=Faker()

def seed_brands(num_brands):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg', ]
    for _ in range(num_brands):
        brand = Brand.objects.create(
            name=fake.company(),
            image=f'brand/{imgs[random.randint(0,5)]}',
        )
    
    print('brand addec successfully')

def unique_slug(name):
    slug = slugify(name)[:50]  # Truncate slug to a reasonable length
    counter = 1
    while Product.objects.filter(slug=slug).exists():
        slug = f"{slug}-{counter}"
        counter += 1
    return slug


def seed_product(n):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg',
           '07.jpg','08.jpg','09.jpg','10.jpg','11.jpg','12.jpg',
           '13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg',
           '19.jpg','20.jpg',
        ]

    brand =Brand.objects.all()
    for _ in range(n):
        name = fake.company()  # Generate a fake company name
        slug =unique_slug(name)

        Product.objects.create(
            brand =brand[random.randint(0,len(brand)-1)] ,
            name = name,
            flag=fake.random_element(elements=('New', 'Sale', 'Feature')),
            image = f'product/{imgs[random.randint(0,19)]}',
            price = fake.random_number(digits=2),
            sku=fake.unique.random_number(digits=5),
            subtitle=fake.sentence(nb_words=60),
            description=fake.paragraph(nb_sentences = 80),
            slug =slug
            

        )
    print('products added successfully')




# seed_brands(200)
seed_product(200)