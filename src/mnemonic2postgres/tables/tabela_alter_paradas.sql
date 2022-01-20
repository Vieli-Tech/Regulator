CREATE TABLE IF NOT EXISTS producao.alter_paradas(
  id_producao text,
  id_parada float PRIMARY KEY,
  parada int,
  categoria int,
  nome text,
  programada boolean,
  inicio float,
  fim float,
  tempo float,
  hora_alteracao float,
  deletado boolean,
  equipamento int,
  turno int,
  data float,
  usuario text
);
