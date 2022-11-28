create database akinator;
use akinator;
create table color(id int auto_increment PRIMARY KEY, color varchar(20) not null);
create table tamanio(id int auto_increment PRIMARY KEY, tamanio varchar(20) not null);
create table tipo(id int auto_increment PRIMARY KEY, tipo varchar(20) not null);
create table pokemon(id int auto_increment PRIMARY KEY, pokemon varchar(20) not null);
create table caracteristica(id int auto_increment PRIMARY KEY, caracteristica varchar(20) not null);
create table aprendizaje(id int auto_increment PRIMARY KEY, color int, tamanio int, tipo  int, caracteristica1 int, caracteristica2 int, caracteristica3 int, caracteristica4 int, caracteristica5 int, pokemon int, total float);


insert into color(color)values("azul");
insert into color(color)values("verde");
insert into color(color)values("rojo");
insert into color(color)values("amarillo");
insert into color(color)values("morado");
insert into color(color)values("cafe");
insert into color(color)values("negro");
insert into color(color)values("blanco");
insert into color(color)values("naranja");

insert into tamanio(tamanio)values("chico");
insert into tamanio(tamanio)values("mediano");
insert into tamanio(tamanio)values("grande");

insert into tipo(tipo)values("normal");
insert into tipo(tipo)values("electrico");
insert into tipo(tipo)values("fuego");
insert into tipo(tipo)values("agua");
insert into tipo(tipo)values("planta");
insert into tipo(tipo)values("lucha");
insert into tipo(tipo)values("psiquico");
insert into tipo(tipo)values("fantasma");
insert into tipo(tipo)values("bicho");
insert into tipo(tipo)values("veneno");

insert into pokemon(pokemon)values("Snorlax");
insert into pokemon(pokemon)values("Bulbasaur");
insert into pokemon(pokemon)values("Charizard");
insert into pokemon(pokemon)values("Wartortle");
insert into pokemon(pokemon)values("Pikachu");

insert into aprendizaje(color,tamanio,tipo,pokemon)values(1,2,1,1);
insert into aprendizaje(color,tamanio,tipo,pokemon)values(2,1,5,2);
insert into aprendizaje(color,tamanio,tipo,pokemon)values(9,3,3,3);
insert into aprendizaje(color,tamanio,tipo,pokemon)values(1,2,4,4);
insert into aprendizaje(color,tamanio,tipo,pokemon)values(4,1,2,5);

SET SQL_SAFE_UPDATES = 0;
select * from aprendizaje;
update aprendizaje set total = 10 where pokemon = 1;
update aprendizaje set total = 19 where pokemon = 2;
update aprendizaje set total = 24 where pokemon = 3;
update aprendizaje set total = 17 where pokemon = 4;
update aprendizaje set total = 12 where pokemon = 5;




