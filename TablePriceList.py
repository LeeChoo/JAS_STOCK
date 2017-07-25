#Create table Pricelist in Mysql

import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd="", db='stock', charset="utf8", cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = """create table Pricelist(time datetime, ma_ck_a char(20) not null, TC_b int not null, tran_c int not null, san_d int not null, giamua3_e int, klmua3_f int, giamua2_g int, klmua2_h int, giamua1_i int, klmua1_j int, tl_k int, giakhop_l int, klkhop_m int, tongkl_n int, giaban1_o int, klban1_p int, giaban2_q int, klban2_r int, giaban3_s int, klban3_t int, tb int, ts int, u int, giacao_v int, giathap_w int, DTNNmua_x int, y int, z int)"""

cursor.execute(sql)
connection.commit()
connection.close()