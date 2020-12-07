-- Display the user information along with the total money spent by each user. sort the result by the money spent descending. 
--    note: If the user didn't provide mobileno, or emailid, display '-' instead of null. 
--          If the user hasn't spent any money yet, display 0 instead of null in the spent column
#Emy Kay

select userId, sum(seatFare*noOfSeats) 
	from users
	natural join 
        (select * from booking natural join 
            (select * from bookingDetail natural join seatType) 
                as fullBookingDetail) 
                as usersFullBookingDetail
	where usersFullBookingDetail.userId = users.userId
    group by users.userId
    ;
    