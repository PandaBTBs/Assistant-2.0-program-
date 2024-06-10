import torch
import sounddevice as sd
import time
import psutil


def out_red(text):
    print("\033[31m {}" .format(text))
    
def out_yellow(text):
    print("\033[33m {}" .format(text))
    
def out_blue(text):
    print("\033[36m {}" .format(text))

def out_white(text):
    print("\033[39m {}" .format(text))
    

def model_change(f_open):
    if f_open == 'aidar':
        return 1

def model_change(f_open):
    if f_open == 'baya':
        return 2

def model_change(f_open):
    if f_open == 'kseniya':
        return 3

def model_change(f_open):
    if f_open == 'xenia':
        return 4
    
    
f = open('speech.txt', 'r', encoding='utf-8')
f_open = f.read()


speaker = 'baya'

if model_change(f_open) == 1:
    print('aidar')
    speaker = 'aidar'

if model_change(f_open) == 2:
    print('baya')
    speaker = 'baya'

if model_change(f_open) == 3:
    print('kseniya')
    speaker = 'kseniya'

if model_change(f_open) == 4:
    print('xenia')
    speaker = 'xenia'
    
else:
    print('baya')
    speaker = 'baya'

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000 # 48000

put_accent = True
put_yo = True
device = torch.device('cpu') 



model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)



def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5 )
    sd.stop()
