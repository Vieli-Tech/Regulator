import traceback
from datetime import datetime
from time import sleep

from src.mnemonic2postgres.controllers.cassandra import CassandraController, CassandraRepository
from src.mnemonic2postgres.controllers.postgres import PostgresController, PostgresRepository
from src.tool import Tool


class Mnemonic2Postgres(Tool):

    def __init__(self):
        self.cassandra_host: str = '172.17.0.1'
        self.cassandra_port: int = 9042
        self.cassandra_keyspace: str = 'producao'
        self.cassandra_username: str = 'vieli'
        self.cassandra_password: str = 'Vieli145823'
        self.postgres_host: str = '172.17.0.1'
        self.postgres_port: int = 5432
        self.postgres_database: str = 'postgres'
        self.postgres_schema: str = 'producao'
        self.postgres_username: str = 'postgres'
        self.postgres_password: str = 'Vieli145823'
        self.menus = {
            'configurar': self.config,
            'listar cassandra': self.listarCassandra,
            'listar postgres': self.listarPostgres,
            'recriar tabelas postgres': self.recriarPostgres,
            'migrar dados': self.migrarDados
        }

    def config(self):
        self.cassandra_host = self.setConfig('Cassandra HOST', value=self.cassandra_host)
        self.cassandra_port = self.setConfig('Cassandra PORT', value=self.cassandra_port)
        self.cassandra_keyspace = self.setConfig('Cassandra Keyspace', value=self.cassandra_keyspace)
        self.cassandra_username = self.setConfig('Cassandra Username', value=self.cassandra_username)
        self.cassandra_password = self.setConfig('Cassandra Password', value=self.cassandra_password)
        self.postgres_host = self.setConfig('Postgres HOST', value=self.postgres_host)
        self.postgres_port = self.setConfig('Postgres PORT', value=self.postgres_port)
        self.postgres_database = self.setConfig('Postgres Database', value=self.postgres_database)
        self.postgres_schema = self.setConfig('Postgres Schema', value=self.postgres_schema)
        self.postgres_username = self.setConfig('Postgres Username', value=self.postgres_username)
        self.postgres_password = self.setConfig('Postgres Password', value=self.postgres_password)

    def listarCassandra(self):
        CassandraController.repository = CassandraRepository(
            self.cassandra_host,
            self.cassandra_port,
            self.cassandra_keyspace,
            self.cassandra_username,
            self.cassandra_password
        )
        CassandraController.getProducoes()
        CassandraController.getProduzidos()
        CassandraController.getRetrabalhos()
        CassandraController.getParadas()
        CassandraController.getAlterProducoes()
        CassandraController.getAlterProduzidos()
        CassandraController.getAlterRetrabalhos()
        CassandraController.getAlterParadas()
        input('\n\nPressione ENTER para continuar...')

    def listarPostgres(self):
        PostgresController.repository = PostgresRepository(
            self.postgres_host,
            self.postgres_port,
            self.postgres_database,
            self.postgres_schema,
            self.postgres_username,
            self.postgres_password
        )
        PostgresController.getProducoes()
        PostgresController.getProduzidos()
        PostgresController.getRetrabalhos()
        PostgresController.getParadas()
        PostgresController.getAlterProducoes()
        PostgresController.getAlterProduzidos()
        PostgresController.getAlterRetrabalhos()
        PostgresController.getAlterParadas()
        input('\n\nPressione ENTER para continuar...')

    @staticmethod
    def insertData(title: str, get: callable, set: callable):
        print('\nColetando {}...'.format(title))
        data = get() or []
        print('\nInserindo {}'.format(title))
        inserted = set(data)
        print('\nInseridos {} de {} {}'.format(inserted, len(data), title))

    def migrarDados(self):
        CassandraController.repository = CassandraRepository(
            self.cassandra_host,
            self.cassandra_port,
            self.cassandra_keyspace,
            self.cassandra_username,
            self.cassandra_password
        )
        PostgresController.repository = PostgresRepository(
            self.postgres_host,
            self.postgres_port,
            self.postgres_database,
            self.postgres_schema,
            self.postgres_username,
            self.postgres_password
        )
        self.insertData('Produções', CassandraController.getProducoes, PostgresController.insertProducao)
        self.insertData('Produzidos', CassandraController.getProduzidos, PostgresController.insertProduzidos)
        self.insertData('Retrabalhos', CassandraController.getRetrabalhos, PostgresController.insertRetrabalhos)
        self.insertData('Paradas', CassandraController.getParadas, PostgresController.insertParadas)
        self.insertData('Alter Produções', CassandraController.getAlterProducoes, PostgresController.insertAlterProducao)
        self.insertData('Alter Produzidos', CassandraController.getAlterProduzidos, PostgresController.insertAlterProduzidos)
        self.insertData('Alter Retrabalhos', CassandraController.getAlterRetrabalhos, PostgresController.insertAlterRetrabalhos)
        self.insertData('Alter Paradas', CassandraController.getAlterParadas, PostgresController.insertAlterParadas)
        input('\n\nPressione ENTER para continuar...')

    def recriarPostgres(self):
        PostgresController.repository = PostgresRepository(
            self.postgres_host,
            self.postgres_port,
            self.postgres_database,
            self.postgres_schema,
            self.postgres_username,
            self.postgres_password
        )
        PostgresController.recreateTables()
        input('\n\nPressione ENTER para continuar...')

    def run(self):
        while True:
            self.clearTerminal()
            print(
                """
 _ _ _                                  __  _ __                        
( / ) )                          o        )( /  )      _/_              
 / / / _ _   _  _ _ _   __ _ _  ,  _, .--'  /--'__ (   /  _,  _   _  (  
/ / (_/ / /_(/_/ / / /_(_)/ / /_(_(__(__   /   (_)/_)_(__(_)_/ (_(/_/_)_
                                                          /|            
                                                         (/             
            Utilize parar migrar o Mnemonic 1.16.5 para 2.0.0            
"""
            )
            print(
                'Configurações:\n\
\tCassandra HOST={}\n\
\tCassandra PORT={}\n\
\tCassandra Keyspace={}\n\
\tCassandra Username={}\n\
\tCassandra Password={}\n\
\tPostgres HOST={}\n\
\tPostgres PORT={}\n\
\tPostgres Database={}\n\
\tPostgres Username={}\n\
\tPostgres Password={}\n\
'.format(
    self.cassandra_host,
    self.cassandra_port,
    self.cassandra_keyspace,
    self.cassandra_username,
    self.cassandra_password,
    self.postgres_host,
    self.postgres_port,
    self.postgres_database,
    self.postgres_username,
    self.postgres_password
)
            )
            print('\nInforme uma opção:')
            for index, menu in enumerate(self.menus.keys()):
                print('\t* {} - {}'.format(index, menu))
            print('* Ou qualquer outra coisa para sair')
            choosen = input('Opção: ')
            length = len(self.menus.keys())
            try:
                index = int(choosen)
                if index > -1 and index < length:
                    choosen = list(self.menus.keys())[index]
            except ValueError:
                pass
            if choosen in self.menus.keys():
                self.menus[choosen]()
            else:
                return
