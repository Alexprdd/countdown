import tkinter as tk
from tkinter import messagebox

#functions
    #messagebox

def time_up():
    messagebox.showinfo("Time Countdown", "Time is Up")

    #functionality of clock/time
    
def start():
    try:
        # Get the time from the entries and convert to seconds
        total_seconds = int(hour_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
        
        # If the time is valid, start the countdown
        if total_seconds > 0:
            countdown(total_seconds)
        else:
            messagebox.showwarning("Invalid Time", "Please enter a time greater than zero.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid integer values for hours, minutes, and seconds.")

def countdown(time_left):
    # Convert seconds to hours, minutes, and seconds
    hours = time_left // 3600
    minutes = (time_left % 3600) // 60
    seconds = time_left % 60

    # Update the entries to show remaining time
    hour_entry.delete(0, tk.END)
    hour_entry.insert(0, f"{hours:02}")
    minutes_entry.delete(0, tk.END)
    minutes_entry.insert(0, f"{minutes:02}")
    seconds_entry.delete(0, tk.END)
    seconds_entry.insert(0, f"{seconds:02}")

    if time_left > 0:
        # Call this function again after 1 second with time_left reduced by 1
        window.after(1000, countdown, time_left - 1)
    else:
        # If time is up, show the time-up message
        time_up()

#window

window=tk.Tk()
window.title("Time Countdown")
window.geometry("433x200")

#entries for time

hour_entry=tk.Entry(window, bd=4, relief=tk.RAISED)
hour_entry.grid(row=1, column=1, padx=2)
hour_entry.delete(0, tk.END)
hour_entry.insert(0, "Hour")

minutes_entry=tk.Entry(window, bd=4, relief=tk.RAISED)
minutes_entry.grid(row=1, column=2, padx=2)
minutes_entry.delete(0, tk.END)
minutes_entry.insert(0, "Minutes")

seconds_entry=tk.Entry(window, bd=4, relief=tk.RAISED)
seconds_entry.grid(row=1, column=3, padx=2)
seconds_entry.delete(0, tk.END)
seconds_entry.insert(0, "Seconds")

#button

set_time=tk.Button(window, text="Set Time Countdown", font=("Arial",12), bd=5, relief=tk.GROOVE, command=start)
set_time.grid(row=2, column=2,  pady=100)

window.mainloop()