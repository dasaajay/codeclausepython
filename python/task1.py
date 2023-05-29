from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("300x900")

mixer.init()
mixer.music.load("C:/Users/aspire5/Downloads/[iSongs.info] 01 - Padi Padi Leche.mp3")

song_name = StringVar()
song_name.set("Padi Padi Leche")  # Set the initial song name

def pause():
    mixer.music.pause()

def play():
    mixer.music.play()
    song_label.place(x=510, y=int(screen_height/2), anchor="w")  # Show the song name bar
    song_label.config(font=("lucidia", 18))  # Increase font size

def resume():
    mixer.music.unpause()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

Label(root, text="Welcome to music player", font="lucidia 30 bold", bg="lightblue").place(x=screen_width//2, y=screen_height//10, anchor="center")

# Create a label for the song name and configure it with scrolling properties
song_label = Label(root, textvariable=song_name, font="lucidia 12", width=80, height=2, anchor="w", relief="sunken",
                   bg="white", fg="black")
song_label.place(x=screen_width//2, y=screen_height//2, anchor="center")

button_width = 10
button_height = 2

play_button = Button(text="Play", command=play)
play_button.config(bg="green", fg="white", font="lucidia 12 bold", width=button_width, height=button_height)
play_button.place(x=screen_width//3, y=screen_height//2 + screen_height//10, anchor="center")

pause_button = Button(text="Pause", command=pause)
pause_button.config(bg="orange", fg="white", font="lucidia 12 bold", width=button_width, height=button_height)
pause_button.place(x=screen_width//3 + screen_width//6, y=screen_height//2 + screen_height//10, anchor="center")

resume_button = Button(text="Resume", command=resume)
resume_button.config(bg="yellow", fg="black", font="lucidia 12 bold", width=button_width, height=button_height)
resume_button.place(x=screen_width//3 + 2*screen_width//6, y=screen_height//2 + screen_height//10, anchor="center")

quit_button = Button(text="Quit", command=quit)
quit_button.config(bg="red", fg="white", font="lucidia 12 bold", width=button_width, height=button_height)
quit_button.place(x=screen_width//3 + 3*screen_width//6, y=screen_height//2 + screen_height//10, anchor="center")

def update_song_name():
    current_song = song_name.get()
    song_name.set(current_song[1:] + current_song[0])  # Scroll the song name

    # Increase the width of the label dynamically
    label_width = len(song_name.get())
    song_label.config(width=label_width)

    # Call the update_song_name function again after 150 milliseconds (adjust as needed)
    root.after(150, update_song_name)

# Start updating the song name periodically
update_song_name()

root.configure(bg="lightblue")  # Set the background color of the root window

root.mainloop()
