#app array
lt=[]
n=int(input("enter  array size:"))
for i in size(0,n):
    ele=int(input("enter elements:"))
    lt.append(ele)
print(lt)
op=int(input("enter operation(1.insert 2.delete 3.search 4.sort 5.exit"))
if (op==1):
    x=int(input("how many nos to be inserted:"))
    for i in range(0,x):
        e=int(input("enter elements":))
        lt.append(e)
    print(lt)
elif (op==2):
    y=int(input("element to be deleted"))
    lt.remove(y)
    print(lt)
elif (op==3):
    z=int(input("enter element to be searched:"))
    if z in lt:
        print(lt.index(z))
else:
    print("not found")
    



