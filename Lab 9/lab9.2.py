def main():

    credit= eval(input("Enter your credit hours: "))

    if credit>=26:
        print("You are a Senior")

    elif credit>=16:
        print("You are a Junior")

    elif credit>=7:
        print("You are a Sophomore")
        
    elif credit<7:
        print("You are a Freshman")


main()
