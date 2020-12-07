# 25.List the emps whose sal is greater than his managers salary
# Extra credit: do not use self join.
# Nested query only version Emy Kay 
select empno
	from emp
	where sal > (select mgr_sal from     
                    (select empno as mgr_no, sal as mgr_sal
                        from emp where empno in 
                        (select distinct(mgr from emp))
                            as mgrs #table alias inner?
                            where mgr_no = mgr) # filter?
                            ;