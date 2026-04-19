from django.core.management.base import BaseCommand
from fertzmall_scrapers.afrimash_scraper import scrape_page
from fertzmall_scrapers.models import Product
import pandas as pd
import re

class Command(BaseCommand):
    help = 'Import data from CSV file into the database'

    def handle(self, *args, **kwargs):
        # Delete all existing data from the Product model
        Product.objects.all().delete()
        
        # Read data from the CSV file
        df = pd.read_csv('products.csv')

        # Iterate over each row in the DataFrame and create a Product object for each
        for index, row in df.iterrows():

            # Clean the price value (remove currency symbols and commas)
            price_cleaned = re.sub(r'[^\d.]', '', row['Price'])

            Product.objects.create(
                name=row['Name'],
                image_url=row['Image_URL'],
                price=price_cleaned,
                url=row['URL']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))