def main():

    age=eval(input("enter your age: "))
    cit=eval(input("How long have you been a US citizen? "))

    if age>=30 and cit>=9:
        print("You are eligible to be a senator.")

    if age>=25 and cit>=7:
        print("You are eligible to be a representative.")

main()
