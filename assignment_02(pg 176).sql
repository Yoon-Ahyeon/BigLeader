-- 1번
select * from student;
select * from professor;

select 학생.name as '학생이름', 교수.name as '지도교수이름'
from student 학생, professor 교수
where 학생.profno = 교수.profno;

select 학생.name as '학생이름', 교수.name as '지도교수이름'
from student 학생 join professor 교수
on 학생.profno = 교수.profno;

-- 2번
select * from customer3; -- cno/ cname
select * from product3; -- pno / pname
select * from sales3; -- qty / pno / cno

select 고객.cname as '고객이름', 제품.pname as '제품이름', 판매.qty as '구입수량'
from customer3 고객, product3 제품, sales3 판매
where 고객.cno = 판매.cno
and 판매.pno = 제품.pno;

select 고객.cname as '고객이름', 제품.pname as '제품이름', 판매.qty as '구입수량'
from customer3 고객 join sales3 판매
on 고객.cno = 판매.cno
join product3 제품
on 판매.pno = 제품.pno;

-- 3번
select 고객.cname as '고객이름', 제품.pname as '제품이름', 판매.qty as '구입수량'
from customer3 고객, product3 제품, sales3 판매
where 고객.cno = 판매.cno
and 판매.pno = 제품.pno
and 제품.pname = 'apple';

select 고객.cname as '고객이름', 제품.pname as '제품이름', 판매.qty as '구입수량'
from customer3 고객 join sales3 판매
on 고객.cno = 판매.cno
join product3 제품
on 판매.pno = 제품.pno
where 제품.pname = 'apple';
