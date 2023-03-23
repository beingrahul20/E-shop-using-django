from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.product import Category
from .models.customer import Customer


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        lastname = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, lastname, phone, email, password)
        customer = Customer(first_name=first_name,
                            lastname=lastname,
                            phone=phone,
                            email=email,
                            password=password)
        customer.register()
        return HttpResponse("Signup SUccess")
