create table test
(id int,
name string,
age string,
tel string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


create table test_2
(id int, 
name string,
tel string)
partitioned by (age int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;


create table test_3
(id int,
name string);


from test
insert into table test_2
partition(age)
select id, name, tel, age
insert into table test_3
select id, name
where id>3;


# 导出到本地
insert overwrite local directory '/tmp/test'
select * from test;


# 导出时指定分隔符
insert overwrite local directory '/tmp/test'
row format delimited
fields terminated by ','
select * from test;
