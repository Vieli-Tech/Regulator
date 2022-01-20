CREATE TABLE IF NOT EXISTS producao.alter_producao(
  equipamento int,
  id text PRIMARY KEY,
  data float,
  turno smallint,
  desconsiderada boolean
);
