CREATE TABLE IF NOT EXISTS producao.alter_produzidos(
  id_producao text,
  id_produzido float PRIMARY KEY,
  equipamento int,
  turno smallint,
  data float,
  quantidade float,
  inicio float,
  fim float,
  tempo float,
  produto bigint,
  nome text,
  contagem int,
  hora_alteracao float,
  deletado boolean,
  tempo_morto float,
  quantidade_esperada float
);
