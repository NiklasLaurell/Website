from django.shortcuts import render
from modules.calender_functions import get_time, get_first_date, get_matrix

# Create your views here.


def index(request):
    action = None
    try:
        QueryDict = request.POST
        queryDict = dict(QueryDict)
        if "direction" in queryDict:
            action = queryDict["direction"][0]
            action = action.split()
            print(action)
    except Exception:
        print(Exception, "WTF")

    time = get_time()

    first_date = get_first_date(time, 6, 7, action)
    a, b, c = first_date
    first_date_str = f"{a} {b} {c}"
    today = (time.year, time.month, time.day)
    matrix = get_matrix(6, 7, first_date)
    days = ['Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag', 'Söndag']
    print(first_date, "firstdate")
    return render(request, 'Test_app/index.html', {
        'days': days,
        'matrix': matrix,
        'time': time,
        'today': today,
        'first_date_str': first_date_str
    })
