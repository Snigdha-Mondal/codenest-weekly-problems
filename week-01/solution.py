arr=list(map(int,input("Enter the numbers seperated by space: ").split()))
length=len(arr)
expected_sum=length*(length+1)//2
actual_sum=sum(arr)
missing_num=expected_sum-actual_sum
print("Missing number is ",missing_num)