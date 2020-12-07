use `assignment_11-30-2020`;
#use `morning_12-1-2020`;
select * from emp;
# 1.	List the details of the emps whose Salaries more than the employee BLAKE
select * from emp
	where sal > (select sal from emp
				where ename="BLAKE");
# 2.	List the emps whose Jobs are same as ALLEN 
select * from emp
	where job = (select job from emp
				where ename="ALLEN");
# 3.	List the emps who are senior to King 
select * from emp
	where hiredate < (select hiredate from emp
						where ename ="KING");
# 4.	List the Emps of Deptno 20 whose Jobs are same as Deptno10
select *  from emp
	where deptno = 20 
		and job in (select distinct(job) from emp 
					where deptno=10);
                    
# 5.	List the Emps whose Sal is greater or equals to SMITH in desc order of Sal 
# There is no SMITH in this dataset? using SCOTT as ename
select * from emp
	where sal > (select sal from emp
				where ename="SCOTT");

# 6.	Find the total annual sal to distribute job wise in the year 81
# employee wise
#select empno, job, sal, timestampdiff(month, hiredate, "1981-12-31") as 'Pay periods this year (months)', sal*timestampdiff(month, hiredate, "1981-12-31") as 'Approx. annual pay (upper limit)'
#    from emp
#    where hiredate between "1980-12-31" and "1981-12-31";

# job wise
select job, sum(annual_sal) from 
	(select empno, job, sal, timestampdiff(month, hiredate, "1981-12-31") as 'Pay periods this year (months)', sal*timestampdiff(month, hiredate, "1981-12-31") as 'annual_sal'
		from emp
		where hiredate between "1980-12-31" and "1981-12-31") as annual_sal_tbl
	group by job; 


# 7.	List the Empno, Ename, Sal, Dname, Grade, Exp, and Ann Sal of emps working for Dept10 or20
# Empno, Ename, Sal, Dname, 
#Grade,	# select grade from salgrade where "2450" between losal and hisal;
#Exp, 	# datediff(curdate(), hiredate)/365.2422 as "tenure"

#Ann Sal # sal*12
select empno, ename, sal, dname, 
		(select grade from salgrade where sal between losal and hisal) as grade,
		datediff(curdate(), hiredate)/365.2422 as "Tenure", 
        sal*12 as "Ann Sal"
 from emp natural join dept
	where deptno in (10, 20);
 
# 8.	List jobs of deptno 10 those that are not found in deptno 20
select distinct(job) from emp 
	where job not in (select distinct(job) from emp
						where deptno=20)
	and deptno=10;
# 9.	Find details of highest paid employee
select * 
	from emp
	where sal = (select max(sal) from emp);
    
# 10.	Find the highest paid employee of sales department
select * from emp 
	where sal = (select max(sal) 
				from emp 
				where deptno = (select deptno 
								from dept 
                                where dname = "SALES"));
# 11.	Display total sal employee belonging to grade 3
select sum(sal) from
	(select empno, sal, 
    (select grade from salgrade where sal between losal and hisal) as grade
	from emp) as this;
# 12.	List the employees  whose sal is >the average sal of emps
select * from emp 
	where sal > (select avg(sal) from emp);

# 13.	Display the Grade, Number of emps, and max sal of each grade
select grade, count(empno), max(sal)
	from (
		select empno, sal, (select grade 
							from salgrade 
                            where sal between losal and hisal) as grade
		from emp) as this
    group by grade;
######################
# 14.	Display dname, grade, No. of emps where at least two emps are clerks
drop view if exists clerks_per_dept;
create view clerks_per_dept as
	select deptno, count(distinct(empno)) as clerk_count
		from emp
		where job="CLERK"
		group by deptno
        ;
create view dept_where_gte_two_clerks as
	select deptno
		from clerks_per_dept
		where clerk_count = (select max(clerk_count) as clerk_max from clerks_per_dept)
		;
select dname, (select grade 
							from salgrade 
                            where sal between losal and hisal) as grade,
				(select count(empno)
                from emp where deptno = (select deptno 
										from dept_where_gte_two_clerks))
										as no_of_emps_in_dept
	from emp natural join dept 
		where deptno = (select deptno 
						from dept_where_gte_two_clerks)
                        ;
# 15.	List the emps whose sal is equal to the average of max and minimum
select * from emp 
		where sal = (select (max(sal)+min(sal))/2 
							from emp);
# 16.	List the emps who joined in the company on the same date
drop view if exists hiredate_cohorts;
create view hiredate_cohorts as
	select * 
    from (select hiredate, count(hiredate) as ttl
		from emp 
		group by hiredate) as this
	where ttl >1
        ;
select * from emp 
	where hiredate in (select hiredate 
						from hiredate_cohorts);
# 17.	List the grades 3 emps of research and operations depts.. joined after 1987 and
# whose names should not be either miller or allen
select * from emp natural join dept
	where dname in ("RESEARCH", "OPERATIONS") #no dname OPERATIONS dept in dataset
    and ename not in ("MILLER", "ALLEN")
    and hiredate > "1987-12-31" #no hiredate > 1987 in dataset
    and sal between 
		(select losal from salgrade where grade=3) and 
        (select hisal from salgrade where grade=3); 
# 18.	List the highest paid emp of joined before the most  recently hired emp
# of grade 2
select * from emp
    where sal between 
		(select losal from salgrade where grade=2) and 
        (select hisal from salgrade where grade=2); 

# 19.	List the name, job, dname ,sal, grade dept wise
# 20.	List the emps who joined in any year but not belongs to the month of March
# 21.	List the emps Whose Jobs are same as MILLER or Sal is more than ALLEN 
# 22.	List the Emps whose Sal is > the total remuneration of the SALESMAN 
# 23.	List the Empno, Ename, Sal, Dname of all the ‘MGRS’ and ‘ANALYST’
# 24.	 working in , with an exp more than 7 years without receiving the  Comm asc order of               location
# 25.	Display the Empno, Ename, Sal, Dname, Loc, Deptno, Job of all emps working at  CHICAGO or working for ACCOUNTING dept with Ann Sal>28000, but the Sal should not be=3000 or 2800 who doesn’t belongs to the Mgr and whose no is having a digit ‘7’ or ‘8’ in 3 rd position in the asc order of Deptno and desc order of job
# 26.	List the Emps of Grade 3,4 belongs to the dept ACCOUNTING and RESEARCH
# whose Sal is more than ALLEN and exp more than SMITH in the asc order of
# EXP 

# 27.	List all the information of emp with Loc and the Grade of all the emps belong to
# the Grade range from 2 to 4 working at the Dept those are not starting with char
# set ‘OP’ and not ending with ‘S’ with the designation having a char ‘a’ any where
# joined in the year 1981 but not in the month of Mar or Sep and Sal not end with
# ‘00’ in the asc order of Grades
# 28.	List the most recently hired emp of grade3 belongs to  location 
# 29.	List the most senior empl working under the king and grade is more  than 3
# 30.	List the details of the department where maximum number of emps are working
# 31.	List the emp name, job, sal, grade and dname except clerks and sort on the basis
# of highest sal
# 32.	List the names of the emps who are getting the highest sal dept wise 
# 33.	List the managers whose sal is more than his employees avg salary 
# 34.	List the name, salary, comm. For those employees whose net pay is greater than
# or equal to any other employee salary of the company
# 35.	Find out least 5 earners of the company 
# 36.	List the Enames who are retiring after the max Job period is 20Y
# 37.	List THE Name of dept where highest no. of emps are working
# 38.	Display the manager who is having maximum number of employees working under him?
# 39.	Count the No. of emps who are working as ‘Managers’(using set option)
# 40.	List the Managers name who is having max no. of emps working under him
