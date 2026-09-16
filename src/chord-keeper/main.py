import keyboard
import time

from pathlib import Path

from core.paths import SONG_LIST
from core.player import Player

if __name__ == "__main__":
    player = Player(SONG_LIST)
    print('Músicas disponíveis:')
    for song in player.song_list:
        print(f'- {song}')
    print('Digite o nome da música que quer tocar:')
    song_name = input().strip()
    if song_name in player.song_list:
        player.get_song(song_name)
        print(f'Tocando a música: {song_name}')
        print(f'BPM: {player.song_bpm}')
        for i in range(3, 0, -1):
            print(f'Começando em {i}...')
            time.sleep(1)
        player.play()
    else:
        print('Música não encontrada.')