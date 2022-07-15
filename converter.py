from get_dict_from_xml import get_dict_from_xml
from datetime import date


def converter(name_from: str, name_to: str, count: int) -> float:
    data = get_dict_from_xml(*str(date.today()).split('-'))

    if name_from == 'Российский рубль':
        # result = data[name_to]['Value'] * count
        result = (1 / (data[name_to]['Value'])) * count

    elif name_to == 'Российский рубль':
        result = data[name_from]['Value'] * count

    else:
        value_form = data[name_from]['Value']
        nominal_from = data[name_from]['Nominal']

        value_to = data[name_to]['Value']
        nominal_to = data[name_to]['Nominal']
        result = ((nominal_to * value_form) / (value_to * nominal_from)) * count

    return result


if __name__ == '__main__':
    print(converter('Швейцарский франк', 'Доллар США', 1))
    print(converter('Доллар США', 'Швейцарский франк', 1))
