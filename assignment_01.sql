select * from professor;

-- 1번 
select profno as '교수번호' , name as '교수이름', id as 'ID' from professor 
where id like 'A%' 
or id like 'B%' 
or id like 'C%' 
or id like 'D%' 
or id like'E%' 
or id like 'F%' 
or id like 'G%';

-- 2번 
select profno as '교수번호', name as '교수이름', deptno as '학과번호' from professor where deptno In (101, 102);

-- 3번 
select profno as '교수번호', name as '교수이름', hpage as '홈페이지주소' from professor where hpage is not null;

-- 4번 
select profno as '교수번호', name as '교수이름', deptno as '학과번호', bonus as 'BONUS' from professor
where deptno in (101, 102) and bonus is not null;

-- 5번 
select studno as '번호', name as '이름', deptno1 as '학과번호'from student 
union all
select profno, name, deptno from professor