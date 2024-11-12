'''
This program make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/07/24
Ending 2024/08/22

'''
import os
import threading
import time
from tkinter import END, filedialog, ttk, messagebox as mb, Menu, Frame, Listbox, W, BOTTOM, X, LEFT, TOP, Label
from ttkthemes import themed_tk as tk
from mutagen.mp3 import MP3
from pygame import mixer


class MP3Player:
    """AI is creating summary for
    """
    def __init__(self):
        # Initialize the main window
        self.root = tk.ThemedTk()
        self.root.resizable(width=False, height=False)
        self.root["bg"] = "#008000"
        # Set the theme for the player
        self.root.set_theme("elegance")
        # Initialize the mixer (audio component)
        mixer.init()
        # Attributes for storing playback state
        self.paused = False
        self.muted = False
        self.songplaylist = []
        self.current_song_index = None
        # UI Elements
        self.setup_ui()

        # Start the main event loop
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_ui(self):
        """AI is creating summary for setup_ui
        """
        # Status bars
        self.statusbar = ttk.Label(self.root, text="Добро пожаловать в Mp3-плеер", anchor=W, font='Arial 16 italic')
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.statusbar1 = ttk.Label(self.root, text="Добро пожаловать в Mp3-плеер", anchor=W, font='Arial 16 italic')
        self.statusbar1.pack(side=TOP, fill=X)
        # Menu
        self.setup_menu()

        # Frames
        ltframe = Frame(self.root, bg="#008000")
        ltframe.pack(side=LEFT, padx=30, pady=30)
        rtframe = Frame(self.root, bg="#008000")
        rtframe.pack(pady=30, padx=20)
        topframe = Frame(rtframe, bg="#008000")
        topframe.pack()
        # Song playlist container
        self.songplaylistcontainer = Listbox(ltframe, fg='white', bg="#808080")
        self.songplaylistcontainer.pack()
        # Buttons on left frame
        add_btn = ttk.Button(ltframe, text="Добавить", command=self.browse_file)
        add_btn.pack(side=LEFT)
        rem_btn = ttk.Button(ltframe, text="Удалить", command=self.remove_song)
        rem_btn.pack(side=LEFT)
        # Labels for time
        self.lengthlabel = ttk.Label(topframe, text='Общее время : --:--')
        self.lengthlabel.pack(pady=5)
        self.currenttimelabel = ttk.Label(topframe, text='Текущее время : --:--')
        self.currenttimelabel.pack()
        # Middle frame for controls
        middleframe = Frame(rtframe, bg="#008000")
        middleframe.pack(pady=30, padx=30)
        play_btn = ttk.Button(middleframe, text="Играть", command=self.play_music)
        play_btn.grid(row=0, column=0, padx=10)
        stop_btn = ttk.Button(middleframe, text="Стоп", command=self.stop_music)
        stop_btn.grid(row=0, column=1, padx=10)
        pause_btn = ttk.Button(middleframe, text="Пауза", command=self.pause_music)
        pause_btn.grid(row=0, column=2, padx=10)
        # Bottom frame for additional controls
        bottomframe = Frame(rtframe, bg="gray")
        bottomframe.pack(pady=10, padx=5)
        rewind_btn = ttk.Button(bottomframe, text="Перемотка", command=self.rewind_music)
        rewind_btn.grid(row=0, column=0, padx=10)
        self.volume_btn = ttk.Button(bottomframe, text="Беззвучный", command=self.mute_music)
        self.volume_btn.grid(row=0, column=1)
        # Volume control scale
        self.scale = ttk.Scale(bottomframe, from_=0, to=100, orient="horizontal", command=self.set_vol)
        # set default scale value on start
        self.scale.set(70)
        mixer.music.set_volume(0.7)
        self.scale.grid(row=0, column=2, pady=15, padx=30)

    def setup_menu(self):
        """AI is creating summary for setup_menu
        """
        # Main menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.browse_file)
        menubar.add_cascade(label="Файл", menu=file_menu)
        # About menu
        about_menu = Menu(menubar, tearoff=0)
        about_menu.add_command(label="О программе", command=self.show_info)
        menubar.add_cascade(label="Справка", menu=about_menu)

    def show_info(self):
        """AI is creating summary for show_info
        """
        mb.showinfo("О программе", "Феткулин Григорий - Mp3-плеер, 2022")

    def browse_file(self):
        """AI is creating summary for browse_file
        """
        # Allow user to select a file and add it to the playlist
        filename_path = filedialog.askopenfilename()
        if filename_path:
            self.add_to_songplaylist(filename_path)
            mixer.music.queue(filename_path)

    def add_to_songplaylist(self, filename_path):
        """AI is creating summary for add_to_songplaylist

        Args:
            filename_path ([type]): [description]
        """
        # Add song to the playlist
        filename = os.path.basename(filename_path)
        self.songplaylist.append(filename_path)
        self.songplaylistcontainer.insert(END, filename)

    def play_music(self):
        """AI is creating summary for play_music
        """
        if self.paused:
            mixer.music.unpause()
            self.statusbar['text'] = "Музыка возобновилась"
            self.paused = False
        else:
            try:
                self.stop_music()
        # wait for a second before starting
                time.sleep(1)
                sel_song = self.songplaylistcontainer.curselection()
                if sel_song:
                    self.current_song_index = int(sel_song[0])
                    play_it = self.songplaylist[self.current_song_index]
                    mixer.music.load(play_it)
                    mixer.music.play()
                    self.statusbar['text'] = "Воспроизведение музыки" + ' - ' + os.path.basename(play_it)
                    self.show_details(play_it)
                else:
                    mb.showerror("Ошибка выбора", "Музыкальный файл не выбран, пожалуйста, повторите попытку")
            except Exception as e:
                mb.showerror('Ошибка', f'MP3-плееру не удалось воспроизвести файл. {str(e)}')

    def stop_music(self):
        """AI is creating summary for stop_music
        """
        mixer.music.stop()
        self.statusbar['text'] = "Музыка остановлена"

    def pause_music(self):
        """AI is creating summary for pause_music
        """
        self.paused = True
        mixer.music.pause()
        self.statusbar['text'] = "Музыка приостановлена"

    def rewind_music(self):
        """AI is creating summary for rewind_music
        """
        self.play_music()
        self.statusbar['text'] = "Музыка перемотана"

    def set_vol(self, val):
        """AI is creating summary for set_vol

        Args:
            val ([type]): [description]
        """
        volume = float(val) / 100
        mixer.music.set_volume(volume)

    def mute_music(self):
        """AI is creating summary for mute_music
        """
        if self.muted:
            mixer.music.set_volume(0.7)
            self.volume_btn.configure(text="Беззвучный")
            self.scale.set(70)
            self.muted = False
        else:
            mixer.music.set_volume(0)
            self.volume_btn.configure(text="Включить звук")
            self.scale.set(0)
            self.muted = True

    def remove_song(self):
        """AI is creating summary for remove_song
        """
        selected_song = self.songplaylistcontainer.curselection()
        if selected_song:
            index = int(selected_song[0])
            self.songplaylistcontainer.delete(index)
            self.songplaylist.pop(index)

    def show_details(self, play_song):
        """AI is creating summary for show_details

        Args:
            play_song ([type]): [description]
        """
        # Get the total length of the song
        file_data = os.path.splitext(play_song)
        if file_data[1] == '.mp3':
            audio = MP3(play_song)
            total_length = audio.info.length
        else:
            a = mixer.Sound(play_song)
            total_length = a.get_length()

        mins, secs = divmod(total_length, 60)
        mins, secs = round(mins), round(secs)
        timeformat = f'{mins:02d}:{secs:02d}'
        self.lengthlabel['text'] = "Общее время - " + timeformat

        # Start a new thread to update the current time
        threading.Thread(target=self.start_count, args=(total_length,)).start()

    def start_count(self, total_time):
        """AI is creating summary for start_count

        Args:
            total_time ([type]): [description]
        """
        # Track and display current song time
        current_time = 0
        while current_time <= total_time and mixer.music.get_busy():
            if not self.paused:
                mins, secs = divmod(current_time, 60)
                mins, secs = round(mins), round(secs)
                timeformat = f'{mins:02d}:{secs:02d}'
                self.currenttimelabel['text'] = "Текущее время - " + timeformat
                time.sleep(1)
                current_time += 1
    def on_closing(self):
        # Handle window closing
        self.stop_music()
        self.root.destroy()


# Run the application
if __name__ == "__main__":
    MP3Player()
