from dataclasses import dataclass
from itertools import islice
import calender_functions


@dataclass(kw_only=True)
class DisplaySettings:
    rows: int = 7
    columns: int = 6
    headline: str = None
    vertical_interval: int = 5*6


@dataclass(kw_only=True)
class CalenderMatrix:
    display_settings: object
    calender: dict = None

    def chunks(self):
        data, SIZE = self.calender, self.display_settings.rows
        it = iter(data)
        for i in range(0, len(data), SIZE):
            yield {k: data[k] for k in islice(it, SIZE)}

    def set_calender(self, first_date: tuple):
        calender = {}
        n_days = self.display_settings.rows * self.display_settings.columns
        date = first_date
        for n in range(n_days):
            calender[n] = date
            date = calender_functions.next_date(date)
        self.calender = calender


def main():
    s = DisplaySettings(rows=9, headline="gr")
    print(s)
    s.row = 10
    print(s)
    c = CalenderMatrix(display_settings=s)
    c.set_calender((1, 1, 1))
    print(c.calender)
    matrix = c.chunks()
    print(matrix)
    for i in matrix:
        print(i)

if __name__ == '__main__':
    main()
