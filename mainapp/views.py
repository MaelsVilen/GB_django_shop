from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def test_context(request):
    context = {
        'title': 'добро пожаловать',
        'username': 'Михаил Пигузов',
        'products': [
            {'name': 'Чёрное худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 800 руб.'},
        ],
        'promotion': True,
        'promotion products': [
            {'name': 'Туфли Dr Martines', 'price': '10 000 руб.'},
        ],
    }

    return render(request, 'mainapp/context.html', context)