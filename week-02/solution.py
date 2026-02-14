def substrings(s):
    count=0
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    
    for k in freq.values():
        count+=k*(k+1)//2
        
    return count

s=input("Enter a substring:")
print("no. of contiguous substrings starting and ending with same letter are",substrings(s))