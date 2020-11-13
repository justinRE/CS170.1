def main():
    
    sum=0
    count=0

    moredata="yes"

#0 is the first index in the character string of 'yes' y=0 e=1 etc. 
    while moredata[0]=="y":

        num=eval(input("Enter a value: "))
        sum= sum+num
        count= count+1

        moredata=input("Do you still have data yes or No: ")

    print("The average is: ", sum/count)

main()
