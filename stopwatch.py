from tkinter import*
from tkinter.ttk import*
import time

start_time = None
running = False

def update_time():
    if running:
        elapsed = time.time() - start_time  # Get elapsed time in seconds
        hr = int(elapsed // 3600)
        mn = int((elapsed % 3600) // 60)
        sc = int(elapsed % 60)
        ms = int((elapsed * 1000) % 1000)  # Convert to milliseconds

        lbl_time.config(text=f"{hr:02}:{mn:02}:{sc:02}:{ms:03}")
        root.after(10, update_time) # Continue updating every 10 ms

def start():
    global start_time, running
    if not running:
        start_time = time.time() - (start_time or 0) # preserve time if paused
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global start_time, running
    running = False
    start_time = None
    lbl_time.config(text="00:00:00:000")   # Reset Display

# Create the main window
root = Tk()
root.title("Stopwatch")
root.geometry("320x150")
root.resizable(False, False)
root.configure(bg="black")

style = Style()
style.configure('TButton', font=('Arial', 10, 'bold'), borderwidth=5)

# Heading
lbl_header = Label(root, text="Hr   Min   Sec   Ms", font=('Arial', 12, 'bold'),
                    foreground='lightgreen', background="black")
lbl_header.grid(row=0, column=0, columnspan=3, pady=5)

# Stopwatch Display
lbl_time = Label(root, text="00:00:00:000", font=('Arial', 30, 'bold'),
                    foreground='cyan', background="black")
lbl_time.grid(row=1, column=0, columnspan=3, pady=5)

# Buttons
button1 = Button(root, text="Start", command=start)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = Button(root, text="Stop", command=stop)
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = Button(root, text="Reset", command=reset)
button3.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()