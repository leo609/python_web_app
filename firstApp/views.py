from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginCredential, Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    data_dict = dict()
    data_dict['persons'] = persons
    data_dict2 = dict()
    data_dict2['LoginCredential'] = LoginCredential
    return render(request, 'firstApp/index.html', data_dict,)
    #return HttpResponse('Hello World')
    

def about(request):
    return render(request, 'firstApp/about.html')

def coolWebsites(request):
    websites_list=[['Youtube', 'https://www.youtube.com/'],['repl', 'https://repl.it/~'],['elearning', 'https://elearning.ardentacademy.com/']]
    return render(request, 'firstApp/coolWebsites.html', {'websites_list': websites_list})

def get_usernames():
    usernames = dict()
    with open('User.txt') as file_in:
        for line in file_in:
            uname, pword = line.strip().split(',')
            usernames[uname] = pword
    return usernames

def login(request):
    username = request.POST.get('uname')
    password = request.POST.get('pword')
    logins= LoginCredential.objects.filter(username=username, password=password)
    if len(logins) == 1:
        return render(request, 'firstApp/login.html')
    return HttpResponse('Error')

def signup(request):
    return render(request, 'firstApp/signup.html')

def new_user(request):
    firstname = request.POST.get('FirstName')
    lastname = request.POST.get('LastName')
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    record = LoginCredential(firstName=firstname, lastName=lastname, username=username, password=password)
    record.save()
    return render(request, 'firstApp/new_user.html')

