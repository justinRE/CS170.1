def main():

    fName= input("enter the file name:")

    inFile=open(fName,"r")

    sum=0
    count=0

    line=inFile.readline()

    while line !="":

        for xStr in line.split(","):

            sum= sum+ float(xStr)
            count=count+1

        line= inFile.readline()

    print("The average is:", sum/count)


main()
