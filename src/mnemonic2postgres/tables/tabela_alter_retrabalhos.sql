CREATE TABLE IF NOT EXISTS producao.alter_retrabalhos(
  id_producao text,
  id_retrabalho float PRIMARY KEY,
  descarte boolean,
  retrabalho int,
  nome text,
  quantidade float,
  inicio float,
  fim float,
  tempo float,
  hora_alteracao float,
  deletado boolean,
  produto int,
  contagem int,
  equipamento int,
  turno int,
  data float,
  usuario text
);
