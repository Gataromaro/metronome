import winsound
import time
import sys

""" 設定パート """
beat = 4 #拍子の設定 1以上の整数、３なら3拍子、4なら4拍子
BPM = 120 #BPMを入力
strong_tone = 4 #強拍の音の高さ 整数を入力　0=ド　1変わると半音変わる　2=レ 4=ミ 9=ラ
week_tone = 0 #弱剥の音の高さ 整数を入力　上に同じ
duration = 50 #1音の長さ：通常 50, 推奨 10~100 長くしすぎるとBPMに影響
cycle = 10 #繰り返し回数
""" 設定パートここまで """

st_tone_d = strong_tone-9
we_tone_d = week_tone-9
st_freq = int(440*2**(st_tone_d/12)) #強拍周波数
we_freq = int(440*2**(we_tone_d/12)) #弱拍周波数
sleep_time = (60/BPM) - (duration/1000) #停止時間
print('途中終了する場合は、「Ctrlキー」と「 c 」同時押し')
try:
    for i in range(cycle): #10回繰り返し
        winsound.Beep(st_freq, int(duration)) #440hz, 100ミリ秒の音
        time.sleep(sleep_time) #1秒間隔
        for _ in range(beat-1):
            winsound.Beep(we_freq, int(duration)) #440hz, 100ミリ秒の音
            time.sleep(sleep_time) #1秒間隔
except KeyboardInterrupt: #ctrl+cのエラー表示
    print('Ctrl + cで停止しました')
    sys.exit() #停止
except ValueError: #停止時間が負の場合のエラー表示
    print('停止時間が負の値です。BPM、duration設定を見直してください')