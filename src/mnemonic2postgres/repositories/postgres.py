from postgres import Postgres


class PostgresRepository():

    def __init__(
        self,
        host,
        port,
        database,
        schema,
        username,
        password
    ):
        url = 'postgresql://{}:{}@{}:{}/{}'.format(
            username,
            password,
            host,
            port,
            database
        )
        try:
            self.schema = schema
            self.connection = Postgres(url=url)
        except Exception as e:
            print('[Postgres Repository] ', e)

    def getAll(self, table):
        result = []
        query = 'SELECT * FROM {}.{};'.format(
            self.schema,
            table
        )
        try:
            print('[Postgres Repository] Executando: \n', query)
            res = self.connection.all(query)
            print(res)
            for item in res:
                print(type(item))
                print(item)
                result.append(
                    item._asdict()
                )
            print('[Postgres Repository] Obtido reposta: \n', result)
            return result
        except Exception as e:
            print('[Postgres Repository] ', e)

    def recreateTable(self, table):
        query = 'DROP TABLE IF EXISTS {}.{}'.format(
            self.schema,
            table
        )
        try:
            print('[Postgres Repository] Executando: \n', query)
            self.connection.run(query)
            query = ''
            with open('src/mnemonic2postgres/tables/tabela_{}.sql'.format(table)) as f:
                query = f.read()
                f.close()
            print('[Postgres Repository] Executando: \n', query)
            self.connection.run(query)
        except Exception as e:
            print('[Postgres Repository] ', e)

    def insertArray(self, table, data: list):
        query = ''
        item: dict
        inserteds = 0
        for item in data:
            keys = ''
            values = ''
            length = len(item.keys())
            for index, key in enumerate(item.keys()):
                value = item[key]
                if isinstance(value, str):
                    value = "'{}'".format(value)
                elif value is True:
                    value = 'true'
                elif value is False:
                    value = 'false'
                elif value is None:
                    value = 'null'
                values += str(value)
                keys += key
                if index + 1 != length:
                    values += ','
                    keys += ','
            query = 'INSERT INTO {}.{} ({}) VALUES ({});'.format(
                self.schema,
                table,
                keys,
                values
            )
            try:
                print('[Postgres Repository] Executando: \n', query)
                self.connection.run(query)
                inserteds += 1
            except Exception as e:
                print('[Postgres Repository] ', e)
        return inserteds
