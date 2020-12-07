drop database if exists multiplex_db;
drop schema if exists multiplex_schema;
####################
# initialize schema, db
####################
#CREATE SCHEMA if not exists multiplex_schema;
#select database();
create DATABASE if not exists multiplex_db;
USE  multiplex_db;
####################
# create tables
####################
CREATE TABLE IF NOT EXISTS Movies(
	MovieId int auto_increment primary key,
    MovieName varchar(255) not null
		);
        
CREATE TABLE IF NOT EXISTS Users(
	UserId int auto_increment primary key not null,
    UserName varchar(45),
    UserType char,
    MobileNo varchar(15), #https://en.wikipedia.org/wiki/Telephone_numbering_plan#:~:text=International%20numbering%20plan,-The%20E.&text=as%20the%20NANP.-,E.,)%2C%20and%20the%20subscriber%20number.
    EmailId varchar(255)
	);
    
CREATE TABLE IF NOT EXISTS Hall(
	HallID int primary key auto_increment,
    HallDesc varchar(255),
    TotalCapacity numeric
	);

create table if not exists SeatType(
	SeatTypeID numeric primary key,
    SeatTypeDesc varchar(255),
    SeatFare float
	);
    
create table if not exists HallCapacity(
	HallID int,
    SeatTypeID numeric,
    SeatCount numeric,
    primary key (HallID, SeatTypeID)
	);

create table if not exists BookingDetail(
	BookingId int,
    SeatTypeId Numeric,
    NoOfSeats Numeric
	);
    
create table if not exists Booking(
	BookingId int primary key auto_increment,
    ShowId int,
    UserId int,
    BookedDate date,
    showdate date
	);

create table if not exists Shows(
	ShowId int primary key auto_increment,
    HallId int,
    MovieId int,
    SlotNo numeric,
    FromDate date,
    ToDate date    
	);
    
####################
# Add indices & FK constraints
create index movies_fk_ix #Seems index is required on some foreign keys but not all?
	on Movies(MovieId);
####################
alter table HallCapacity
	add foreign key (HallID) references Hall(HallID),
    add foreign key (SeatTypeId) references SeatType(SeatTypeID)
    ;
alter table BookingDetail
	add foreign key (BookingId) references Booking(BookingId),
    add foreign key (SeatTypeId) references SeatType(SeatTypeId)
    ;
alter table Booking
	add foreign key (ShowId) references Shows(ShowId),
    add foreign key (UserId) references Users(UserId)
    ;
alter table Shows
	add foreign key (HallID) references Hall(HallID),
    add foreign key (MovieId) references Movies(MovieId)
	;
alter table Users
	add constraint EmailId_like_ptrn
		check (EmailId like "_%@_%._%"),
	add constraint type_is_admin_or_cust
		check (userType in ("a","c"))
	;

####################
# add test data
####################
insert into Movies (MovieId, MovieName)
	values  (Null, "Blade Runner (1982)"), 
			(Null, "The Matrix (1999)"),
            (Null, "Star Wars (1977)");
            
insert into Users (UserId, UserName, UserType, MobileNo, EmailId)
	values  (Null, "Rick Deckard", "c", "1-982-2523", "rdeckard@lapd.gov"),
			(Null, "Roy Batty", "c", "1-982-2523", Null),
			(Null, "Agent Smith", "a", "1-243-6877", "smith@agents.net"),
            (Null, "Obi Wan Kenobi", "c", "8-286-6646", "smith@agents.net");

insert into Hall (HallID, HallDesc, TotalCapacity)
	values  (1, "Snake Pit", 200),
			(2, "Nebudchanezzar", 250),
			(3, "Death Star", 300);  
            
insert into SeatType (SeatTypeId, SeatTypeDesc, SeatFare)
	values  (1, 'Executive', 25),
			(2, 'Premium', 17),
            (3, 'Regular', 11)
            ;

insert into HallCapacity (HallId, SeatTypeId, SeatCount)
	values	(1, 1, 25),
			(1, 2, 50),
			(1, 3, 125),
			(2, 1, 40),
            (2, 2, 80),
            (2, 3, 140),
            (3, 1, 50),
            (3, 2, 75),
            (3, 3, 175)
            ;

insert into Shows (ShowId, HallId, MovieId, SlotNo, FromDate, ToDate)
	values	(null, 1, 1, 1, "2021-02-01", "2022-02-01"),
			(null, 2, 2, 2, "2021-02-01", "2022-02-01"),
			(null, 3, 3, 3, "2021-02-01", "2022-02-01")
			;

insert into Booking (ShowId, UserId, BookedDate, ShowDate)
	values	(1, 1, "2021-1-25", "2021-02-01"),
			(2, 2, "2021-1-25", "2021-02-01"),
            (3, 3, "2021-1-25", "2021-02-01")
            ;

insert into BookingDetail (BookingId, SeatTypeId, NoofSeats)
	values 	(1, 1, 1),
			(2, 2, 2),
			(3, 3, 3)
            ;
