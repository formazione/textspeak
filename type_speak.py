# create the mp3 letters audio files
import os
from gtts import gTTS
import tkinter as tk
from pygame import mixer  # Load the popular external library
from tqdm import trange
from time import sleep

def mp3_from_text(letters="abcdefghijklmnopqrstuvwxyz", words=""):
    "words needs to be separated by a comma"
    
    # Create folder audio if not present
    if "audio" not in os.listdir():
        os.mkdir("audio")
    if letters != "":
        letters = list(letters)
    else:
        letters = []
    if words != "":
        for word in words.split():
            letters.append(word)
    for x in range(len(letters)):
        # do not overwrites existring audio if saved yet
        if f"audio/{letters[x]}.mp3" not in os.listdir("audio/"):
            t = gTTS(letters[x], "it")
            t.save(f"audio/{letters[x]}.mp3")

def speak(word):
        if f"audio/{word}.mp3" not in os.listdir("audio/"):
            print("creating file")
            t = gTTS(word, "it")
            t.save(f"audio/{word}.mp3")
            print("created " + word)



def start():
    global word

    mixer.init()
    word = ""
    def audiokey(event):
        global word

        print(event.char)
        try:
            if event.char == " ":
                speak(word)
                mixer.music.load("audio/" + word + ".mp3")
                mixer.music.play()
                word = ""
            else:
                word += str(event.char)
                # mixer.music.load("audio/" + event.char + ".mp3")
                # mixer.music.play()
                print(word)
        except:
            pass
    def indietro(event):
        print(event.char)
        try:
            mixer.music.load("indietro.mp3")
            mixer.music.play()
        except:
            pass
 
    root = tk.Tk()
    root.geometry("600x400+200+400")
    text = tk.Text(root)
    text.pack()
    text.focus()
    text.bind("<Key>", audiokey)
    text.bind("<BackSpace>", indietro)
    root.mainloop()

# UNCOMMENT THE FOLLOWING LINE TO CREATE AUDIO THE FIRST TIME 
# mp3_from_text(words="spazio, indietro")
start()
