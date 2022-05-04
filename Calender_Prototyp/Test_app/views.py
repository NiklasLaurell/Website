from django.shortcuts import render
from calenderkod.calender_matrix import get_time, DisplaySettings, CalenderMatrix
# Create your views here.

# from modules.calender_functions import get_time, get_first_date, get_matrix
#
#
# month_number_to_name = {1: "January",
#                         2: "February",
#                         3: "March",
#                         4: "April",
#                         5: "May",
#                         6: "June",
#                         7: "July",
#                         8: "August",
#                         9: "September",
#                         10: "October",
#                         11: "November",
#                         12: "December",
#                         }
#
#
# def index2(request):
#     action = None
#     QueryDict = request.POST
#     print(QueryDict)
#     queryDict = dict(QueryDict)
#     print(queryDict)
#     if "direction" in queryDict:
#         action = queryDict["direction"][0]
#         action = action.split()
#         print(action)
#
#     time = get_time()  # today
#
#     first_date = get_first_date(time, 6, 7, action)
#     y, m, d = first_date
#     first_date_str = f"{y} {m} {d}"
#     today = (time.year, time.month, time.day)
#     matrix = get_matrix(6, 7, first_date)
#     days = ['Måndag', 'Tisdag', 'Onsdag',
#             'Torsdag', 'Fredag', 'Lördag', 'Söndag']
#     main_month = time.month
#     month_and_year = f"{month_number_to_name[main_month]} {time.year}"
#     print(first_date, "firstdate")
#     return render(request, 'Test_app/index.html', {
#         'days': days,
#         'matrix': matrix,
#         'time': time,
#         'today': today,
#         'first_date_str': first_date_str,
#         'month_and_year': month_and_year
#     })


def index(request):
    action = None
    QueryDict = request.POST
    print(QueryDict)
    queryDict = dict(QueryDict)
    print(queryDict)
    if "direction" in queryDict:
        action = queryDict["direction"][0]
        action = action.split()
        print(action)

    time = get_time()  # today
    today = (time.year, time.month, time.day)
    main_month = time.month

    settings = DisplaySettings()
    c = CalenderMatrix(settings)

    iterable = c.matrix_generater

    y, m, d = c.calender[0]
    first_date_str = f"{y} {m} {d}"

    month_and_year = f"{c.get_month_name(main_month)} {time.year}"
    print(c)
    html_variables = {'calender': c.calender,
                      'iterable': iterable,
                      'time': time,
                      'today': today,
                      'first_date_str': first_date_str,
                      'month_and_year': month_and_year}

    return render(request, 'Test_app/index2.html', html_variables)
