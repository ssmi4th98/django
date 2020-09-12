from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "mynewapp/home.html",
                  {'h1Text': 'MessageBox',
                   'pText': 'Welcome to the MessageBox App! Click to log in.'
    })

def about(request):
    return render(request, "mynewapp/about.html",
                  {'message': 'We are about it all.'
    })


#the values h1Text and pText are passed in a key pair values (dictionary values).