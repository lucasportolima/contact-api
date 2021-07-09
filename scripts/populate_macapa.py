import json

from macapa.models import MacapaContact


def run():
    """ Populate the table with the given data source """

    with open('./compose/data_source/contacts-macapa.json', 'r', encoding='utf8') as json_data:
        data = json.load(json_data)

        for contact in data.get('contacts'):
            MacapaContact.objects.get_or_create(
                nome=contact['name'].upper(),
                celular=f"+{contact['cellphone'][0:2]} "
                        f"({contact['cellphone'][2:4]}) "
                        f"{contact['cellphone'][4:9]}-"
                        f"{contact['cellphone'][9:13]}"
            )
