from django.shortcuts import render


# Create your views here.


def index(request):
    Test_app = [[i for i in range(7)] for _ in range(4)]
    days = ['Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag', 'Söndag']
    return render(request, 'Test_app/index.html', {
        'show_Test_app': True,
        'Test_app': Test_app,
        'days': days
    })
