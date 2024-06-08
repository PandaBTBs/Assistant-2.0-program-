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
    
    
def model_change(speech):
    if speech == 'aidar':
        return 1
    elif speech == 'baya':
        return 2
    elif speech == 'kseniya':
        return 3
    elif speech == 'xenia':
        return 3
    

speaker = 'baya'

time.sleep(1)
out_yellow('. \n\
                continue without selecting a model & - input: on/off  / \n\n\
                #-NOactive-# would you like to customize the vosk model and voice & - input: model \n\n\
                if you want to activate the skill - entertaining stories, \n\
                then enter(after downloading): hs1, hs2, hs3 \n\
                --do you want to skip? enter any value')
    
p  = str(input())
if p == 'on': 
        print('--------start jmonge--------')
        pass
elif p == 'off':
    out_yellow('--------off pr*******--------')
    out_white('text-auto')
    for proc in psutil.process_iter():
        if proc.name() == 'python.exe':
            proc.terminate()
                
        
elif p == 'model':
            
    print('input speech: aidar, baya, kseniya, xenia')
        
    speech = str(input())
        
            
    if model_change(speech) == 1:
            out_red('speech finish installed: aidar')
            out_red('-------------------------start-------------------------')
            out_white('text-auto')
            speaker = 'aidar' 
    
    elif model_change(speech) == 2:
            out_red('speech finish installed: baya')
            out_red('-------------------------start-------------------------')
            out_white('text-auto')
            speaker = 'baya'
    
    elif model_change(speech) == 3:
            out_red('model_vosk and speech finish installed: kseniya')
            out_red('-------------------------start-------------------------')
            out_white('text-auto')
            speaker = 'kseniya'
    
    elif model_change(speech) == 4:
            out_red('model_vosk and speech finish installed: xenia')
            out_red('-------------------------start-------------------------')
            out_white('text-auto')
            speaker = 'xenia'
            
        
    else:
        out_red('error, EXIT')
        out_white('text-auto')
        for proc in psutil.process_iter():
            if proc.name() == 'python.exe':
                proc.terminate()
        
else:
    out_yellow('--------no list cmds, close pr................--------')
    out_white('text-auto')
    for proc in psutil.process_iter():
        if proc.name() == 'python.exe':
            proc.terminate()



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
