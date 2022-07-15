from datetime import date, timedelta
from get_dict_from_xml import get_dict_from_xml


# Неделя
# Месяц
# Квартал (1/4 Года)
# Год

def get_period_days(period=1):
    return [str(date.today()).split('-')] + \
           [str(date.today() - timedelta(days=i)).split('-') for i in range(1, period)]


def get_period_month(period=1):
    return [str(date.today()).split('-')] + \
           [str(date.today() - timedelta(days=(31 * i))).split('-') for i in range(1, period)]


def get_week_from_name(name: str):
    dates = get_period_days(7)
    return [(dat, get_dict_from_xml(*dat)[name]['Value']) for dat in dates]


def get_month_from_name(name: str):
    dates = get_period_days(31)
    return [(dat, get_dict_from_xml(*dat)[name]['Value']) for dat in dates]


def get_quarter_from_name(name: str):
    dates = get_period_days(93)
    return [(dat, get_dict_from_xml(*dat)[name]['Value']) for dat in dates]


def get_year_from_name(name: str):
    # dates = get_period_month(12)
    dates = get_period_days(372)
    return [(dat, get_dict_from_xml(*dat)[name]['Value']) for dat in dates]


if __name__ == '__main__':
    print(get_period_days(7))
    print(get_period_month(6))

    print(get_week_from_name('Австралийский доллар'))
    print(get_month_from_name('Австралийский доллар'))
    print(get_quarter_from_name('Австралийский доллар'))
    print(get_year_from_name('Австралийский доллар'))
