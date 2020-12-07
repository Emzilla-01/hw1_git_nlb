1.	Display unique Jobs from table 

select distinct(job) from emp;

2.	List the emps name, job  who are with out manager

select ename, job from emp 
    where mgr is NULL;


3.	List the emps in the asc order of their Salaries 

select empno, ename from emp
    order by sal asc;

4.	List the emps in the asc order of Designations of those joined after the second half of 1981

select empno, ename from emp
    where hire_date > '1981-07-02'
    order by job asc;


5.	List the details of the emps in asc order of the sal and desc of Jobs 

select * from emp
    order by sal asc, job desc;

6.	Display all the unique job groups in the descending order 

select distinct(job) from emp
    order by job desc;

7.	Find the total sal given to the MGR

select ename, empno, sal+comm as "Total sal"
	from emp
    where job="MANAGER";

8.	Display the average salaries of all the clerks

select avg(sal) 
	from emp
    where job="CLERK";

9.	List the emps who are either ‘CLERK’ or ‘ANALYST’ in the Desc order

select empno, ename, job from emp 
    where job in ("CLERK", "ANALYST")
    order by empno DESC;

10.	List the emps who joined on ,3-DEC-81,17-DEC-81, in asc order of seniority and salary

select empno, ename from emp
    where hiredate between "1981-12-03" and "1981-12-17"
    order by hiredate asc, sal desc;

11.	List the Enames those are having five characters in their Names

select ename from emp 
    where length(ename) =5;

12.	List the Enames those are starting with ‘S’ and with five characters

select ename from emp 
    where substring(ename, 1,1)="S"
        and length(ename) =5;

13.	List the emps those are having four chars and third character must be ‘R’

select ename from emp 
    where substring(ename, 3,1)="R"
        and length(ename) =4;

14.	List the five character names starting with ‘S’ and ending with ‘H’

select ename from emp 
    where substring(ename, 1,1)="S"
	  and substring(ename, 5,1)="H"
        and length(ename) =5;

15.	List the emps whose Sal is four-digit number ending with Zero

select empno, ename, sal from emp 
    where substring(sal, 4,1)="0"
        and length(sal) = 4;

16.	List all the emps except ‘PRESIDENT’ & ‘MGR” in asc order of Salaries
select empno, sal
	from emp
    where job not in ("MANAGER", "PRESIDENT")
    order by sal asc;

17.	List the total information of table along with DNAME and Loc of all the
emps Working Under ‘ACCOUNTING’ & ‘RESEARCH’ in the asc Deptno

select *
	from emp natural join dept
    where dname in ("ACCOUNTING", "RESEARCH")
    order by dept.deptno;


18.	Find the highest sal of table

select max(sal) 
    from emp

19.	Find the total annual sal to distribute job wise in the year 81

# Without some additional assumption/s we cannot answer this question.
# Assuming that sal has not changed since hiredate.
# Additionally this answer should be considered maximal since I dont yet have a function to calculate sal paid according to date of join.

# ie: CLARK joins '1981-06-09', he is paid since then to the end of the year, but CLARK`s SAL is monthly, so we would need some way to count each pay period since his join. Is it 12-6= ~6 months, 6 months * 2450 SAL = total 1981 pay? SAL is described as monthly, but does CLARK receive the full month`s pay for joining on June 9th, or is it decremented like 30-9 days->21/30==.7 -> .7*2450SAL = CLARK`s pay for that month?

#I can implement these business rules in Python but not yet in SQL :/

#naive answer
select job, sum(sal)
	from emp
    where hiredate between "1901-01-01" and "1981-12-31"
    group by job;



20.	Display the average salaries of all the clerks
#repeat of question 8?
select avg(sal)
	from emp
    where job = "CLERK"; 


21.	Display the number of employee  for each job group deptno wise

select job, count(empno), deptno
	from emp
    group by job, deptno;

22.	List the manage rno and the number of employees working for those mgrs in the
ascending Mgrno

select mgr, count(empno) as "Direct Reports"
	from emp
    group by mgr
    order by mgr asc;

23.	List the department,details where at least two emps are working

select * from 
	(select emp.deptno, count(emp.deptno) as hc 
		from emp natural join dept
		group by emp.deptno) as deptcounts natural join dept
        where hc>=2;


24.	List the employees whose salary is more than 3000 after giving 20% increment

select empno, sal, sal*1.2 as "incremented sal"
	from emp
    where sal*1.2 > 3000;
 

25.	List the emps whose sal is greater than his managers salary

select a.empno, a.sal as emp_sal, a.mgr, b.sal as mgr_sal
	from emp a inner join emp b 
		on a.mgr=b.empno
    where a.sal > b.sal;


26.	List the no. of emps in each department where the no. is more than 3

select * from 
	(select emp.deptno, count(emp.deptno) as hc 
		from emp natural join dept
		group by emp.deptno) as deptcounts natural join dept
        where hc>3;


27.	List the emps who joined in the month of which second character is ‘a’

select empno, monthname(hiredate), hiredate 
	from emp
    where substring(monthname(hiredate),2,1)="a";


28.	List the emps those who joined in 80’s

select empno, year(hiredate), hiredate 
	from emp
    where year(hiredate) between 1979 and 1990;

29.	List all the emps who joined before or after 1981

select empno, year(hiredate), hiredate 
	from emp
    where year(hiredate) != 1981;

30.	List the emps who joined in any year but not belongs to the month of March

select empno, monthname(hiredate), hiredate 
	from emp
    where monthname(hiredate) != "March";


31.	List the emps of Deptno 30 or 10 joined in the year 1981

select empno, year(hiredate), deptno 
	from emp
    where year(hiredate) = 1981 and
    deptno in (10, 30);

32.	List the Emps who are senior to their own MGRS

select a.empno, a.hiredate as emp_hiredate, a.mgr, b.hiredate as mgr_hiredate
	from emp a inner join emp b 
		on a.mgr=b.empno
    where a.hiredate < b.hiredate;


33.	List the Enames who are retiring after the max Job period is 20Y by end of 1989
#Find all people who are hired before the end of 1989 and didn`t retire be

select ename, hiredate, datediff(curdate(), hiredate)/365.2422 as "tenure"
	from emp
    where (datediff(curdate(), hiredate)/365.2422) > 20


34.	List the emps who joined in the month of DECEMBER

select empno, month(hiredate)
	from emp
    where month(hiredate) != 12;

35.	List the emps whose first 2 chars from Hiredate=last 2 characters of Salary

select empno, hiredate, sal
	from emp
    where substring(hiredate, 1,2) = substring(sal, -2);

