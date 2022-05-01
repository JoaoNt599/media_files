import os
from moviepy.editor import *
import glob

lista_mp4 = glob.glob('*mp4')

print(lista_mp4)

for video in lista_mp4:
    print('Buscadno os arquivos mp4 no diretório...')
    print('_'*20)
    mp4 = VideoFileClip(os.path.join(video))
    nome_mp3 = video[:-4]+'.mp3'
    print('Convertendo arquivos para mp3')
    mp4.audio.write_audiofile(os.path.join(nome_mp3))
    print('_'*20)
    print('Convertendo mp4 ' + video + ' para mp3 ' + nome_mp3)