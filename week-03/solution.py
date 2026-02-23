n=int(input())
arr=list(map(int,input().split()))

even,odd=0,0

for i in arr:
    if i%2==0:
        even+=1

odd=n-even

print(even,odd)
