CREATE DATABASE IF NOT EXISTS bachelor_project;

use bachelor_project;

drop table if exists Student;
create table Student (
	MSSV int,
    name char(30),
    email varchar(255),
    pwd varchar(255)
);

create table Admin (
    name char(30),
    email varchar(255),
    pwd varchar(255)
);

create table Teacher (
    name char(30),
    email varchar(255),
    pwd varchar(255)
);



insert into Student values 
	(123, 'test', 'test', ''),
    (1, 'test1', 'test', ''),
    (2, 'test2', 'test', ''),
    (3, 'test3', 'test', ''),
    (4, 'test4', 'test', ''),
    (5, 'test5', 'test', ''),
	(20170067, N'Trương Ngọc Giang', 'giangtn.170067@sis.hust.edu.vn', '123456'),
    (20170068, N'Trương Quang Khánh', 'khanhtq.170068@sis.hust.edu.vn', '123456'),
    (20170069, N'Trần Minh Hiếu', 'hieutm.170069@sis.hust.edu.vn', '123456'),
    (20170070, N'Nguyễn Mai Phương', 'phuongnm.170070@sis.hust.edu.vn', '123456')
;

insert into Admin values 
	('admin', 'admin', '')
;

insert into Teacher values 
	('teacher', 'teacher', '')
;

select * from Student;

drop table if exists Attendance_History;
create table Attendance_History (
	id int auto_increment,
	MSSV int,
    time_attend datetime,
    primary key(id)
);

insert into Attendance_History values (null, 1, "2011-01-18 01:17:17");
select * from Attendance_History;

