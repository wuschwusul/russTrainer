import os
#os.popen("mkdir hui")

#-V0 -h -b 160 --vbr-new input.wav output.mp3

mp3file="temp.mp3"
wavfile="temp.wav"

os.popen(".\lame\lame.exe -V0 -h -b 160 --vbr-new "+mp3file+" "+wavfile)