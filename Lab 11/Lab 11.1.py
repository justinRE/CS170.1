def main():
    limit = eval(input("Enter the speed limit: "))
    clocked = eval(input("Enter the speed that was clocked: "))
    if(clocked <= limit):
        print("The speed clocked is a legal speed")
    elif(clocked > limit and clocked < 90):
        fine = 50 + (clocked - limit) * 5
        print("Your fine is $",fine)
    else:
        fine = 250 + (clocked - limit) * 5
        print("Your fine is $",fine)
main()
                 
