-- 부모테이블 만들기 
CREATE TABLE dept4(
deptno int primary key,
dname varchar(10) not null,
loc varchar(10) not null);

insert into dept4 values (10, "총무부", "3F");
insert into dept4 values (20, "생산부", "1F");
insert into dept4 values (30, "영업부", "2F");
commit;

select * from dept4;

-- 자식테이블 만들기
CREATE TABLE emp4(
empno int primary key,
ename varchar(20) not null,
deptno int,
foreign key (deptno) references dept4(deptno) );

insert into emp4 values (1001, '서진수', '10');
insert into emp4 values (1002, '일지매', '20');
insert into emp4 values (1003, '전우치', '30');
-- insert into emp4 values (1004, '강감찬', '40'); #참조무결성 조건 위반으로 에러 발생

select * from emp4;


-- 뷰 만들기

-- 단순 뷰
Create or replace view vemp
as
select empno, ename, deptno
from emp3
where deptno in(10, 20);

select * from vemp;

-- 복합 뷰
create or replace view vemp3
as
select e.ename, d.dname, e.deptno
from emp3 e, dept3 d
where e.deptno = d.deptno
and e.deptno = 10;
select * from vemp3;

