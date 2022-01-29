from django.shortcuts import render,redirect
from django.views import View
from E_Door.storeApp.models.customers import Customer

from E_Door.storeApp.models.products import Products
from E_Door.storeApp.models.orders import Order




class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        mobile_no = request.POST.get('mobile_no')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_product_by_id(list(cart.key()))
        print(address,mobile_no,customer,cart,products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer))
