from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
    # return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')


#1.od P:
# title = 'przejdz na produkty'
# productsAboutResponse = f'''
#     products/about 🚀 <a href="/products">{title}</a>
#     *dodałam ten wiersz i tutaj wpisuję tekst na stronę, który chcę, żeby się wyświetlił. 🎨
#     *I jeszcze ten wiersz 👓🚙😎
#     '''


## def products(request):
#     return HttpResponse('products 🚀 *mój tekst🦋👀🦚* <a href="/products/about">about</a> <br/> <marquee>Heloo to moja pierwsza stroanaanaaaaa!</marquee>')

# def productsAbout(request):
#     return HttpResponse(productsAboutResponse)
