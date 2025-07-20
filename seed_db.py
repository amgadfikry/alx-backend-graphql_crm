#!/usr/bin/env python

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphql_crm.settings')
django.setup()

from crm.models import Customer, Product, Order


def seed_database():
    customers_data = [
        {"name": "test test 1", "email": "test1@example.com", "phone": "+1234567890"},
        {"name": "test test 2", "email": "test2@example.com", "phone": "1234567890"},
        {"name": "test test 3", "email": "test3@example.com", "phone": "+1234567890"},
        {"name": "test test 4", "email": "test4@example.com"},
        {"name": "test test 5", "email": "test5@example.com", "phone": "+1234567890"},
    ]

    customers = []
    for data in customers_data:
        customer, created = Customer.objects.get_or_create(
            email=data['email'],
            defaults=data
        )
        customers.append(customer)

    products_data = [
        {"name": "prod1", "price": 10, "stock": 10},
        {"name": "prod2", "price": 20, "stock": 20},
        {"name": "prod3", "price": 30, "stock": 30},
        {"name": "prod4", "price": 40, "stock": 40},
        {"name": "prod5", "price": 50, "stock": 50},
    ]

    products = []
    for data in products_data:
        product, created = Product.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        products.append(product)

    if customers and products:
        order1, created = Order.objects.get_or_create(
            customer=customers[0],
            defaults={}
        )
        if created:
            order1.products.set([products[0], products[1]])
            order1.calculate_total()
            order1.save()

        order2, created = Order.objects.get_or_create(
            customer=customers[1],
            defaults={}
        )
        if created:
            order2.products.set([products[2], products[4]])  # Keyboard + Headphones
            order2.calculate_total()
            order2.save()

if __name__ == '__main__':
    seed_database()