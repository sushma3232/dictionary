Dic= {
1: 'NAVGURUKUL',
2: 'IN',  
3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}
}
for i in Dic:
    if i==3:
       del Dic[3]['A']
print(Dic) 