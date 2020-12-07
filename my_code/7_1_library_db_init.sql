########################################################
# init db
########################################################
drop database if exists library;
create DATABASE if not exists library;
USE library;

# title, copy, rental
########################################################
# init tables
########################################################
drop table if exists title;
create table title(
	titleId int auto_increment primary key not null,
    titleName varchar(255) not null,
    titleYear year,
    author varchar(255),
    publisher varchar(255),
    titleDesc varchar(255)
	);

drop table if exists copy;
create table copy(
    copyId int auto_increment primary key not null,
    titleId int,
    copyCondition enum("mint", "acceptable", "poor", "damaged", "lost") default "acceptable", #maybe copycondition should its own table?
    acquiredDate date not null,
    inCirculation boolean,
    retiredDate date,
    checkedIn boolean default True
    );

drop table if exists cust;
create table cust(
    custId int auto_increment primary key not null,
    custName varchar(255),
    custPhone int,#varchar(15),
    custPhone_sms boolean default FALSE,
    custEmailId varchar(320) #https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address#:~:text=%22There%20is%20a%20length%20limit,total%20length%20of%20320%20characters.
    );

drop table if exists rental;
create table rental(
    rentalId int auto_increment primary key not null,
    titleId int,
    custId int,
    copyId int,
    checkoutdate date,
    duedate date,
    copyCondition enum("mint", "acceptable", "poor", "damaged", "lost") #maybe copycondition should its own table?
);

drop table if exists checkin;
create table checkin(
	checkinId int auto_increment primary key not null,
    custId int,
    rentalId int,
    copyId int,
    checkinDate date, 
    copyCondition enum("mint", "acceptable", "poor", "damaged", "lost") #maybe copycondition should its own table?
);
########################################################
# add fk constraints
########################################################
alter table copy
    add foreign key (titleId) references title(titleId)
    ;
alter table rental
    add foreign key (custId) references cust(custId),
    add foreign key (copyId) references copy(copyId),
    add foreign key (titleId) references title(titleId)
    #add constraint dueDate_inFuture
	#	check (duedate > curdate())
        ;
        
#https://stackoverflow.com/questions/55204218/how-to-use-curdate-in-check-clause
-- CREATE TRIGGER dueDate_inFuture_trg
-- 	BEFORE INSERT ON rental
-- 	FOR EACH ROW
-- 	BEGIN
-- 	IF NEW.duedate <= CURDATE()  THEN
-- 			SIGNAL SQLSTATE '45000'
-- 			SET MESSAGE_TEXT = 'Invalid date!';
-- 	END IF;
-- 	END;

alter table checkin
	add foreign key (custId) references cust(custId),
    add foreign key (rentalId) references rental(rentalId),
    add foreign key (copyId) references copy(copyId)
    ;

alter table cust
	add constraint EmailId_like_ptrn
		check (custEmailId like "_%@_%._%")
        ;
########################################################
# insert initial data
########################################################
insert into cust (custName, custPhone, custEmailId)
	values 	("Hiro Protagonist", 555987987, "deliverator95512@enzo.pizza"),
			("Molly Millions", 678978955, "rzrgrl_pow6@merc.list"),
			("Rick Deckard", 12132523, "rdeckard@lapd.gov")
            ;
insert into title (Titlename, author, titleYear)
	values  ("Snow Crash", "Neal Stephenson", 1992),
            ("Neuromancer", "William Gibson", 1984),
            ("Do Androids Dream of Electric Sheep?", "Philip K. Dick", 1968)
            ;
insert into copy(titleId, copyCondition, acquiredDate, checkedIn)
	values  (1, "mint", "2021-01-01", True),
			(2, "mint", "2021-01-01", True),
            (3, "mint", "2021-01-01", True)
            ;