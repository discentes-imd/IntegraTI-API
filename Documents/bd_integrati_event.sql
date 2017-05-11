create database integrati 
	DEFAULT CHARACTER SET utf8
	DEFAULT COLLATE utf8_general_ci;;
use integrati;

create table reg_tag(
	id_tag int(10) unsigned not null auto_increment,
	name varchar(50) not null,
	slug varchar(50) not null,
	
	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_tag),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_user{
	id_user int(10) unsigned not null auto_increment,
	name varchar(100) not null,

	sigaa_matricula varchar(15) not null,

	username varchar(30) not null,
	password varchar(100) not null,

	path_foto varchar(255) not null, 

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_user),
	unique(sigaa_matricula),
	unique(sigaa_user_name),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
};

create table reg_user_interest(
	id_user_interest int(10) unsigned not null auto_increment,
	id_user int(10) unsigned not null
	id_tag int(10) unsigned not null, 

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_file),
	unique(id_user, id_tag),
	foreign key(id_user) references reg_user(id_user),
	foreign key(id_tag) references reg_tag(id_tag),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_file(
	id_file int(10) unsigned not null auto_increment,
	name varchar(255) not null,
	description varchar(255) not null,
	path_file varchar(255) not null,

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_file),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_event_type(
	id_event_type int(10) unsigned not null auto_increment,
	name varchar(100) not null,
	description varchar(255) not null,

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_type),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_event(
	id_event int(10) unsigned not null auto_increment,
	id_event_type int(10) unsigned not null, 
	id_organizer int(10) unsigned not null,
	title varchar(100) not null,
	description varchar(255) not null,
	date_event_start datetime not null,
	date_event_end datetime not null,
	location varchar(255) not null,
	url varchar(255) not null,
	help boolean not null,

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event),
	foreign key(id_event_type) references reg_event_type(id_event_type),
  	foreign key(id_organizer) references reg_user(id_user),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_event_file(
	id_event_file int(10) unsigned not null auto_increment,
	id_event int(10) unsigned not null
	id_file int(10) unsigned not null, 

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_file),
	unique(id_file),
	foreign key(id_event) references reg_event(id_event),
	foreign key(id_file) references reg_file(id_file),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);

create table reg_event_tag(
	id_event_tag int(10) unsigned not null auto_increment,
	id_event int(10) unsigned not null
	id_tag int(10) unsigned not null, 

	id_user_insert int(10) unsigned, 
	id_user_update int(10) unsigned,
	data_insert datetime not null,
	data_update timestamp not null,
	primary key(id_event_file),
	unique(id_event, id_tag),
	foreign key(id_event) references reg_event(id_event),
	foreign key(id_tag) references reg_tag(id_tag),
	foreign key(id_user_insert) references reg_user(id_user),
  	foreign key(id_user_update) references reg_user(id_user)
);
