low=2
high=100

print("prime number between",low ,"and",high,"are:")

for num in range(low,high):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
