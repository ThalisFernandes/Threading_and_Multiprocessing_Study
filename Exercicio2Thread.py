from threading import Thread
import time
from pytube import YouTube

videos_url = []

def download_videos(url, number):
    try:
        print(f'Iniciando a Thread {number}')
        yt = YouTube(f'{url}')
        time.sleep(10 - number)
        mp4_file = yt.streams.filter(file_extension='mp4')
        file360 = mp4_file.get_by_resolution('360p')
        file360.download('./download/')
        print(f'Finalizando a Thread {number}')
    except Exception as E:
        print(E)


t1 = Thread(target=download_videos, args=('https://www.youtube.com/watch?v=9GeNsY1m4SE', 1))
t2 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/hA1gUK7dqJI',2))
t3 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/6ZWwOtA9j-E',3))
t4 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/nQNBqmf9n-M',4))
t5 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/s-Ecj9bor5o',5))
t6 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/jMc5uIkhoeU',6))
t7 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/fus2oS2Wl18',7))
t8 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/2Y8QCcdAu_s',8))
t9 = Thread(target=download_videos, args=('https://www.youtube.com/shorts/R8nsEz11AtA',9))






t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()


