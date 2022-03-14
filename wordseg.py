import jieba
f=open("data/20220314.txt","r",encoding='utf8')
w=open("output/20220314_result.txt","w",encoding='utf8')
con=f.readlines()
for line in con:
    res=jieba.cut(line)
    res=" ".join(res)
    w.write(res)
f.close()
w.close()
print("okk")