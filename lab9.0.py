def main():
    
    n= eval(input("How many items do you want to calculate: "))
    sum=0
    
    for i in range (n):

        num= eval(input("Enter a value: "))
        sum= sum+num
    print(("The average is: "), sum/num)

main()
