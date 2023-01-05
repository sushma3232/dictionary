
# write the sum of the list from the dictionary

# d={"a":[4,8,6],"b":[4,1],"c":[8,3]}
# for i in d:
#     g=d[i]
#     l=[]
#     sum=0
#     j=0
#     while j<len(g):
#         sum=sum+g[j]
#         j+=1
#     l.append(sum)
#     d[i]=l
# print(d)


# # for loop:
# d={"a":[4,8,6],"b":[4,1],"c":[8,3]}
# for i in d:
#     sum=0
#     for j in d[i]:
#         sum+=j
#     d[i]=[sum]
# print(d)


a={"a":2 ,"b":3,"c":4}
b=a.keys()
i=0
while i<len(a):
    if b in a:
        print(b[0])
    i=i+1