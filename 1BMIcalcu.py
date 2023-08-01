
def greetings():
    print(f"good morning")
    print("Hello",Name)
    print("This program will give your BMI index ")
    


def BMI():
    weight=float(input("Enter your weight in kgs \n"))
    height=float(input("Enter your height in meter \n"))
    bmi=weight/height**2
    print(bmi)

Name=input("Enter Your Name \n")
greetings()
BMI()
