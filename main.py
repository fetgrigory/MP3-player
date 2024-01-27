'''
This program make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/07/24
Ending 2024/08/22

'''
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox as mb
from tkinter import *
import os
import threading
from ttkthemes import themed_tk as tk
from mutagen.mp3 import MP3
import time
from pygame import mixer
# Создание главного окна
root = tk.ThemedTk()
root.resizable(width=False, height=False)
root["bg"]="#008000"
# Настройка темы для плеера
root.set_theme("elegance")
statusbar = ttk.Label(root, text="Добро пожаловать в Mp3-плеер", anchor=W, font='Arial 16 italic')
statusbar.pack(side=BOTTOM, fill=X)
statusbar1 = ttk.Label(root, text="Добро пожаловать в Mp3-плеер", anchor=W, font='Arial 16 italic')
statusbar1.pack(side=TOP, fill=X)
# Создать строку меню
menubar = Menu(root)
root.config(menu=menubar)
def show_info():
    mb.showinfo("О программе", "Феткулин Григорий - Mp3-плеер, 2022")

# Создать подменю
subMenu = Menu(menubar, tearoff=0)
# Список для хранения воспроизведения
songplaylist = []
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_songplaylist(filename_path)
    mixer.music.queue(filename_path)
def add_to_songplaylist(filename):
    filename = os.path.basename(filename)
    index = 0
    songplaylistcontainer.insert(index, filename)
    songplaylist.insert(index, filename_path)
    index += 1
main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label="Открыть", command=browse_file)
about_menu = Menu()
about_menu.add_command(label="О программе", command=show_info)
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)
root.config(menu=main_menu)
mixer.init()  
# Инициализация микшера
root.title("Mp3-плеер")
ltframe = Frame(root,bg="#008000")
ltframe.pack(side=LEFT, padx=30, pady=30)
songplaylistcontainer = Listbox(ltframe,fg='white')
songplaylistcontainer["bg"]="#808080"
songplaylistcontainer.pack()
addBtn = ttk.Button(ltframe, text="Добавить",command=browse_file)
addBtn.pack(side=LEFT)
def remove_song():
    sel_song = songplaylistcontainer.curselection()
    sel_song = int(sel_song[0])
    songplaylistcontainer.delete(sel_song)
    songplaylist.pop(sel_song)
root.style = ttk.Style()
root.style.theme_use("clam")
remBtn = ttk.Button(ltframe, text="Удалить", command=remove_song)
remBtn.pack(side=LEFT)
root.style.configure('TButton', background='#DAA520')
rtframe = Frame(root,bg="#008000")
rtframe.pack(pady=30,padx=20)
topframe = Frame(rtframe,bg="#008000")
topframe.pack()
root.style = ttk.Style()
root.style.configure('TLabel', background='#008000')
lengthlabel = ttk.Label(topframe,text='Общее время : --:--')
lengthlabel.pack(pady=5)
currenttimelabel = ttk.Label(topframe, text='Текущее время : --:--')
currenttimelabel.pack()
def show_details(play_song):
    file_data = os.path.splitext(play_song)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Общее время" + ' - ' + timeformat
    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()
def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Текущее время" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1
def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Музыка Возобновилась"
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            sel_song = songplaylistcontainer.curselection()
            sel_song = int(sel_song[0])
            play_it = songplaylist[sel_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Воспроизведение музыки" + ' - ' + os.path.basename(play_it)
            show_details(play_it)
        except:
            mb.showerror('Файл не найден', 'Mp3-player не удалось найти файл. Пожалуйста, выберите еще раз.')
def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Музыка остановлена"
paused = FALSE
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Музыка приостановлена"
def rewind_music():
    play_music()
    statusbar['text'] = "Музыка перемотана"
def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)
muted = FALSE
def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        volumeBtn.configure(text="Беззвучный")
        scale.set(70)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(text="Громкость")
        scale.set(0)
        muted = TRUE
middleframe = Frame(rtframe,bg="#008000")
middleframe.pack(pady=30, padx=30)
playBtn = ttk.Button(middleframe, text="Играть", command=play_music)
playBtn.grid(row=0, column=0, padx=10)
stopBtn = ttk.Button(middleframe, text="Стоп", command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)
pauseBtn = ttk.Button(middleframe, text="Пауза", command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)
bottomframe = Frame(rtframe,bg="gray")
bottomframe.pack(pady=10,padx=5)
rewindBtn = ttk.Button(bottomframe, text="Перемотка", command=rewind_music)
rewindBtn.grid(row=0, column=0,padx=10)
volumeBtn = ttk.Button(bottomframe, text="Беззвучный", command=mute_music)
volumeBtn.grid(row=0, column=1)
scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70) 
 # установить значение масштаба по умолчанию при запуске музыкального проигрывателя
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)
def on_closing():
    stop_music()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
if __name__==mainloop():
 root.mainloop()
