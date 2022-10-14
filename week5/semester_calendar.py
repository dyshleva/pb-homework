"""
Semester calendar assignment
"""

from calendar import TextCalendar, HTMLCalendar


def semester_calendar(
    output_type: str, year: int, first_month: int, last_month: int
) -> str:
    """
    Make a string of months.

    Args:
        output_type: outhpu type. txt or html
        year: year to print months from
        first_month: month to strt with
        last_month: last month

    Returns:
        str: a string of a formatted calendar

    >>> semester_calendar("txt", 2021, 10, 10)
    '    October 2021\\nMo Tu We Th Fr Sa Su\\n             1  2  3\\n 4  5  6  7  8  9 10\\n\
11 12 13 14 15 16 17\\n18 19 20 21 22 23 24\\n25 26 27 28 29 30 31\\n'
    >>> semester_calendar("html", 2021, 10, 10)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" class=\
"month">October 2021</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class=\
"wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class=\
"sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class=\
"noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td>\
<td class="sun">3</td></tr>\\n<tr><td class="mon">4</td><td class="tue">5</td><td class=\
"wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td><td class=\
"sun">10</td></tr>\\n<tr><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td>\
<td class="thu">14</td><td class="fri">15</td><td class="sat">16</td><td class="sun">17</td>\
</tr>\\n<tr><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">\
21</td><td class="fri">22</td><td class="sat">23</td><td class="sun">24</td></tr>\\n<tr>\
<td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td>\
<td class="fri">29</td><td class="sat">30</td><td class="sun">31</td></tr>\\n</table>\\n'
    """
    result = []

    for month in range(first_month, last_month + 1):
        # Make year and month.
        # If month > 12, then formatmonth ill fail, so for that we just
        # Increment the year
        year_mod = year + month // 12
        mth = month % 12 if (month % 12) != 0 else 1
        if output_type == "txt":
            result.append(TextCalendar().formatmonth(year_mod, mth))
        else:
            result.append(HTMLCalendar().formatmonth(year_mod, mth))

    return "\n".join(result)
