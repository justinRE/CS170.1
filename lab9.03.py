def main():

    xStr= input("Please enter a value or press enter to quit:")
    sum=0
    count=0

    while xStr != "":
        sum=sum+eval(xStr)
        count=count+1
        xStr= input("Enter a value or press enter to quit:")

    print("the average is:", sum/count)

main()
