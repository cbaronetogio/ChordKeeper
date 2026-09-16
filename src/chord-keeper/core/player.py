import keyboard
import time

from pathlib import Path

NOTE_TO_KEY = {
    'c': 'z',
    'C': 'q',
    'd': 'x',
    'D': 'w',
    'e': 'c',
    'E': 'e',
    'f': 'v',
    'F': 'r',
    'g': 'b',
    'G': 't',
    'a': 'n',
    'A': 'y',
    'b': 'm',
    'B': 'u',
}

class Player:
    def __init__(self, songs: Path):
        self.song_path = songs
        self.guarantee_songs_folder()
        self.song_list = []
        self.song_bpm = 0
        self.song = []
        for song in self.song_path.iterdir():
            if song.is_file() and song.suffix == ".txt":
                self.song_list.append(song.stem)

    def guarantee_songs_folder(self):
        self.song_path.mkdir(exist_ok=True, parents=True)

    def get_song(self, song_name):
        with open(self.song_path / f"{song_name}.txt", "r") as f:
            for line in f:
                if line.startswith("bpm="):
                    self.song_bpm = int(line.split("=")[1].strip())
                else:
                    notes = line.strip().split()
                    self.song.extend(notes)

    def play(self):
        for elem in self.song:
                note, duration = elem.split(":")
                d = float(duration)
                if len(note) > 1:
                    chord = '+'.join([NOTE_TO_KEY[n] for n in note])
                    keyboard.press(chord)
                    time.sleep((60/self.song_bpm) * d)
                    keyboard.release(chord)
                elif len(note) == 1:
                    if note in NOTE_TO_KEY:
                        key = NOTE_TO_KEY[note]
                        keyboard.press(key)
                        time.sleep((60/self.song_bpm) * d)
                        keyboard.release(key)
                    else:
                        time.sleep((60/self.song_bpm) * d)
