from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random
import time 
# Create your views here.

menu_items = [
    {'meal': 'Grilled Salmon', 'price': 33},
    {'meal': 'Caesar Salad', 'price': 15},
    {'meal': 'Flounder', 'price': 36},
    {'meal': 'Steak Frites', 'price': 48},
    {'meal': 'Fish & Chips', 'price': 30},
    {'meal': 'Lobster and Broccoli', 'price': 56},
    {'meal': 'Boathouse Burger', 'price': 27},
    {'meal': 'Tuna', 'price': 34},
    {'meal': 'NY Strip Steak', 'price': 42},
    {'meal': 'Crab Cakes', 'price': 40},
]
extras = [
    {'meal': 'Add Butter', 'price': 5},
    {'meal': 'Clam Chowder Soup', 'price': 8},
]
daily_specials = [
    {'meal': 'Surf & Turf', 'price': 50},
    {'meal': 'Boathouse Bouillabaise', 'price': 35},
    {'meal': 'Catch of the Day', 'price': 30},
]
def main(request):
    '''Respond to the URL 'main', delegate work to a template.'''

    template_name = 'restaurant/main.html'
    # a dict of context variables (key-value pairs)
    context = {
       
    }
    return render(request, template_name, context)

def order(request):
    '''Respond to the URL 'order', delegate work to a template.'''

    template_name = 'restaurant/order.html'
    # a dict of context variables (key-value pairs)
    context = {
        'menu_items': menu_items, 
        'daily_special': random.choice(daily_specials),
    }
    return render(request, template_name, context)

def confirmation(request):
    '''Process the form submission, and generate a result.'''

    template_name = "restaurant/confirmation.html"
    print(request)

    # check if POST data was sent with the HTTP POST message:
    if request.POST:

        # extract form fields into variables:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        items_ordered = request.POST.getlist('menu_items') # searched how to fix mutlivaluedicterror-needed .getlist
        daily_special = request.POST.get('daily_special')
        special_instructions = request.POST.get('instructions')

        # for calculating the total price of customers order
        total_cost = 0
        for item in menu_items:
            if item['meal'] in items_ordered:
                total_cost += item['price']

        for item in extras: 
            if item['meal'] in items_ordered:
                total_cost += item['price']

        if daily_special:
            for special in daily_specials:
                if special['meal'] == daily_special:
                    total_cost += special['price']

        wait_time = random.randint(30, 60)
        expected_time = time.ctime(time.time() + wait_time * 60)

        # create context variables for use in the template
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'items_ordered': items_ordered,
            'daily_special': daily_special,
            'special_instructions': special_instructions,
            'total_cost': total_cost,
            'expected_time': expected_time,
        }
    else: # for if they leave everything empty and press submit, so site does not crash
        context = {} 

    # delegate the response to the template, provide context variables
    return render(request, template_name=template_name, context=context)