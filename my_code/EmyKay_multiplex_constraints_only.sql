####################
# Submission from Emy Kay
# Excerpt from multiplex_init.sql
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