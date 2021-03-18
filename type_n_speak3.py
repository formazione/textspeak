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
        show_list()


def show_list():
    global lbx

    lbx.delete("0")
    elenco = os.listdir("audio")
    elenco.sort(reverse=False)
    for file in elenco:
        if len(file[:-4]) == 1:
            lbx.insert("end", f"")
            lbx.insert("end", f"=== [ {file[:-4]} ] ====")
        else:
            lbx.insert("end", file)

def start():
    global word, lbx, text

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
    
    # text widget where you write
    lbx = tk.Listbox(
        root,
        bg="black",
        fg="white"
        )
    lbx.pack(side="left", fill="both")
    show_list()

    text = tk.Text(root)
    text.pack()


    lbx.bind("<Double-Button>", add_word_to_text)
    text.focus()
    text.bind("<Key>", audiokey)
    text.bind("<BackSpace>", indietro)
    text.bind("<Return>", _return)
    root.mainloop()

def add_word_to_text(evt):
    global lbx, text

    word = lbx.get(lbx.curselection())
    word = word[:-4]
    print(word)
    text.insert("end", word)
    mixer.music.load("audio/" + word + ".mp3")
    mixer.music.play()
    text.insert("end", " ")



speak(word="spazio, indietro")
start()
