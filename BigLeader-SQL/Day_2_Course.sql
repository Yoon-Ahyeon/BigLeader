select deptno, sum(pay), max(pay), min(pay)
from professor
group by deptno;

select deptno, position,sum(pay), max(pay), min(pay)
from professor
where year(hiredate) > 1990
group by deptno, position ;

-- having절
select deptno, count(deptno), sum(pay),max(pay), min(pay)
from professor
group by deptno
having count(deptno) >= 2; -- group by: where절 대신에 having절을 사용한다.

-- rollup(1)
select deptno, count(deptno), sum(pay), max(pay), min(pay)
from professor
group by deptno
with rollup; -- 밑에 총계가 같이 나온다. 

-- rollup(2)
select deptno, position, count(deptno), sum(pay), max(pay), min(pay)
from professor
where deptno in (101, 102, 103) -- 각 deptno 별로 총계도 같이 나온다 
group by deptno, position
with rollup;

select max(if(day = 'SUN', dayno, NULL)) "SUN",
max(if(day = 'MON', dayno, NULL)) "MON",
max(if(day = 'TUE', dayno, NULL)) "TUE",
max(if(day = 'WED', dayno, NULL)) "WED",
max(if(day = 'THU', dayno, NULL)) "THU",
max(if(day = 'FRI', dayno, NULL)) "FRI",
max(if(day = 'SAT', dayno, NULL)) "SAT"
from cal
group by weekno
order by weekno;

select ename, sal, rank() over (order by sal desc) "급여순위"
from emp3;

-- 등수는 무조건 1-10까지 순서대로 존재한다. 
select ename, sal, dense_rank() over (order by sal desc) "급여순위"
from emp3;

select *
from (select ename, sal, dense_rank() over (order by sal desc) as "급여순위"from emp3) 순위
where 순위.급여순위 = 5;

#학부에 따라 순위를 측정한다. 
select empno, ename, sal, deptno,
dense_rank() over (partition by deptno order by sal desc) "급여순위"
from emp3;

-- 누적 합계 
select empno, ename, sal, sum(sal) over(order by sal)"급여 누적합계"
from emp3;

-- partiotion by를 활용한 누적 합계율
select empno, ename, deptno, sal, sum(sal) over(partition by deptno order by sal)"급여 누적합계"
from emp3;

-- join하기
-- Equal join
select e.ename '사원이름', d.dname '부서이름'
from emp3 e join dept3 d
on e.deptno = d.deptno;

select * from emp3;
select * from dept3;

-- 3개의 테이블 조인 (1)
select 부서.dname, 학생.name as '학생성명', 교수.name as '교수성명'
from department 부서, student 학생, professor 교수
where 부서.deptno = 학생.deptno1
and 학생.profno = 교수.profno;

-- 3개의 테이블 조인 (2)
select 부서.dname, 학생.name as '학생성명', 교수.name as '교수성명'
from department 부서 join student 학생
on 부서.deptno = 학생.deptno1
join  professor 교수
on 학생.profno = 교수.profno;

-- 조인 및 검색 (1)
select s.name '학생이름', p.name '지도교수이름'
from student s, professor p
where s.profno = p.profno
and s.deptno1 = 101;

-- 조인 및 검색 (2)
select s.name '학생이름', p.name '지도교수이름'
from student s join professor p
on s.profno = p.profno
where s.deptno1 = 101;

