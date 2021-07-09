from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.sql import text


def run():
    """ Create the tables of the models that will be used """

    engine_macapa = create_engine(settings.MACAPA_CONNECTION_STRING_ENGINE)
    engine_varejao = create_engine(settings.VAREJAO_CONNECTION_STRING_ENGINE)

    with engine_macapa.connect() as con:
        file = open("./compose/sql_scripts/create-table-macapa.sql")
        query = text(file.read())

        con.execute(query)

    with engine_varejao.connect() as con:
        file = open("./compose/sql_scripts/create-table-varejao.sql")
        query = text(file.read())

        con.execute(query)

    engine_macapa.dispose()
    engine_varejao.dispose()
