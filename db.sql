create table coffee (
  id integer primary key autoincrement,
  sort text not null,
  degree_of_roasting text not null, 
  kind text not null, 
  taste_description text,
  price bigint not null,
  volume real not null
);

insert into coffee (sort, degree_of_roasting, kind, taste_description, price, volume) values 
  ("арабика", "светлая", "молотый", "тонкий, с апельсинвыми нотками", 350, 0.5),
  ("рабуста", "темнее средней", "в зёрнах", "терпкий с насыщенным ароматом", 500, 1),
  ("мокко", "средняя", "в зёрнах", "освежающее послевкусие, яркий букет ароматов", 400, 0.75);

