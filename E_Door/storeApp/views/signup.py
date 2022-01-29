from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from storeApp.models.customers import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile_no = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')

        #validate
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'mobile_no':mobile_no,
            'email':email
        }

        error_message = None

        customer = Customer(first_name=first_name,last_name=last_name,mobile_no=mobile_no,email=email,password=password)
        #using the validateCustomer to validate the user
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name,last_name,mobile_no,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error': error_message,
                'values': value
            }
            return render(request,'signup.html',data)

    def validateCustomer(self,customer):
        error_message =None
        if(not customer.first_name):
            error_message =" Please enter your First Name"
        elif len(customer.first_name) <3:
            error_message="First Name must be equal to or more than 3 characters"
        elif(not customer.last_name):
            error_message = "Please enter your last name"
        elif len(customer.last_name) < 3:
            error_message= "Last Name must be equal to or more than 3 characters"
        elif not customer.mobile_no:
            error_message="Enter you mobile number"
        elif len(customer.mobile_no) <10 or len(customer.mobile_no) > 10:
            error_message="Mobile number must be of 10 digits."
        elif len(customer.password) < 5:
            error_message = "Password must be of 5 characters"
        elif len(customer.email)<5:
            error_message = "Email should must contain 5 character"
        elif customer.isExists():
            error_message="Email already registered once"
        
        #saving

        return error_message