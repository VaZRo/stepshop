from django.shortcuts import render


links_menu = [
        {'link': 'index', 'name': 'Home'},
        {'link': 'products:index', 'name': 'Products'},
        {'link': 'about', 'name': 'About Us'},
        {'link': 'contacts', 'name': 'Contacts'},
    ]


def index(request):
    title = "Главная"
    context = {
        "title": title,
        'links_menu': links_menu,
    }
    return render(request, 'index.html', context)


def about(request):
    title = "Информация"
    context = {
        "title": title,
        'links_menu': links_menu,
    }
    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"
    context = {
        "title": title,
        'links_menu': links_menu,
    }
    return render(request, 'contacts.html', context)


def products(request):
    title = "Каталог продуктов"
    context = {
        "title": title,
        'links_menu': links_menu,
    }
    return render(request, 'products.html', context)


def product(request):
    title = "Продукт"
    context = {
        "title": title,
        'links_menu': links_menu,
    }
    return render(request, 'product.html', context)

