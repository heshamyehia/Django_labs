from django.shortcuts import render

MENU_ITEMS = [
    {'name': 'Burger',          'category': 'Main',     'price': 120, 'available': True},
    {'name': 'Grilled Chicken', 'category': 'Main',     'price': 150, 'available': True},
    {'name': 'Pasta Carbonara', 'category': 'Main',     'price': 110, 'available': False},
    {'name': 'Orange Juice',    'category': 'Drinks',   'price': 35,  'available': True},
    {'name': 'Mango Smoothie',  'category': 'Drinks',   'price': 45,  'available': True},
    {'name': 'French Fries',    'category': 'Sides',    'price': 40,  'available': True},
    {'name': 'Coleslaw',        'category': 'Sides',    'price': 30,  'available': True},
    {'name': 'Chocolate Cake',  'category': 'Desserts', 'price': 60,  'available': True},
    {'name': 'Ice Cream',       'category': 'Desserts', 'price': 50,  'available': False},
]

CATEGORIES = ['Main', 'Drinks', 'Sides', 'Desserts']


def menu_list(request):
    items = MENU_ITEMS
    query = request.GET.get('q')
    selected_category = request.GET.get('category')


    if selected_category:
        items = [item for item in items if item['category'] == selected_category]

    if query:
        items = [item for item in items if query.lower() in item['name'].lower()]

    context = {
        'items': items,
        'categories': CATEGORIES,
        'query': query,
        'selected_category': selected_category,
    }
    return render(request, 'base.html', context)