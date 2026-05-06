def smallerNumberThanCurrent(N):
    ans=[]
    for i in N:
        count=0
        for j in N:
            if i>j:
                count+=1
        ans.append(count)
                
    return ans
            
# Taking input from user:
# input() -> takes whole line as string
# split() -> breaks string into list based on spaces
# map(int, ...) -> converts each element into integer

N=list(map(int,input("Enter your number").split())) 
print(smallerNumberThanCurrent(N))
