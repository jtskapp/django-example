from django.shortcuts import render

# Create your views here.
def index(request):
    context_data = {'text': 'hello world, this is a test template filtering', 'number': 100, 'range': range(1,11)}
    return render(request,'basicapp/index.html', context = context_data)


def about(request):
    return render(request,'basicapp/about.html')


def other(request):
    return render(request,'basicapp/other.html')
