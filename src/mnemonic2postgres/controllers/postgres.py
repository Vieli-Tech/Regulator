from src.mnemonic2postgres.repositories.postgres import PostgresRepository

class PostgresController():

    repository: PostgresRepository = None

    @classmethod
    def getProducoes(cls):
        return cls.repository.getAll('producao')

    @classmethod
    def getProduzidos(cls):
        return cls.repository.getAll('produzidos')

    @classmethod
    def getParadas(cls):
        return cls.repository.getAll('paradas')

    @classmethod
    def getRetrabalhos(cls):
        return cls.repository.getAll('retrabalhos')

    @classmethod
    def getAlterProducoes(cls):
        return cls.repository.getAll('alter_producao')

    @classmethod
    def getAlterProduzidos(cls):
        return cls.repository.getAll('alter_produzidos')

    @classmethod
    def getAlterParadas(cls):
        return cls.repository.getAll('alter_paradas')

    @classmethod
    def getAlterRetrabalhos(cls):
        return cls.repository.getAll('alter_retrabalhos')

    @classmethod
    def recreateTables(cls):
        return [cls.repository.recreateTable(table) for table in [
            'producao',
            'produzidos',
            'retrabalhos',
            'paradas',
            'alter_producao',
            'alter_produzidos',
            'alter_retrabalhos',
            'alter_paradas'
        ]]

    @classmethod
    def insertProducao(cls, data: list):
        return cls.repository.insertArray('producao', data)

    @classmethod
    def insertProduzidos(cls, data: list):
        return cls.repository.insertArray('produzidos', data)

    @classmethod
    def insertParadas(cls, data: list):
        return cls.repository.insertArray('paradas', data)

    @classmethod
    def insertRetrabalhos(cls, data: list):
        return cls.repository.insertArray('retrabalhos', data)

    @classmethod
    def insertAlterProducao(cls, data: list):
        return cls.repository.insertArray('alter_producao', data)

    @classmethod
    def insertAlterProduzidos(cls, data: list):
        return cls.repository.insertArray('alter_produzidos', data)

    @classmethod
    def insertAlterParadas(cls, data: list):
        return cls.repository.insertArray('alter_paradas', data)

    @classmethod
    def insertAlterRetrabalhos(cls, data: list):
        return cls.repository.insertArray('alter_retrabalhos', data)
