import jieba
f=open("20220309.txt","r",encoding='utf8')
w=open("20220309_result.txt","w",encoding='utf8')
con=f.readlines()
for line in con:
    res=jieba.cut(line)
    res=" ".join(res)
    w.write(res)
f.close()
w.close()
print("okk")