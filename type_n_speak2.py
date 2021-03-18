# create the mp3 letters audio files
import os
from gtts import gTTS
import tkinter as tk
from pygame import mixer



def speak(word):
    print("looking for word in dictionary")
    print(os.listdir("audio/"))
    if f"{word}.mp3" not in os.listdir("audio/"):
        print("This is not present... creating")
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
            if event.char == " " or event.char in ",.!?":
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
            word=""

    def indietro(event):
        global word
        
        print(event.char)
        word = word[:-1]
        print(word)
        try:
            mixer.music.load("indietro.mp3")
            mixer.music.play()
        except:
            pass

    def _return(evt):
        global word

        speak(word)
        mixer.music.load("audio/" + word + ".mp3")
        mixer.music.play()
        word = ""
 
    root = tk.Tk()
    root.title("Type to hear the pc reading the text when press space")
    root.geometry("600x400+200+400")
    text = tk.Text(root)
    text.pack()
    text.focus()
    text.bind("<Key>", audiokey)
    text.bind("<BackSpace>", indietro)
    text.bind("<Return>", _return)
    root.mainloop()


speak(word="spazio, indietro")
start()
