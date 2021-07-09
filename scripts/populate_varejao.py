import json

from varejao.models import VarejaoContact


def run():
    """ Populate the table with the given data source """

    with open('./compose/data_source/contacts-varejao.json', 'r', encoding='utf8') as json_data:
        data = json.load(json_data)

        for contact in data.get('contacts'):
            VarejaoContact.objects.get_or_create(
                nome=contact['name'],
                celular=contact['cellphone']
            )
