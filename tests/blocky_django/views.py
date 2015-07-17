from blocky.django.shortcuts import render_template


def home(request):
    return render_template(request, 'child.html', {'content': '.content'})
