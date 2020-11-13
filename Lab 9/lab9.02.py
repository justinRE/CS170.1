def main():
    num= eval(input("Enter a value or enter negative value to quit"))

    sum=0
    count=0

    while num >=0:

        sum=sum+ num
        count= count+1
        num= eval(input("enter a value or enter negative value to quit: "))

    print("the average is:", sum/count)

main()
