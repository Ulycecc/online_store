import datetime

from django.shortcuts import render, get_object_or_404
from .models import Product, Сonsumer, Order, ProductImage
from .form import ProductForms, ImageForm
from django.core.files.storage import FileSystemStorage

...


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form': form})


def product_week(request, consumer_id):
    consumer = get_object_or_404(Сonsumer, pk=consumer_id)
    orders = Order.objects.filter(consumer=consumer).order_by(
        '-date').filter(date__gte=datetime.datetime.today() - datetime.timedelta(days=7))
    return render(request, 'myapp/product_week.html', {'consumer':
                                                       consumer, 'orders': orders, 'days': 7})


def product_month(request, consumer_id):
    consumer = get_object_or_404(Сonsumer, pk=consumer_id)
    orders = Order.objects.filter(consumer=consumer).order_by(
        '-date').filter(date__gte=datetime.datetime.today() - datetime.timedelta(days=30))
    return render(request, 'myapp/product_week.html', {'consumer':
                                                       consumer, 'orders': orders, 'days': 30})


def product_year(request, consumer_id):
    consumer = get_object_or_404(Сonsumer, pk=consumer_id)
    orders = Order.objects.filter(consumer=consumer).order_by(
        '-date').filter(date__gte=datetime.datetime.today() - datetime.timedelta(days=365))
    return render(request, 'myapp/product_week.html', {'consumer':
                                                       consumer, 'orders': orders, 'days': 365})


def upload_image_base(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            product_image = ProductImage(product=product, image=image)
            product_image.save()
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form': form})


def post_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date = form.cleaned_data['date']
            product = Product(
                name=name, description=description, price=price, quantity=quantity, date=date)
            product.save()
            return render(request, 'myapp/postproduct.html', {'answer': 'Продукт добавлен'})

    else:
        form = ProductForms()
    return render(request, 'myapp/postproduct.html', {'form': form})
