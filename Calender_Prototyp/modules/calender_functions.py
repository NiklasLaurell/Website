import calendar
from datetime import datetime


def get_time():
    return datetime.now()


def previus_date(current_date: tuple) -> tuple:
    year, month, date = current_date
    if date == 1:  # If first day of month
        if month == 1:  # If first day of the year
            date = calendar.monthrange(year - 1, 12)[1]
            return (year - 1, 12, date)
        date = calendar.monthrange(year, month - 1)[1]
        return (year, month - 1, date)
    return (year, month, date - 1)


def next_date(current_date: tuple) -> tuple:
    year, month, date = current_date
    days_in_month = calendar.monthrange(year, month)[1]
    if days_in_month == date:  # If new month
        if month == 12:  # If new year
            return (year + 1, 1, 1)
        return (year, month + 1, 1)
    return (year, month, date + 1)


def n_dates_back(n: int, current_date):
    date = current_date
    for _ in range(n):
        date = previus_date(date)
    return date


def n_dates_forward(n: int, current_date):
    date = current_date
    for _ in range(n):
        date = next_date(date)
    return date


def get_first_date(time_object, columns, rows, action) -> tuple:
    if action is None:
        current_date = time_object.year, time_object.month, time_object.day
        year, month, date = current_date
        main_month = calendar.monthcalendar(year, month)
        for week in main_month:
            for n, d in enumerate(week):
                if d == date:
                    return n_dates_back(n+1, current_date)
    else:
        current_date = int(action[0]), int(action[1]), int(action[2])
        if action[3] == "upp":
            return n_dates_back(7, current_date)
        elif action[3] == "ner":
            return n_dates_forward(7, current_date)
    return (1, 1, 1)


def get_matrix(columns: int, rows: int, first_date: tuple) -> list:
    matrix = []
    date = first_date
    for y in range(columns):
        row = []
        for x in range(rows):
            row.append(date)
            date = next_date(date)
        matrix.append(row)

    return matrix


def main():
    matrix = get_matrix(datetime.now(), 9, 7)
    from pprint import pprint
    pprint(matrix)


if __name__ == '__main__':
    main()
