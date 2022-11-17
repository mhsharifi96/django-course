from django.shortcuts import render,HttpResponse

import requests

from .models import Product

def index(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    context = {'product': product, 'recently_viewed_products': recently_viewed_products}
    return render(request, 'shop/product.html', context)


def limit_seen_main_page(request):
    print('session expire age  : ',request.session.get_expiry_age())
    if request.session.get('limit_seen',False):
        print('limit seen type :',type(request.session['limit_seen']))
        if request.session['limit_seen'] >= 3:
            return HttpResponse("Limited! you can seen this page just 3 times")

        request.session['limit_seen'] +=1

    else : 
        request.session.set_expiry(60) 
        request.session['limit_seen'] = 1
    
    request.session['has_commented'] = True
    # request.session['seen_page'] = 
    return HttpResponse(f"Number of page visited : {request.session['limit_seen']}")



def sample_cookie(request):
    response = HttpResponse("set cookie is worked !")
    response.set_cookie('changed',True)
    response.set_cookie('language','english')
    return response

def read_cookie(request):
    change = request.COOKIES['changed']
    language = request.COOKIES['language']
    print(change,' : ',language)

    response = HttpResponse("read cookie!")
    return response

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def sample_cookie2(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return HttpResponse('test cookies! work or not work')


def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        product = Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()

    return render(request, 'shop/index.html')