from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def works(request):
    # Pass a range of numbers to the template
    image_range = range(1, 10)
    return render(request, 'myapp/works.html', {'image_range': image_range})

def contact(request):
    return render(request, 'myapp/contact.html')