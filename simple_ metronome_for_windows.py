import winsound
import time
import sys

""" 設定パート """
BPM = 200 #BPMを入力
tone = 0 #音の高さ 整数を入力　0=ド　1変わると半音変わる　2=レ 4=ミ 9=ラ
duration = 50 #1音の長さ：通常 50, 推奨 10~100 長くしすぎるとBPMに影響
cycle = 10 #繰り返し回数
""" 設定パートここまで """

tone_d = tone-9
freq = int(440*2**(tone_d/12)) #周波数
sleep_time = (60/BPM) - (duration/1000) #停止時間
print('途中終了する場合は、「Ctrlキー」と「 c 」同時押し')
try:
    for i in range(cycle): #10回繰り返し
        winsound.Beep(freq, int(duration)) #440hz, 100ミリ秒の音
        time.sleep(sleep_time) #1秒間隔
except KeyboardInterrupt: #ctrl+cのエラー表示
    print('Ctrl + cで停止しました')
    sys.exit() #停止
except ValueError: #停止時間が負の場合のエラー表示
    print('停止時間が負の値です。BPM、duration設定を見直してください')