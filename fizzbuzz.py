#check the number, fizbuzz - if the number is divisible by 3 and 5 | fizz- if the number is divisible by 3 | Buzz- if the number is divisible by 5
class FizzBuss:
    def generate(self,n):
        array=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                array.append("fizzbuss")
            elif i%3==0:
                array.append("fizz")
            elif i%5==0:
                array.append("Buzz")
            else:
                array.append(i)
        return array

obj=FizzBuss()
n=int(input("Enter your number"))
print(obj.generate(n))





