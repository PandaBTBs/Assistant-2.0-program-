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

def model_vosk(voskSTT):
    if voskSTT == 'big':
        return 1
    elif voskSTT == 'small':
        return 2


print('input vosk model: small or big (or pass - small model)')
voskSTT = str(input())
if model_vosk(voskSTT) == 1:
    print('model_vosk finish installed: big')
    model = vosk.Model("J:\\Stella\\stellaPR\\vosk_model_big_ru_0.10")

elif model_vosk(voskSTT) == 2:
    print('model_vosk finish installed: small')
    model = vosk.Model("J:\\Stella\\stellaPR\\vosk_model_small_ru_0.4")

else:
    model = vosk.Model("J:\\Stella\\stellaPR\\vosk_model_small_ru_0.4")


# else:
#     out_red('error, EXIT')
#     out_white('text-auto')
#     for proc in psutil.process_iter():
#         if proc.name() == 'python.exe':
#             proc.terminate()



# model = vosk.Model("J:\\Stella\\stellaPR\\vosk_model_small_ru_0.4")


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
            
