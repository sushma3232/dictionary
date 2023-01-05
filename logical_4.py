
    
    
a={"a":1,"b":2,"c":3}
n=input("enter the alp")
b=list(a.keys())
i=0
while i<len(a):
      if n in b[i]:
          print(b[i])
      i=i+1




a={'a':10,'b':10,'c':12}
b=list(a.keys())
print(b[-1])




a={"a":1,"b":2,"c":3}
n=input("enter the alp")
if n in a:
    print(n)
else:
    print("key not present")
    




# a=[12,45,69,78]  
# b=[]
# i=0
# while i<len(a):
#       r=a[i]%10
#       c=a[i]//10
#       b.append(r+c)
#       i=i+1
# print(b)


# a="sai"
# a+="jyothi"
# print(a)