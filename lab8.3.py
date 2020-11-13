def sumN(n):

    sum=0

    for num in range(1,n+1):
        sum= sum+num

    return sum

def sumNCubes(n):

    total=0

    for i in range(1,n+1):
        total= total+ i**3

    return total

def test():

    n= eval(input("Please enter a number"))

    print("The sum of the first ", n," natural numbers is: ", sumN(n))

    print("The sum of the cubes of the first ", n," natural numbers is: ", sumNCubes(n))
test()
