-- Display the user information along with the total money spent by each user. sort the result by the money spent descending. 
--    note: If the user didn't provide mobileno, or emailid, display '-' instead of null. 
--          If the user hasn't spent any money yet, display 0 instead of null in the spent column
#Emy Kay
use multiplex_db;
select * from users;
select usersFullBookingDetail.userId, userName, userType, coalesce(sum(seatFare*noOfSeats), 0) as money_spend, coalesce(mobileNo, '-') as mobileNo, coalesce(emailId, '-') as emailId
	from users
	left outer join 
        (select * from booking natural join 
            (select * from bookingDetail natural join seatType) 
                as fullBookingDetail) 
                as usersFullBookingDetail
	where usersFullBookingDetail.userId = users.userId
    group by emailId
    order by money_spend desc
    ;
