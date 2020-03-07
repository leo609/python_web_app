from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from myApp')
    my_list=['video games','chess', 'swim', 'piano', 'python']
    student_list = []
    student_list.append(['Carson', '13', 'python', '100%', '50%', '50%'])
    student_list.append(['Chandon', '12', 'python', '75%', '60%', '50%'])
    student_list.append(['Aaron', '7', 'python', '10%', '10%', '10%'])
    return render(request, 'myApp/index.html', {'students':student_list})

def sign_up(request):
    return render(request, 'myApp/sign-up.html')

def info(request):
    return render(request, 'myApp/info.html')
    
def submit(request):
    return render(request, 'myApp/submit.html')