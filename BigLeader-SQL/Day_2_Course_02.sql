use my_testdb;
create table temp_1 (
	no int default 9999,
    name char(10) default 'AAA',
    birthday date default '2001-01-01') ;
    
select * from tmp_1;
select * from temp_1;

insert into temp_1(no) values(1);
alter table temp_1
add column tel varchar(40) default '010-1111-2222';
alter table temp_1 
modify column tel varchar(50);
alter table temp_1
change column tel phone varchar(40);
select * from temp_1;

-- 다른 테이블 복사해서 만들기
create table temp_2
as
select * from emp3
where sal < 1500;

select * from temp_2;

-- 데이터 필드만 복사하기 (1) (데이터나 인덱스 등의 정보는 가져올 수 없다.)
create table temp_3
as 
select * from emp3
where 1= 2;

select * from temp_3;
alter table temp_3
drop column sal;

-- 데이터 필드 복사하기 (2) (데이터, 인덱스도 가져온다.)
create table temp_4 like emp3;
select * from temp_4;

-- 테이블 생성 후 데이터 입력하기 
create table temp_8(
no int default 9999,
name varchar(10) default 'aaa',
birth datetime default current_timestamp);

insert into temp_8(no, name, birth)
values(1, '홍길동', '1975-10-23');

select * from temp_8;

insert into temp_8 values(2, '전우치', '1982-07-15');
insert into temp_8 (no, name) values(3, '강감찬');

-- 다른 테이블의 데이터 복사해서 입력하기
create table temp_9 
as 
select * from emp3
where 1= 2;

insert into temp_9
select * from emp3
where sal <= 1500;

select * from temp_9;


set sql_safe_updates = 0; 

-- 값 갱신하기
update temp_9
set sal = sal * 1.5
where sal >= 1000;

select * from temp_9;

-- 값 삭제하기
select * from temp_9
order by hiredate;

delete from temp_9
where hiredate > '1982-01-01';