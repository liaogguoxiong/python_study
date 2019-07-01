import  pymysql

for i in range(1,13):
    start_time="2018-{M}-01  00:00:00 ".format(M=i)
    end_time="2018-{M}-31 23:59:59".format(M=i)
    # print(start_time,end_time)
    sql='''SELECT COUNT(*) FROM invoice_info WHERE nsrsbh='91440300MA5DRNEM7D' AND kprq BETWEEN '{s_time}' AND '{e_time}' '''.format(s_time=start_time,e_time=end_time)
    db=pymysql.connect(host='192.168.20.40',user='root',password='A_isino#888',port=3306,db='dzfp_zzs_kpfw_arm')
    cursor=db.cursor()
    cursor.execute(sql)
    date=cursor.fetchone()
    print(date)
    db.close()
    # print(sql)
