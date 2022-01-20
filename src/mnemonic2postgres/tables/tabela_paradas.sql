CREATE TABLE IF NOT EXISTS producao.paradas(
  id_producao text,
  id_parada float PRIMARY KEY,
  parada int,
  categoria int,
  nome text,
  programada boolean,
  inicio float,
  fim float,
  tempo float,
  equipamento int,
  turno smallint,
  data float
);