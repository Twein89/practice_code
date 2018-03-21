/*
create table table_name (col ..)
partitioned by (key type)
*/

create table emp
(name string,
salary bigint)
partitioned by (dt string)
row format delimited fields terminated by ','
lines terminated by '\n'
stored as textfile;

# desc formatted emp;
# show partitions emp; 查看分区

# 加分区
alter table emp add if not exists
partition(dt='2017-01-01');

# hadoop fs -ls /user/hive/warehouse/twein_test.db/emp

# load data local inpath '/tmp/a.txt' into table emp partition(dt='2017-01-01')

select * from emp;
select dt from emp;

/*动态分区
在写入数据时自动创建分区(包括目录结构)*/

create table emp_2
(name string,
salary bigint)
partitioned by (dt string)
row format delimited fields terminated by ','
lines terminated by '\n'
stored as textfile;

insert into table emp_2 partition(dt)
select name, salary, dt
from emp;

set hive.exec.dynamic.partition.mode=nonstrict;
