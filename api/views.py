from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import custom,sell,admin,image_upload
import math
import re
import os
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')         
def home(request):
    images = image_upload.objects.all()
    image_data = [{'image_url': im.image.url, 'image_id': im.id} for im in images]
    context = {'image_data_list': image_data}
    return render(request, 'card.html', context)


def login(request):
    # if 'email' in request.session:
    #     return redirect('profile')
    # else:
    #     return redirect('login')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))
        if lat and lon is not None:
            request.session["user_lat"] = lat
            request.session["user_lon"] = lon
            print('login lat lon',lat,lon)

        all_data = custom.objects.all()

        
        
        if not email:
            return HttpResponse("Please enter your email address")
        elif not password:
            return HttpResponse("Please enter your password")
        
        # with open('data.json', 'r') as outfile:
        #     data = json.load(outfile)
        
        # match = True
        for obj in all_data:
            if email==obj.email and password==obj.password:
                request.session['email'] = email
                request.session['login_type'] = "custom"
                obj.active = True
                obj.save()
                return redirect('profile')
                
        
        # if not match:
        #     else:
        #         return HttpResponse("Login failed")
        #         return redirect('login')
    
    return render(request, 'login.html')


def sell_login(request):
    # if 'email' in request.session:
    #     return redirect('profile')
    # else:
    #     return redirect('login')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
 
        
        # if not email:
        #     return HttpResponse("Please enter your email address")
        # elif not password:
        #     return HttpResponse("Please enter your password")
        
        # with open('sell.json', 'r') as outfile:
        #     data = json.load(outfile)
        data = sell.objects.all()
        
        # match = True
        for obj in data:
            if email==obj.email and password==obj.password:
                request.session['email'] = email
                request.session['login_type'] = "sell"
                obj.active = True
                obj.save()
                # obj["latitude"] = latitude
                # obj["longitude"] = longitude
                # request.session["latitude"] = obj["latitude"]
                # request.session["longitude"] = obj["longitude"]

                # print(request.session['email'])
                return redirect('sellprofile')
        return HttpResponse("Login failed")
    
    return render(request, 'login.html')


def admin_login(request):
        username = ""
        password = ""
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')

        all_data = admin.objects.all()

        
        
        # if not username:
        #     return HttpResponse("Please enter your email address")
        # elif not password:
        #     return HttpResponse("Please enter your password")
        
        for obj in all_data:
            if username==obj.username and password==obj.password:
                request.session['username'] = username
                request.session['login_type'] = "admin"
                return redirect("admin_page")     
                
                
        
        # if not match:
        #     else:
        #         return HttpResponse("Login failed")
        #         return redirect('login')
    
        return render(request, 'login.html')


def admin_page(request):
    return render(request, "admin_page.html")


def upload_image(request):
    uploaded_files = {}

    if request.method == 'POST':
        for i in range(1, 7):  # Assuming 6 file input fields (file1 to file6)
            uploaded_file = request.FILES.get(f'file{i}')
            if uploaded_file:
                new_image = image_upload(image=uploaded_file)
                new_image.save()
        uploaded_files = []
        image = image_upload.objects.all()
        for i in image:
            uploaded_files.append(i)

        # return render(request, "card.html", {'uploaded_files': uploaded_files})

    return render(request, "upload_image.html")


def user_info(request):
    data = custom.objects.all()
    return render(request,"user_info.html", {"user_info":data})


    





def validate_password(password):
    # Check if the password has a minimum length of 4 characters
    if len(password) < 4:
        return False
    
    # Check if the password contains at least one letter and one number
    has_letter = re.search(r'[a-zA-Z]', password)
    has_number = re.search(r'\d', password)
    
    if not (has_letter and has_number):
        return False
    
    return True




def signup(request):
    check = False
    if request.method == 'POST':
        uname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        bday = request.POST.get('bday')
        occ = request.POST.get('Occupation')
        
        all = custom.objects.all()
        for i in all:
            if i.email == email:
                exist_email_message = 'This email already exists.'
                return render(request, 'signup.html', {'exist_email_message': exist_email_message})

       
        
        if not validate_password(password):
            check = True
            pass_error = 'Password must be at least 4 characters long and contain a mix of letters and numbers.'
            return render(request, 'signup.html', {'pass_error': pass_error})
        

        if uname == "":
            check = True
            name_error = 'Please enter your username.'
            return render(request, 'signup.html', {'name_error': name_error})
        if email == "" :
             check = True
             error_message = 'Please enter your email.'
             return render(request, 'signup.html', {'error_message': error_message})
        
      
        if check == False:
            user = custom(
                name=uname,
                email=email,
                password=password,
                address=address,
                mobile=mobile,
                birthday=bday,
                occupation=occ,
                active=False  
            )
            user.save()
            set_user = User.objects.create_user(username=uname, email = email, password=password)
            # set_user.set_password(password)
            set_user.save()
        
        return redirect('payform')
    
    return render(request, 'signup.html')


def adminsign(request):
    if request.method == 'POST' :
        username = request.POST.get('email')
        password = request.POST.get('password')

        
        all_data = admin.objects.all()
        for user in all_data:
            if user.username == username:
                exist_email_message = 'This email already exists.'
                return render(request, 'signup.html', {'exist_email_message': exist_email_message})

       
        if username == "" :
             error_message = 'Please enter your email.'
             return render(request, 'signup.html', {'error_message': error_message})
        
        user = admin(
                username=username,
                password=password, 
            )
        user.save()
        
        
        # with open("sell.json", "w") as file:
        #     json.dump(data, file, indent=4) 
        
        return redirect('login')
        
        
    
    return render(request, 'login.html')



def signup_sell(request):
    data=[]

    if request.method == 'POST' :
        uname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        bday = request.POST.get('bday')
        occ = request.POST.get('Occupation')

        
        # try:
        #     with open('sell.json', 'r') as file:
        #         data = json.load(file)
        # except json.JSONDecodeError as e:
        #     print("Error decoding JSON:", e)
        # except FileNotFoundError:
        #     print("File not found or path is incorrect.")
        # except Exception as e:
        #     print("Error:", e)
        all_data = sell.objects.all()
        for user in all_data:
            if user.email == email:
                exist_email_message = 'This email already exists.'
                return render(request, 'signup.html', {'exist_email_message': exist_email_message})
        
        if not validate_password(password):
            pass_error = 'Password must be at least 4 characters long and contain a mix of letters and numbers.'
            return render(request, 'signup.html', {'pass_error': pass_error})
        if uname == "":
            name_error = 'Please enter your username.'
            return render(request, 'signup.html', {'name_error': name_error})
        if email == "" :
             error_message = 'Please enter your email.'
             return render(request, 'signup.html', {'error_message': error_message})
        
        # dic = {
        #     "name": uname,
        #     "email": email,
        #     "password": password,
        #     "address": address,
        #     "mobile": mobile,
        #     "birthday": bday,
        #     "occupation": occ,
        #     "active":False,

        # }
        
        # data.append(dic)
        user = sell(
                name=uname,
                email=email,
                password=password,
                address=address,
                mobile=mobile,
                birthday=bday,
                occupation=occ,
                active=False  
            )
        user.save()
        
        
        # with open("sell.json", "w") as file:
        #     json.dump(data, file, indent=4) 
        
        return redirect('login')
        
        
    
    return render(request, 'signup.html')



def profile(request):
   email = request.session.get('email')
   if email:
        # with open('data.json', 'r') as file:
        #     data = json.load(file)
        
        data = custom.objects.all()
        user_data = None
        
        for obj in data:
            if obj.email== email:
                user_data = obj
                break

        if user_data is None:
            return HttpResponse("User data not found")

        context = {
            'data': user_data,
            'login_type': 'custom',
        }
    
        return render(request, 'profile.html', context)
   else:
        return redirect('login')
    
    
def sell_profile(request):
   email = request.session.get('email')
   if email:
        data = sell.objects.all()
        # with open('sell.json', 'r') as file:
        #     data = json.load(file)

        user_data = None
        
        for obj in data:
            if obj.email == email:
                user_data = obj
                break

        if user_data is None:
            return HttpResponse("User data not found")

        context = {
            'data': user_data,
            'login_type': 'sell',
        }
    
        return render(request, 'profile.html', context)
   else:
        return redirect('login')
   

def edit_profile(request):
    email = request.session.get('email')
    login_type = request.session.get('login_type')
    if login_type == "custom":
        model = custom
    if login_type == "sell":
        model = sell
    data = model.objects.all() 
    if email:
        user_data = None
        for obj in data:
            if obj.email == email:
                user_data = obj
        if user_data is None:
            return HttpResponse("User data not found")
        
        context = {
            'data': user_data,
            'login_type': login_type
        }
        

        
    # else:
    #     return redirect('login')
    
        if request.method == 'POST':
            uname = request.POST.get('fname')
            password = request.POST.get('password')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            bday = request.POST.get('bday')
            occ = request.POST.get('Occupation')
            # for obj in data:
            #     if obj.email == email:
                    # sell.objects.filter(email).update(name = uname, password=password, address = address, mobile = mobile, birthday = bday, occupation = occ)
            user_data.name = uname
            user_data.password = password
            user_data.address = address
            user_data.mobile = mobile
            user_data.occupation = occ
            try:
                user_data.birthday = datetime.strptime(bday, '%Y-%m-%d').date()
            except ValueError:
                # Handle the case where 'bday' is not in the correct format
                return HttpResponse("Invalid date format")
            user_data.save()
        return render(request, 'edit.html', context)
    else: 
        return HttpResponse("Email not found in session")
        
        

    
        
    
    
    
def logout(request):
    email = request.session.get('email')

    if email:
        # with open('data.json', 'r') as file:
        #     data = json.load(file)
        data =  custom.objects.all() or sell.objects.all()
        for obj in data:
            if obj.email == email:
                obj.active = False
                obj.save()  # Set active flag to False for the logged-out user
                break
        del request.session['email']  # Assuming 'email' is the key for the session variable storing the user's email
    return redirect('home')


def payform(request):
    return render(request, 'payform.html')

def search_bar(request):
    return render(request, 'search_bar.html')


def search_result(request):

    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        results = calculate_distance_and_filter(latitude, longitude)

        return JsonResponse({'results': results})

    return render(request, 'search_results.html')



def calculate_distance_between_points(lat1, lon1, lat2, lon2):
    # Use the haversine formula to calculate the distance between two points
    # You can modify this calculation as per your needs
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(
        dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


# def test(request):
#     lat = request.session.get('latitude')
#     lon = request.session.get('longitude')
#     email = request.session.get('email')
#     content = {}
#     if email:
#         if request.method == "POST":
#             latitude = request.POST.get("latitude")
#             longitude = request.POST.get("longitude")
#             occ = request.POST.get('occupation')
#             match_profile = {}
    
#             # with open('sell.json', 'r') as outfile:
#             #     data = json.load(outfile)
#             data = sell.objects.all()
#             for obj in data:
#                 print(obj.occupation)
#                 print(occ)
#                 if occ == obj.occupation:
#                     if lat and lon:
#                         print(lat,lon)
#                         distance = calculate_distance_between_points(latitude,longitude,lat,lon)
#                         print(distance)
#                         if (distance <=3 or distance <=10 or distance <=15) and (email != email):
#                             if obj.email==email:
#                                 em = obj.email
#                                 phn = obj.mobile
#                                 occu = obj.occupation
#                                 match_profile["em"] = em
#                                 match_profile["phn"] = phn
#                                 match_profile["occu"] = occu
#                                 print("match",match_profile)
#                     if match_profile is not None:
                

#                         content = {
#                         "data":match_profile
#                         }
#                     else:
#                         return HttpResponse("no user is here")
            
#         return render(request,'test.html',content)
#     return HttpResponse("no user is here")

def test(request):
    lat = float(request.session.get('latitude'))
    lon = float(request.session.get('longitude'))
    email = request.session.get('email')
    content = {}
    
    if email:
        if request.method == "POST":
            latitude = float(request.session.get('user_lat'))
            longitude = float(request.session.get('user_lon'))
            print("first",latitude,longitude)
            print(type(latitude), type(longitude), type(lat), type(lon))
            occ = request.POST.get('occupation')
            match_profiles = []
            
            data = sell.objects.all()  # Assuming your model name is Sell
            
            for obj in data:
                if occ == obj.occupation:
                    if lat and lon and latitude and longitude is not None:
                        distance = calculate_distance_between_points(latitude, longitude, lat, lon)
                        if distance <= 3:
                            match_profile = {
                                "em": obj.email,
                                "phn": obj.mobile,
                                "occu": obj.occupation
                            }
                            match_profiles.append(match_profile)
                    else:
                        print("One or more coordinates are missing.")
                        print(latitude, longitude, lat, lon)
            
            if match_profiles:
                content = {"data": match_profiles}
            else:
                return HttpResponse("No matching users found.")
            
        return render(request, 'test.html', content)
    
    return HttpResponse("No user is here.")
    

    
def test2(request):
    email = request.session.get('email')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    request.session['latitude'] = latitude
    request.session['longitude'] = longitude
    request.session['em'] = email
    print(latitude,longitude)
    # context = {
    #     "latitude":latitude,
    #     "longitude":longitude

    # }
    

    return render(request,'test2.html')

def api(request):
    if request.method=='post':
        occ = request.POST.get('search')
        with open('sell.json') as file:
            data = json.load(file)
            cse_data = [item for item in data if item['occupation'] == occ]
            context={'data':cse_data}
            return render(request,'test2.html',context)
        
        
    
    

def calculate_distance_and_filter(user_latitude, user_longitude):
    with open('data.json', 'r') as file:
        users = json.load(file)

    matched_users = []
    user_location = (float(user_latitude) if user_latitude else 0.0, float(user_longitude) if user_longitude else 0.0)

    for user in users:
        if user['active']:
            occupation = user['occupation'].lower()
            profile_latitude = float(user.get('latitude', 0))
            profile_longitude = float(user.get('longitude', 0))
            distance = calculate_distance_between_points(user_location[0], user_location[1], profile_latitude, profile_longitude)

            if distance <= 3:
                user['distance'] = distance
                matched_users.append(user)

    if len(matched_users) == 0:
        return [{'message': 'No matches found.'}]
    
    return matched_users

