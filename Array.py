from array import*
arr = array('i',[])
n = int(input("Enter the array length"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)
print(arr,end=" ")
print()


val = int(input("Enter search"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1
else:
    print("Out of range")
