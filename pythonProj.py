import random
a=(random.sample(range(1,100),1))
print("Selected number is",a)

for i in a:
    if i%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

for i in a:
    if i>0:
        print("It is a positive number")
    else:
        print("It is a negative number")

for i in a:
    if i==1:
        print("It is neither prime nor composite")
    else:
        for divisor in range(2,(i//2)+1):
            if i%divisor == 0:
                print("It is a composite number")
                break
        else:
            print("It is a prime number")
