from dataclasses import dataclass, field
from itertools import count
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


def calculate_first_date() -> tuple:
    return (1, 1, 1)


def set_calender(first_date: tuple, n_days: int) -> dict:
    calender = {}
    date = first_date
    for n in range(n_days):
        calender[n] = date
        date = next_date(date)
    return calender


@dataclass(kw_only=True)
class DisplaySettings:
    rows: int = 7
    columns: int = 6
    n_squares: int = field(init=False)
    interval: int = 1  # Number of rows moved from arrowbutton
    month_focus: bool = True

    def __post_init__(self):
        self.n_squares = self.rows * self.columns


@dataclass()
class CalenderMatrix:
    display_settings: object
    calender: dict = field(init=False, repr=False)
    day_names: tuple = field(repr=False,
                             default=('Monday', 'Tuesday', 'Wednesday',
                                      'Thursday', 'Friday', 'Saturday',
                                      'Sunday'))
    month_names: tuple = field(repr=False,
                               default=("January", "February", "March",
                                        "April", "May", "June", "July",
                                        "August", "September", "October",
                                        "November", "December"))

    def __post_init__(self):
        n_days = self.display_settings.n_squares
        first_date = calculate_first_date()
        self.calender = set_calender(first_date, n_days)

    def matrix_generater(self):
        n = count()
        x, y = self.display_settings.rows, self.display_settings.columns
        return((next(n) for _ in range(x)) for _ in range(y))

    def get_month_name(self, month_number: int) -> str:
        return self.month_names[month_number+1]


def main():
    s = DisplaySettings(rows=9)
    print(s)

    c = CalenderMatrix(display_settings=s)

    print(c)
    matrix = c.matrix_generater()
    print(matrix)
    for i in matrix:
        for j in (i):
            # print(j)
            pass


if __name__ == '__main__':
    main()
