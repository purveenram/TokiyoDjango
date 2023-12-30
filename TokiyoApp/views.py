from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import ListView
import datetime
import json
from .models import *
from .forms import *

def home(request):
    userId = request.session.get("userId")
    user = None
    if userId:
        user = CustomerDetail.objects.get(pk=userId)
    
    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'user': user,
    }
    return render(request, 'home.html', context)

def searchInput(request):
    if request.method == 'POST':
        search_term = request.POST.get('search')
        prods = ProductDetail.objects.filter(productName__icontains=search_term)
        products = [product for product in prods]

        userId = request.session.get("userId")
        user = None
        if userId:
            user = CustomerDetail.objects.get(pk=userId)

        product_names = ProductDetail.objects.values('id', 'productName')
        qs_json = json.dumps(list(product_names))
        searchContent = f"Result for '{search_term}'"
        context = {
        'qs_json': qs_json,
        'category': searchContent,
        'products': products,
        'user': user,
        }
        return render(request, 'category/category.html', context)
    else:
        return render(request, 'your_template.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('home')

def credentialCheck(request):
    if request.method == 'POST':
        buttonClick = request.POST.get('buttonClick')
        if buttonClick == 'loginButton':
            email = request.POST.get('userEmail')
            password = request.POST.get('userPass')
            user = authenticate(request, customerEmail=email, customerPassword=password)
            if user is not None:
                request.session["userId"] = user.id
                return redirect('home')
        elif buttonClick == 'signupButton':
            return redirect("addCustomer")
    return redirect('login')

# for navigation of form
def registrationCustomer(request):
    return render(request, "registrationCustomer.html")

def registrationAddress(request):
    userId = request.session.get("userId")
    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'userId':userId,
    }
    return render(request, "registrationAddress.html",context)

# for adding the details newly
def addCustomer(request):
    form = CustomerDetailsForm()
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['customerEmail']
            if CustomerDetail.objects.filter(customerEmail=email).exists():
                return render(request, 'login.html', {'error_message': 'This Email Id Already Exist !'})
            else:
                password = form.cleaned_data['customerPassword']
                form.save()
                user = authenticate( request, customerEmail=email, customerPassword=password)
                request.session["userId"] = user.id
                return render(request, 'registrationAddress.html', {"userId": user.id})
    return redirect('registrationCustomer')

def addAddress(request):
    form = CustomerAddressForm()
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return redirect('registrationAddress')

# for viewing the details from navbar
def customerProfile(request):
    userId = request.session.get("userId")
    customer = CustomerDetail.objects.get(pk=userId)
    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'customer': customer,
    }
    return render(request, 'profile.html', context)

def customerAddress(request):
    userId = request.session.get("userId")
    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    try:
        customer = CustomerAddressDetail.objects.get(customerId=userId)
        if customer:
            context = {
                'qs_json': qs_json,
                'customer': customer, 
                "customerId": userId,
            }
            return render(request, 'address.html', context)
    except:
        skip = "value"
        context = {
            'qs_json': qs_json,
            "customerId": userId,
            "forSkip": skip,
        }
        return render(request, 'registrationAddress.html', context)

# for updating the existing details
def updateProfile(request):
    if request.method == 'POST':
        userId = request.session.get("userId")
        if userId is not None:
            customer = CustomerDetail.objects.get(pk=userId)
            form = CustomerDetailsForm(request.POST, instance=customer)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return HttpResponseBadRequest("Form validation failed")
    return redirect('profile')

def updateAddress(request):
    if request.method == 'POST':
        userId = request.session.get("userId")
        if userId is not None:
            customer = CustomerAddressDetail.objects.get(customerId=userId)
            form = CustomerAddressForm(request.POST, instance=customer)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return HttpResponseBadRequest("Form validation failed")
    return redirect('address')

# for product and category pages
def viewCategory(request, category):
    category_mapping = {
        1: 'Katana',
        2: 'Action Figure',
        3: 'Accessories',
        4: 'Posters',
    }
    userId = request.session.get("userId")
    user = None
    if userId:
        user = CustomerDetail.objects.get(pk=userId)

    if category == 0:
        selected_category = 'All Products'
        products = ProductDetail.objects.all()
    else:
        selected_category = category_mapping.get(category, category_mapping[category])
        products = ProductDetail.objects.filter(productCategory=selected_category)
    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'category': selected_category,
        'products': products,
        'user': user,
    }
    return render(request, 'category/category.html', context)

def viewProduct(request, prod):
    productImages = ProductImage.objects.filter(product=prod)
    product = ProductDetail.objects.get(id=prod)
    products = ProductDetail.objects.filter(
        productCategory=product.productCategory)

    userId = request.session.get("userId")
    user = None
    if userId:
        user = CustomerDetail.objects.get(pk=userId)

    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'products': products,
        'productImages': productImages,
        'product': product,
        'user': user,
    }
    return render(request, 'category/productView.html', context)

def viewCart(request):
    userId = request.session.get("userId")
    orders = None
    try:
        orders = CartDetail.objects.filter(customerIdInCart=userId)
        totalPriceOfProducts = 0

        for item in orders:
            totalPriceOfProducts += item.productIdInCart.productSellingPrice * item.productQuantityInCart

        discountForTotalPrice = 10 * (totalPriceOfProducts/100)
        totalAmountToPay = totalPriceOfProducts-discountForTotalPrice
        
        request.session["totalPriceOfProducts"] = float(totalPriceOfProducts)
        request.session["discountForTotalPrice"] = float(discountForTotalPrice)
        request.session["totalAmountToPay"] = float(totalAmountToPay)
        product_names = ProductDetail.objects.values('id', 'productName')
        qs_json = json.dumps(list(product_names))

        context = {
            'qs_json': qs_json,
            'orders': orders,
            'totalPriceOfProducts': totalPriceOfProducts,
            'discountForTotalPrice': discountForTotalPrice,
            'totalAmountToPay': totalAmountToPay,
        }
        return render(request, 'cart.html', context)
    except:
        product_names = ProductDetail.objects.values('id', 'productName')
        qs_json = json.dumps(list(product_names))

        context = {
        'qs_json': qs_json,
        'orders': orders,
        }

        return render(request, 'cart.html', context)

def removeInCart(request, productId):
    item = get_object_or_404(CartDetail, id=productId)
    item.delete()
    return redirect('cart')

def addInCart(request, prod):
    if request.method == 'POST':
        buttonClick = request.POST.get('buttonAdd')
        if buttonClick == 'addCart':
            form = CartDeatilsForm(request.POST)
            if form.is_valid():
                addingInCart(request,form)
                return redirect('product', prod=prod)
            else:
                return redirect('login')
        elif buttonClick == 'addBuy':
            form = CartDeatilsForm(request.POST)
            if form.is_valid():
                addingInCart(request,form)
                return redirect('cart')
            else:
                return redirect('login')
        
def addingInCart(request,form):
    product_id = form.cleaned_data['productIdInCart']
    quantity = form.cleaned_data['productQuantityInCart']
    product = ProductDetail.objects.get(id=product_id.id)
    product_price = product.productSellingPrice  
    total_price = product_price * quantity
    existing_item = CartDetail.objects.filter(customerIdInCart=request.session.get("userId"), productIdInCart=product_id).first()
    if existing_item:
        existing_item.productQuantityInCart += quantity
        existing_item.productPrizingInCart += total_price
        existing_item.save()
    else:
        cart_item = form.save(commit=False)
        cart_item.productPrizingInCart = total_price
        cart_item.save()

def makePayment(request):
    userId = request.session.get("userId")

    ordersInCart = CartDetail.objects.filter(customerIdInCart=userId)

    if ordersInCart:

        # tokiyoOrderId
        lastTokiyoOrderId = OrderDetail.objects.last()
        tokiyoOrderId = lastTokiyoOrderId.tokiyoOrderId if lastTokiyoOrderId else 963000000
        tokiyoOrderId = tokiyoOrderId+1

        try:
            userAddress = CustomerAddressDetail.objects.get(customerId=userId)
            # deliverAddressInOrder
            userAddress = CustomerAddressDetail.objects.get(customerId=userId)
            deliverAddressInOrder = f"{ userAddress.cutomerHouseNo }, { userAddress.cutomerAddressLine1 }, { userAddress.cutomerAddressLine2 }, { userAddress.customerCity }, { userAddress.customerState }-{ userAddress.customerPinCode }"
    
            # deliveryNumberInOrder
            deliveryNumberInOrder = userAddress.customerDeliveryNumber
        except:
            return redirect('addAddress')

        # totalItemCostInOrder
        totalItemCostInOrder = request.session.get("totalPriceOfProducts")

        # discountInOrder
        discountInOrder = request.session.get("discountForTotalPrice")

        # totalAmountPaidInOrder
        totalAmountPaidInOrder = request.session.get("totalAmountToPay")

        # orderPlacedTimeDate
        orderPlacedTimeDate = datetime.datetime.today().strftime("%B %d, %Y, @%H:%M:%S")

        # orderPlacedDate
        orderPlacedDate = datetime.date.today()

        # orderDeliveredDate
        orderDeliveredDate = orderPlacedDate + datetime.timedelta(days=7)

        form_data = {
            'customerIdInOrder': userId,
            'tokiyoOrderId': tokiyoOrderId,
            'deliverAddressInOrder': deliverAddressInOrder,
            'deliveryNumberInOrder': deliveryNumberInOrder,
            'totalItemCostInOrder': totalItemCostInOrder,
            'discountInOrder': discountInOrder,
            'totalAmountPaidInOrder': totalAmountPaidInOrder,
            'orderPlacedTimeDate':orderPlacedTimeDate,
            'orderPlacedDate': orderPlacedDate,
            'orderDeliveredDate': orderDeliveredDate,
            'orderStatusInOrder': 'N',
        }

        form = OrderDeatilsForm(form_data)
        form.save()
        orderDetailSId = OrderDetail.objects.get(tokiyoOrderId=tokiyoOrderId)

        for item in ordersInCart:
            form_data = {
                'customerIdInODP':userId,
                'orderDetailSId': orderDetailSId.id,
                'productIdInODP': item.productIdInCart,
                'productQuantityInODP': item.productQuantityInCart,
                'productPrizingInODP': item.productPrizingInCart,
            }
            form = OrderDetailsProductsForm(form_data)
            form.save()
            item.delete()

    return redirect('viewOrders')

def viewOrders(request):
    userId = request.session.get("userId")
    try:
        ordersList = OrderDetail.objects.filter(customerIdInOrder=userId)
        for order in ordersList:
            if order.orderDeliveredDate < datetime.date.today():
                order.orderStatusInOrder = "Y"
                order.save()
        orderProductsList = OrderDetailsProduct.objects.filter(customerIdInODP=userId)
    except:
        ordersList = None
        orderProductsList = None

    product_names = ProductDetail.objects.values('id', 'productName')
    qs_json = json.dumps(list(product_names))

    context = {
        'qs_json': qs_json,
        'ordersList': ordersList,
        'orderProductsList': orderProductsList,
    }
    return render(request, 'order.html',context)

def removeInOrder(request, orderId):
    order = OrderDetail.objects.get(id=orderId)
    order.orderStatusInOrder = 'C'
    order.save()
    return redirect('viewOrders')
