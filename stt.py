# python -m sounddevice
import vosk
import sys
import sounddevice as sd
import queue
import json
import time
import psutil


def out_red(text):
    print("\033[31m {}" .format(text))\
        
def out_white(text):
    print("\033[39m {}" .format(text))

def model_vosk(f_open):
    if f_open == 'big':
        return 1
    elif f_open == 'small':
        return 2




f = open('vosk.txt', 'r', encoding='utf-8')
f_open = f.read()


if model_vosk(f_open) == 1:
    print('model_vosk finish installed: big')
    model = vosk.Model("vosk_model_big_ru_0.10")

elif model_vosk(f_open) == 2:
    print('model_vosk finish installed: small')
    model = vosk.Model("vosk_model_small_ru_0.4")

else:
    model = vosk.Model("vosk_model_small_ru_0.4")


samplerate = 16000
device = 1

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
            #else:
            #    print(rec.PartialResult())
            
