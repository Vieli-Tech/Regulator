CREATE TABLE IF NOT EXISTS producao.producao(
  equipamento int,
  id text PRIMARY KEY,
  data float,
  turno smallint,
  inicio float,
  fim float,
  total_turno float,
  total_parada_nao_programada float,
  total_parada_programada float,
  total_produzido float,
  total_retrabalho float,
  total_descarte float,
  hash_paradas bigint,
  hash_produzidos bigint,
  hash_retrabalhos bigint,
  id_octopus text,
  desconsiderada boolean
);