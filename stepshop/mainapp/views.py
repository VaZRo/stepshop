from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'Home'},
        {'link': 'products:index', 'name': 'Products'},
        {'link': 'about', 'name': 'About Us'},
        {'link': 'contacts', 'name': 'Contacts'},
    ]

    categories = Category.objects.all()

    context = {
        'links_menu': links_menu,
        'categories': categories,
    }

    context.update(**kwargs)
    return context


def index(request):
    title = "Главная"
    context = get_data(title=title)
    return render(request, 'index.html', context)


def about(request):
    title = "Информация"
    context = get_data(title=title)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"
    context = get_data(title=title)
    return render(request, 'contacts.html', context)


def products(request, pk=None):
    title = "Каталог продуктов"
    context = {}

    prods = Product.objects.order_by('price')
    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        prods = Product.objects.filter(category__pk=pk).order_by('price')
        context = get_data(category=category)


    context = get_data(title=title, prods=prods, **context)
    return render(request, 'products.html', context)


def product(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    context = get_data(title=title, prod=prod)
    return render(request, 'product.html', context)

