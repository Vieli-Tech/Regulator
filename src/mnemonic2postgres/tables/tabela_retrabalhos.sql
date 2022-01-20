CREATE TABLE IF NOT EXISTS producao.retrabalhos(
  id_producao text,
  id_retrabalho float PRIMARY KEY,
  descarte boolean,
  retrabalho int,
  nome text,
  quantidade float,
  inicio float,
  fim float,
  tempo float,
  usuario text,
  produto bigint,
  contagem int,
  equipamento int,
  turno smallint,
  data float
);
