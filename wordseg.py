import jieba
f=open("data/20220313.txt","r",encoding='utf8')
w=open("output/20220313_result.txt","w",encoding='utf8')
con=f.readlines()
for line in con:
    res=jieba.cut(line)
    res=" ".join(res)
    w.write(res)
f.close()
w.close()
print("okk")