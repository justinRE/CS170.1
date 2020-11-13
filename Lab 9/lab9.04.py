def main():

    fileName= input("enter a file name:")
    inFile= open(fileName,"r")

    sum=0
    count=0

    for line in inFile:

        sum= sum+float(line)
        count= count+1

    print("The average is:", sum/count)

main()
