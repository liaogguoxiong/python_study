#Program：字符串与字节包相互转化
#History：lgx    2018-10-16      First release
msg="我是大粑粑"
print(msg)
msg_bytes=msg.encode('utf-8') #python3默认字符,字节都为Unicode
print(msg_bytes)
print(msg_bytes.decode('utf-8')) #解码