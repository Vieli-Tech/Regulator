from cassandra.cluster import Cluster, Session, ResultSet

class CassandraRepository():

    def __init__(
        self,
        host,
        port,
        keyspace,
        username,
        password
    ):
        self.cluster = Cluster([host], port=port)
        try:
            self.session: Session = self.cluster.connect()
            self.session.set_keyspace(keyspace)
        except Exception as e:
            print('[Cassandra Repository] ', e)

    def getAll(self, table):
        result = []
        query = 'SELECT * FROM {};'.format(
            table
        )
        try:
            print('[Cassandra Repository] Executando: \n', query)
            res: ResultSet = self.session.execute(query)
            for item in res:
                result.append(
                    item._asdict()
                )
            print('[Cassandra Repository] Obtido reposta: \n', result)
            return result
        except Exception as e:
            print('[Cassandra Repository] ', e)


