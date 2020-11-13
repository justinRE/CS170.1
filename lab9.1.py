def main():

    score=eval(input("Input your score as a number: "))

    if score>=5:
        print("You got a A")

    elif score>=4:
        print("You got a B")

    elif score>=3:
        print("You got a C")
        
    elif score>=2:
        print("You got a D")
        
    elif score<=1:
        print("You got a F")

main()
