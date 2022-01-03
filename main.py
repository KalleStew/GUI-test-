# create the window
import tkinter as tk
import tkinter
from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("Launch GUI")

window.geometry('735x441')

# back ground
window.config(bg="grey")

# Special variables


# functions
'''
def resizer(e):
    global bg1, resized_bg, new_bg
    # Open our imagine
    bg1 = Image.open("realbg.png")
    # Resize the image
    resized_bg = bg1.resize((e.width,e.height), Image.ANTIALIAS)
    # Define out image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add back to the canvas
    my_canvas.create_image(0, 0, image= new_bg, anchor="nw")
    #size text
'''


# Launch function
def launch():
    global running
    # Timer
    if not running:
        update()
        running = True
    # buttons

# Abort function
def abort():
    # timer(stop timer)
    global running
    if running:
        # cancel updating of the time  using after_cancel
        timer.after_cancel(update_time)
        running = False

    # buttons(close all valves)
    global O1, O2, N1, N2
    O1valveC.select()
    O2valveC.select()
    N1valveC.select()
    N2valveC.select()
    rlan.set(0)
    launch.config(state=DISABLED)


# Update Function(for timer)
def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # include zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update time label
    timer.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second, call update function with update_time function
    global update_time
    update_time = timer.after(1000, update)


# launchReady function
def launchReady():
    '''# check whether a valve was opened or closed
    if state == 1:
        rCount += 1
    if state == 0:
        rCount -= 1
    # check if enough valves are open to launch
    if rCount == 2:
        rLaunch.select()
        launch.config(state=NORMAL)'''
    global O1, O2, N1, N2
    if O1.get() == 1 and O2.get() == 1 and N1.get() == 1 and N2.get() == 1:
        rLaunch.select()
        launch.config(state=NORMAL)
    else:
        rLaunch.deselect()
        launch.config(state=DISABLED)
        rlan.set(0)


# Creating frames for the buttons
# Cortrols
frame_display = tkinter.Frame(master=window,
                              width=250,
                              height=300,
                              bg="gray80",
                              relief=SUNKEN)

frame_display.grid(row=0, column=0, padx=2, pady=10)

window.columnconfigure(frame_display, weight=1, minsize=250)
window.rowconfigure(frame_display, weight=1, minsize=300)

# display
frame_controls = tkinter.Frame(master=window,
                               width=390,
                               height=410,
                               bg="gray80",
                               relief=SUNKEN)

frame_controls.grid(row=0, column=2, padx=2, pady=10)

window.columnconfigure(frame_controls, weight=1, minsize=390)
window.rowconfigure(frame_controls, weight=1, minsize=410)

# Background with image
'''
#create a background
bg = ImageTk.PhotoImage(file = "realbg.png")

my_canvas = Canvas(window, width = 735 , height =441)

#my_canvas.place(x=0,y=0)
my_canvas.create_image(0,0,image=bg, anchor="nw")
my_canvas.pack(fill = "both", expand = True)
'''

# label QSET at the top

mLbl = Label(
    window,
    text="QRET",
    font=("Abobe Arabic", 40),
    bg="silver",
    fg="black")

# Place Label

mLbl.place(x=75, y=10)

# Test/Flight timer
# Variables
running = False
hours, minutes, seconds = 0, 0, 0

# label that displays the time
timer = Label(text="00:00:00", font=('Arial', 40), bg="black", fg="white")
timer.place(x=50, y=350)

# buttons
# Abort
# creating the button
abort = Button(master=frame_controls,
               text="Abort",
               font=("Abobe Arabic", 15),
               fg="red2",
               bg="dark red",
               width=10,
               height=1,
               command=abort)
#   putting it on the screen
abort.grid(row=0, column=2, padx=5, pady=5)

# launch
# creating the button
launch = Button(master=frame_controls,
                text="Launch",
                font=("Abobe Arabic", 15),
                fg="pale green",
                bg="green",
                width=10,
                height=1,
                command=launch,
                state=DISABLED)
# putting it on the screen
launch.grid(row=0, column=1, padx=5, pady=5)

# Go for launch button
# button
rlan = IntVar()
rlan.set(0)
rLaunch = Radiobutton(master=frame_controls, text="Ready for Launch", bg="gray80", value=1, variable=rlan,
                      activeforeground="green")
rLaunch.grid(row=0, column=0, padx=10, pady=5)

# Fine Controls
# O valve 1
O1 = IntVar()
O1.set(2)
# Label
Ovalve1 = Label(master=frame_controls, text="Oxygen valve 1", bg="gray80")
Ovalve1.grid(row=1, column=0, pady=5)
# Open button
O1valveO = Radiobutton(master=frame_controls, text="Open", value=1, bg="gray80", variable=O1, command=launchReady())
O1valveO.grid(row=1, column=1, pady=5)
# Close button
O1valveC = Radiobutton(master=frame_controls, text="Closed", value=2, bg="gray80", variable=O1, command=launchReady())
O1valveC.grid(row=1, column=2, pady=5)

# O valve 2
O2 = IntVar()
O2.set(2)
# Label
Ovalve2 = Label(master=frame_controls, text="Oxygen valve 2", bg="gray80")
Ovalve2.grid(row=2, column=0, pady=5)
# Open button
O2valveO = Radiobutton(master=frame_controls, text="Open", value=1, bg="gray80", variable=O2, command=launchReady)
O2valveO.grid(row=2, column=1, pady=5)
# Close button
O2valveC = Radiobutton(master=frame_controls, text="Closed", value=2, bg="gray80", variable=O2, command=launchReady)
O2valveC.grid(row=2, column=2, pady=5)

# N valve 1
N1 = IntVar()
N1.set(2)
# Label
Nvalve1 = Label(master=frame_controls, text="Nitrous Oxide valve 1", bg="gray80")
Nvalve1.grid(row=3, column=0, pady=5)
# Open button
N1valveO = Radiobutton(master=frame_controls, text="Open", value=1, bg="gray80", variable=N1, command=launchReady)
N1valveO.grid(row=3, column=1, pady=5)
# Close button
N1valveC = Radiobutton(master=frame_controls, text="Closed", value=2, bg="gray80", variable=N1, command=launchReady)
N1valveC.grid(row=3, column=2, pady=5)

# N value 2
N2 = IntVar()
N2.set(2)
# Label
Nvalve2 = Label(master=frame_controls, text="Nitrous Oxide valve 2", bg="gray80")
Nvalve2.grid(row=4, column=0, pady=5)
# Open button
N2valveO = Radiobutton(master=frame_controls, text="Open", value=1, bg="gray80", variable=N2, command=launchReady)
N2valveO.grid(row=4, column=1, pady=5)
# Close button
N2valveC = Radiobutton(master=frame_controls, text="Closed", value=2, bg="gray80", variable=N2, command=launchReady)
N2valveC.grid(row=4, column=2, pady=5)

# Trust slider
# Label
trustS = Label(master=frame_controls, text="% Thrust", bg="grey80")
trustS.grid(row=5, columnspan=3, pady=3)
# Slider
SlideT = Scale(master=frame_controls, from_=0, to=100, tickinterval=10, orient=HORIZONTAL, bg="gray80")
SlideT.grid(row=6, sticky=EW, columnspan=3)

# Display values
# nitrous oxide pressure(2 values)
# Main Name Label
nPres = Label(frame_display, text="Nitrogen Pressure", bg="grey80", font="lucida 9 underline")
nPres.grid(row=2, columnspan=2, pady=3)

# Valve 1
N1pressure = 20
N1pres = StringVar()
N1pres.set(str(N1pressure) + ' PSI || ' + str(round((N1pressure * 0.0689476), 2)) + ' Barr')
# Name Label
N1presL = Label(frame_display, text="Valve 1 Pressure", bg="gray80")
N1presL.grid(row=3, column=0, padx=5)
# Display Label
N1presD = Label(frame_display, textvariable=N1pres, bg="black", fg="white", width=15)
N1presD.grid(row=4, column=0, padx=5)

# Valve 2
N2pressure = 30
N2pres = StringVar()
N2pres.set(str(N2pressure) + ' PSI || ' + str(round((N2pressure * 0.0689476), 2)) + ' Barr')
# Name Label
N2presL = Label(frame_display, text="Valve 2 Pressure", bg="gray80")
N2presL.grid(row=3, column=1, padx=5)
# Display Label
N2presD = Label(frame_display, textvariable=N2pres, bg="black", fg="white", width=15)
N2presD.grid(row=4, column=1, padx=5)

# oxygen pressure(2 values)
# Main Name Label
OPres = Label(frame_display, text="Oxygen Pressure", bg="grey80", font="lucida 9 underline")
OPres.grid(row=5, columnspan=2, pady=3)

# Valve 1
O1pressure = 15
O1pres = StringVar()
O1pres.set(str(O1pressure) + ' PSI || ' + str(round((O1pressure * 0.0689476), 2)) + ' Barr')
# Name Label
O1presL = Label(frame_display, text="Valve 1 Pressure", bg="gray80")
O1presL.grid(row=6, column=0, padx=5)
# Display Label
O1presD = Label(frame_display, textvariable=O1pres, bg="black", fg="white", width=15)
O1presD.grid(row=7, column=0, padx=5)

# Valve 2
O2pressure = 35
O2pres = StringVar()
O2pres.set(str(O2pressure) + ' PSI || ' + str(round((O2pressure * 0.0689476), 2)) + ' Barr')
# Name Label
O2presL = Label(frame_display, text="Valve 2 Pressure", bg="gray80")
O2presL.grid(row=6, column=1, padx=5)
# Display Label
O2presD = Label(frame_display, textvariable=O2pres, bg="black", fg="white", width=15)
O2presD.grid(row=7, column=1, padx=5)

# environment temperature
temp = 25
eTemp = StringVar()
eTemp.set(str(temp) + ' C')
# Name Label
envTempL = Label(frame_display, text="Environment Temperature", bg="gray80")
envTempL.grid(row=0, column=0, padx=5)
# Display Label
envTempD = Label(frame_display, textvariable=eTemp, bg="black", fg="white", width=15)
envTempD.grid(row=1, column=0, padx=5)

# environment pressure
pres = 1
ePres = StringVar()
ePres.set(str(pres) + ' PSI || ' + str(round((pres * 0.0689476), 2)) + ' Barr')
# Name Label
envPresL = Label(frame_display, text="Environment Pressure", bg="gray80")
envPresL.grid(row=0, column=1, padx=5)
# Display Label
envPresD = Label(frame_display, textvariable=ePres, bg="black", fg="white", width=15)
envPresD.grid(row=1, column=1, padx=5)

# Current trust
currentTrust = 200000
cThrust = StringVar()
cThrust.set(str(currentTrust) + ' N')
# Name Label
cThrustL = Label(frame_display, text="Thrust", bg="gray80")
cThrustL.grid(row=10, columnspan=2)
# Display Label
cThrustD = Label(frame_display, textvariable=cThrust, bg="black", fg="white", width=15)
cThrustD.grid(row=11, columnspan=2)

# Ejector temp?


# window.bind('<Configure>',resizer)
window.mainloop()

'''
#main definition
def main():
    print("balls\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
