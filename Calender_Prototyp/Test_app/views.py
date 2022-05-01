from django.shortcuts import render
from modules.calender_functions import get_matrix, get_time

# Create your views here.


def index(request):
    print(request)
    time = get_time()
    today = (time.year, time.month, time.day)
    matrix = get_matrix(time, 6, 7)

    days = ['Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag', 'Söndag']
    return render(request, 'Test_app/index.html', {
        'days': days,
        'matrix': matrix,
        'time': time,
        'today': today
    })


def index2(request):
    if request.method == 'POST':
        print("hej")

<<<<<<< HEAD

=======
>>>>>>> 8dce2123d4c33a05408240065738db4b6b137667
    time = get_time()

    today = (time.year, time.month, time.day)

    matrix = get_matrix(time, 8, 7)

    days = ['Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag', 'Söndag']
    return render(request, 'Test_app/index.html', {
        'days': days,
        'matrix': matrix,
        'time': time,
        'today': today
    })
