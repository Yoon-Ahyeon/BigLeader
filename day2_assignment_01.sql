-- 1번 문제

create table customer4 (
no int,
name varchar(30) default 'AAA',
tel varchar(15) default '1111',
email varchar(100) default 'abc@def.net'
);

select * from customer4;

-- 문제 2번
insert customer4 values ('2022001', '서진수', '02)111-2222', 'seojinsu@gmail.com');
insert customer4 values ('2022002', '손기동', '031)234-5678', 'skdong@daum.net');
insert customer4 values ('2022003', '정진교', '055)233-4678', 'jjk12345@naver.com');
insert customer4 values ('2022004', '홍길동', '054)4567-0987', 'hongkd1234@gmail.com');
insert customer4 values ('2022005', '일지매', '053)2233-4455', 'onejm2222@daum.net');

-- 문제 3번
create table customer5
as
select name, tel
from customer4;

select * from customer5;

-- 문제 4번
alter table customer5
add column birth varchar(20) default '9999-12-31';

select * from customer5;