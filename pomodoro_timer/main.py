from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark_text = "✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_text["text"] = "Timer"
    canvas.itemconfig(timer_canvas, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)

    Work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    Long_break_sec = LONG_BREAK_MIN*60


    if reps%8==0:
        count_down(Long_break_sec)
        timer_text["text"]="Break"
        timer_text["fg"]=RED

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text["text"] = "Break"
        timer_text["fg"] = PINK

    else:
        count_down(Work_sec)
        timer_text["text"] = "Work"
        timer_text["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_min = math.floor(count/60)
    count_sec = count % 60

    for n in range(10):
        if count_sec == n:
            count_sec = f"0{n}"
        if count_min ==n:
            count_min = f"0{n}"

    canvas.itemconfig(timer_canvas, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer =  window.after(1000, count_down, count-1)
    elif reps>=8:
        reps = 0
        return
    else:
        start_timer()
        if reps%2 ==0:
            n=reps//2
            checktext = check_mark_text * n
            check_mark["text"]= checktext




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=10,padx=10, bg= YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,110,image= tomato_img)
timer_canvas = canvas.create_text(100,110,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2 ,row=2)

timer_text = Label(text="TIMER",fg= GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
timer_text.grid(column=2 ,row=1)

start_button = Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(column=1, row= 3)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3, row= 3)


check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check_mark.grid(column=2, row=4)



window.mainloop()


