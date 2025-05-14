from django.shortcuts import render

def home(request):
    show_image = False
    if request.method == 'POST':
        show_image = True
    return render(request, 'main/home.html', {'show_image': show_image})