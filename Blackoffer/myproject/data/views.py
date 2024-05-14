from django.shortcuts import render
from .models import Yourdata
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    datas = Yourdata.objects.all()
    print("===>", datas)
    return render(request, "index.html", {"datas":datas})

def json_add_data(request):
    import os
    from datetime import datetime
    json_file_path = './jsondata.json'
    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_directory, 'jsondata.json')
    print("===>", json_file_path)
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            # Iterate through the JSON data and save it to the database
            for item in data:
                Yourdata.objects.create(
                    end_year=item['end_year'],
                    intensity=item['intensity'],
                    sector=item['sector'],
                    topic=item['topic'],
                    insight=item['insight'],
                    url=item['url'],
                    region=item['region'],
                    start_year=item['start_year'],
                    impact=item['impact'],
                    added=datetime.strptime(item['added'], "%B, %d %Y %H:%M:%S") if item['added'] else None,
                    published=datetime.strptime(item['published'], "%B, %d %Y %H:%M:%S") if item['published'] else None,
                    country=item['country'],
                    relevance=item['relevance'],
                    pestle=item['pestle'],
                    source=item['source'],
                    title=item['title'],
                    likelihood=item['likelihood'],
                    # Add other fields as needed
                )
                
        message = 'Data saved successfully.'
        
    except FileNotFoundError:
        message = 'JSON file not found.'
        
    except json.JSONDecodeError:
        message = 'Error decoding JSON data.'
    return HttpResponse(message)

def set(request):
    from django.db.models import Sum, Count, Avg
    queryset = Yourdata.objects.all().aggregate(Sum("intensity", default=0), Sum("likelihood", default=0), Sum("relevance", default=0))
    total = queryset['intensity__sum'] + queryset['likelihood__sum'] + queryset['relevance__sum'] 
    print("===>", total)
    intensity_perc = queryset['intensity__sum']*100 / total
    print("===>", intensity_perc)
    likelihood_perc = queryset['likelihood__sum']*100 / total
    print("===>", likelihood_perc)
    relevance_perc = queryset['relevance__sum']*100 / total
    print("===>", relevance_perc)
    print("===>", queryset)
    return render(request, "visualize.html",{"intensity":intensity_perc ,"likelihood":likelihood_perc ,"relevance":relevance_perc})


#def sat(request):
#    return render(request, "login.html")
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
def login_data(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        try:
            data = request.POST.get
            user = User.objects.get(username=data("username"))
            
            if not user:
                messages.success(request, "You don't have permission", extra_tags='alert')
                return redirect("login_data")
            else:
                 user = authenticate(username=user.username, password=data("password"))
                 return redirect("home")
                 
        except Exception as exe:
            messages.warning(request, "You don't have permission", extra_tags='alert')
            return redirect("login_data")
        
from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect("login_data")

# def signup(request):
#     return render(request, "signup.html")

def signup(request):
    if request.method == 'POST':
        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        EmailId = request.POST.get('emailid')
        print("--->", EmailId)
        # Username = request.POST.get('Username')
        Phone_number = request.POST.get('phone_number')
        Password = request.POST.get('password')

        # Check if user with the given email already exists
        if User.objects.filter(email=EmailId).exists():
            # Handle the case where the user already exists (e.g., show an error message)
            return render(request,  {'error_message': 'User with this email already exists'})

        user = User.objects.create_user(first_name=Firstname, last_name=Lastname, email=EmailId, username=EmailId, password=Password)
        print("===>", user)
        # No need to call user.save() after create_user, as create_user does that internally

        # Redirect to the home page or any other page after successful user creation
        return redirect('login_data')
    else:
        # Handle the case where the request method is not POST (e.g., display the registration form)
        return render(request, 'signup.html')
    
    
def index(request):
    from django.db.models import Sum, Count, Avg
    queryset = Yourdata.objects.all().aggregate(Sum("intensity", default=0), Sum("likelihood", default=0), Sum("relevance", default=0))
    total = queryset['intensity__sum'] + queryset['likelihood__sum'] + queryset['relevance__sum'] 
    print("===>", total)
    intensity_perc = queryset['intensity__sum']*100 / total
    print("===>", intensity_perc)
    likelihood_perc = queryset['likelihood__sum']*100 / total
    print("===>", likelihood_perc)
    relevance_perc = queryset['relevance__sum']*100 / total
    print("===>", relevance_perc)
    print("===>", queryset)
    datas = Yourdata.objects.all()
    return render(request, "visualization.html",{"intensity":intensity_perc ,"likelihood":likelihood_perc ,"relevance":relevance_perc,"datas": datas})

def chart(request): 
    return render(request, "chart.html")
    


