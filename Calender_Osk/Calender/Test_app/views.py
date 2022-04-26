from django.shortcuts import render


# Create your views here.


def index(request):
    Test_app = [
        {'title': "Tester"},
        {'title': "kukTester"}
    ]
    return render(request, 'Test_app/index.html', {
        'show_Test_app': False,
        'Test_app': Test_app
    })
