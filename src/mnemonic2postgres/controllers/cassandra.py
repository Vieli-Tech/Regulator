from src.mnemonic2postgres.repositories.cassandra import CassandraRepository

class CassandraController():

    repository: CassandraRepository = None

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
