import turtle

screen = turtle.Screen()
screen.title("State Name Game")
screen.setup(width=1000, height=800)
kerala_image = "Kerala_profile_map.gif"
screen.addshape(kerala_image)

turtle.shape(kerala_image)
kuttan = turtle.Turtle()
kuttan.hideturtle()
kuttan.penup()

with open("kerala_districts.csv", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]
districts = [district_data.split(",") for district_data in lines]

User_answer = "null"
list_districts = ['ALAPPUZHA', 'ERNAKULAM', 'KOZHIKODE', 'PALAKKAD', 'KOLLAM', 'KANNUR', 'KASARAGOD', 'IDUKKI',
                  'KOTTAYAM', 'THRISSUR', 'PATHANAMTHITTA', 'MALAPPURAM', 'WAYANAD', 'TRIVANDRUM']


def custom_textinput(prompt):
    user_input = screen.textinput("Custom Input", prompt)
    return user_input


def location_finder(answer, list):
    x = 0
    y = 0
    for name in list:
        if answer == name[0].upper():
            x = float(name[1])
            y = float(name[2])
            kuttan.goto(x=x, y=y)
            kuttan.write(answer, align="center")


def check_answer(user_answer):
    if user_answer in list_districts:
        location_finder(User_answer, districts)


def user_input(n):
    user_answer = screen.textinput(title=f"{n}/20 Guess a district",
                                   prompt="Enter the districts name").upper()
    return user_answer


for n in range(20):
    # User_answer = screen.textinput(title=f"{n}/20 Guess a district", prompt="Enter the districts name").upper()
    User_answer= user_input(n)
    check_answer(User_answer)
    if User_answer == "EXIT":
        break

# score = 20 - fail_count
# kuttan.goto(400,700)
# print(f"score: {score}/20")
# def getMouseClickCoordinate(x,y):
# print(x,y)
# turtle.onscreenclick(getMouseClickCoordinate)
# turtle.mainloop()
