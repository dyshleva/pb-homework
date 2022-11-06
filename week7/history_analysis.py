"""
history_analysis submission
"""


def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([], "2022-11-11")
    set()
    """
    lst = list(filter(lambda search: search[2] == date, visits))
    if lst != []:
        return set(map(lambda site: site[0], lst))
    return set()


def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([], 12)
    set()
    """
    if not visits:
        return set()
    res_dct = {}
    for visit in visits:
        if visit[0] in res_dct:
            res_dct[visit[0]] += 1
        else:
            res_dct[visit[0]] = 1

    lst = list(res_dct.items())
    lst = sorted(lst, key=lambda x: x[1])
    lst = list(map(lambda x: x[0], lst))
    return set(lst[:number])


def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([], "https://reddit.com/")
    set()
    >>> get_url_info([("https://reddit.com/", "Reddit", "2021-11-11", "11:11:11.111")], "https://reddit.com/")
    ('Reddit', '2021-11-11', '11:11:11.111', 1, '11:11:11.111')
    """
    lst = list(filter(lambda x: url in x[0], visits))
    if lst == []:
        return set()
    title = lst[0][1]
    last_visit = max(map(lambda x: int(x[2].replace("-", "")), lst))
    time_tuples = list(map(lambda x: tuple(map(float, (x[3].split(':')))), lst))
    average_time_tuple = tuple(map(lambda x: x / len(time_tuples), map(sum, zip(*time_tuples))))
    for visit in lst:
        if visit[2].replace("-", "") == str(last_visit):
            visit_time = visit[3]
            visit_date = visit[2]

    return (title, visit_date, visit_time, len(lst), f'{average_time_tuple[0]:02.0f}:{average_time_tuple[1]:02.0f}:{average_time_tuple[2]:02.3f}')
