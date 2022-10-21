"""
One month calendar submission
"""
from calendar import monthcalendar
from calendar import weekday as wd

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    try:
        return ("mon", "tue", "wed", "thu", "fri", "sat", "sun")[number]
    # That's probably counterproductive, but I don't care anymore
    except IndexError as exc:
        raise ValueError from exc


def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    fn_day, fn_month, fn_year = map(int, date.split('.'))

    return wd(fn_year, fn_month, fn_day)

def calendar(fn_month: int, fn_year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """

    weeks = monthcalendar(fn_year, fn_month)

    result = "mon tue wed thu fri sat sun\n"

    result += "\n".join(
            " ".join('   ' if day==0 else str(day).rjust(3) for day in week)
            for week in weeks
        )
    return result.rstrip()


def transform_calendar(fn_calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    lines = fn_calendar.split('\n')

    result = [[] for i in range(7)]

    for line in lines:
        for j, i in enumerate(range(0, 27, 4)):
            day = line[i: i+4]
            day = ' ' if not day.strip() else day.strip()
            result[j].append(day)

    return '\n'.join(" ".join(line).rstrip() for line in result)


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print(calendar(month, year))
    except ValueError as err:
        print(err)
