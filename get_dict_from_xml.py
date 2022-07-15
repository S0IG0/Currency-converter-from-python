from get_xml import get_xml
import xml.dom.minidom


def get_dict_from_xml(year='2022', moth='04', day='22') -> dict:
    currency_dict = dict()
    response = get_xml(year, moth, day)

    dom = xml.dom.minidom.parseString(response.text)
    dom.normalize()
    node_list = dom.getElementsByTagName('Valute')

    for node in node_list:
        child_list = node.childNodes
        temp_dict = dict()
        for child in child_list:
            temp_dict[child.nodeName] = child.childNodes[0].nodeValue
        currency_dict[temp_dict['Name']] = temp_dict

    for key in currency_dict.keys():
        currency_dict[key]['Value'] = float(currency_dict[key]['Value'].replace(',', '.'))
        currency_dict[key]['Nominal'] = float(currency_dict[key]['Nominal'].replace(',', '.'))

    return currency_dict


if __name__ == '__main__':
    print(get_dict_from_xml())
