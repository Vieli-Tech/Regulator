CREATE TABLE IF NOT EXISTS producao.produzidos(
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
  tempo_morto float,
  quantidade_esperada float
);
