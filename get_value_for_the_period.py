from get_dict_from_xml import get_dict_from_xml


def get_value_for_the_period(days: list, name: str, year: str, moth: str):
    list_dict_period = [get_dict_from_xml(year, moth, day) for day in days]

    return [(int(day), item[name]['Value']) for day, item in zip(days, list_dict_period)]


if __name__ == '__main__':
    days_list = [f'{i:02}' for i in range(1, 20)]
    print(get_value_for_the_period(days_list, 'Австралийский доллар', '2022', '04'))
