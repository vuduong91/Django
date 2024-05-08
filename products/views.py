from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductDetail, Order, OrderDetail, User,Shipping,Category
from .form import LoginForm, OrderForm
from django.db.models import F


# Create your views here.
# -------------------------------- home website
def index(request):
 cates = Category.objects.all()
 productdetails = ProductDetail.objects.all()
 products = Product.objects.all()
 context = {
     "cates":cates,
     "productdetails": productdetails,
            "products": products}
 return render(request, 'product/index.html', context)
# -------------------------------- product site
def product(request):
 productdetails = ProductDetail.objects.all()
 products = Product.objects.all()
 context = {"productdetails": productdetails,
            "products": products}
 return render(request, 'product/product.html', context)
# --------------------------------- product+cate
def product_cate(request,id):
    cates = get_object_or_404(Category, id=id)
    productdetails = ProductDetail.objects.all()
    products = Product.objects.all()
    context = {"cates": cates,
        "productdetails": productdetails,
               "products": products}
    return render(request, 'product/product_cate.html', context)
# --------------------------------- take the id product to come product detail
def product1(request,id):
    print(request.POST)
    productdetails = get_object_or_404(ProductDetail, id=id)
    if request.method == 'POST':
        return redirect('product1')
    context = {'productdetails': productdetails}
    return render(request, 'product/product_detail.html', context)

def order(request,id):
    orders = get_object_or_404(OrderDetail, id=id)
    productdetails = get_object_or_404(ProductDetail,id=id)
    context = {"productdetails": productdetails,
                "orders":orders}
    return render(request,'product/order.html',context)

def update_order(request, id):
    orders = OrderDetail.objects.all().annotate(total_price=F('cost')*F('quanity'))
    for t in orders:
        print(t.total_price)
    context = {}
    orders = get_object_or_404(OrderDetail,id=id)
    form = OrderForm(request.POST or None, instance=orders)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,'product/update.html',{'form':form})

def orderdetail(request,id):
    shippings = Shipping.objects.all()
    users = get_object_or_404(User,id=id)
    order = get_object_or_404(Order,id=id)
    orders = get_object_or_404(OrderDetail, id=id)
    context = {"shippings":shippings,
                "users":users,
                "order":order,
               "orders": orders}
    if request.method == "POST":
        sum = request.POST.get('sum',None)
        customer = request.POST.get('customer',None)
        dateorder = request.POST.get('dateorder',None)
        shipping = request.POST.get('shipping',None)
        if sum is not None and customer is not None and dateorder is not None and shipping:
            data = OrderDetail(sum=sum, customer=customer, dateorder=dateorder, shipping=shipping)
            data.save()
            return render(request, 'product/order_detail.html', context)
        else:
            messages.error(request, f'Invalid data')
        pass
    else:
        return render(request,'product/order_detail.html',context)

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'product/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('index')
        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'product/login.html', {'form': form})
