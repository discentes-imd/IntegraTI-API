create database integrati 
	DEFAULT CHARACTER SET utf8
	DEFAULT COLLATE utf8_general_ci;;
use integrati;

create table cad_user{
	id_user int(10) unsigned not null auto_increment,
	name varchar(100) not null,
	sigaa_matricula varchar(15) not null,
	sigaa_user_name varchar(30) not null,
	sigaa_password varchar(100) not null,
	path_foto varchar(255) not null, 
	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_user),
	unique(sigaa_matricula),
	unique(sigaa_user_name),
	foreign key(id_user_insert references cad_user(id_user) on delete set null,
	foreign key(id_user_update) references cad_user(id_user) on delete set null
};

create table cad_event_type(
	id_event_type int(10) unsigned not null auto_increment,
	name varchar(100) not null,
	description varchar(255) not null,
	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_type),
	foreign key(id_user_insert references cad_user(id_user) on delete set null,
	foreign key(id_user_update) references cad_user(id_user) on delete set null
);

create table cad_event(
	id_event int(10) unsigned not null auto_increment,
	id_event_type int(10) not null unsigned, 
	title varchar(100) not null,
	description varchar(255) not null,
	date_event_start datetime not null,
	date_event_end datetime not null,
	location varchar(255) not null,
	url varchar(255) not null,
	help enum('0', '1') not null,
	id_organizer int(10) unsigned not null,
	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event),
	foreign key(id_user_insert references cad_user(id_user) on delete set null,
	foreign key(id_user_update) references cad_user(id_user) on delete set null
);

create table cad_event_file(
	id_event_file int(10) unsigned not null auto_increment,
	id_event int(10) unsigned not null,
	name varchar(255) not null,
	description varchar(255) not null,
	path_file varchar(255) not null,
	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_file),
	foreign key(id_event) references cad_event(id_event) on delete cascade,
	foreign key(id_user_insert references cad_user(id_user) on delete set null,
	foreign key(id_user_update) references cad_user(id_user) on delete set null
);
