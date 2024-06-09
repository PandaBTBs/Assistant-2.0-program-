import os
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
import random



VE_NAME = ('Стелла')

VA_ALIAS = ('ассистент', 'робот', 'стелла', 'стела', 'стала', 'стоило')

VA_TBR = ('ответь', 'переведи', 'скажи', 'говори', 'сколько вермя')

VA_CMD_LIST = {
        "list": ('список команд', 'команды', 'что ты умеешь'),
        
        "time": ('время', 'текущее время', 'сейчас времени', 'который час'),
        
        "open_browser": ( 'гугл хром', 'браузер'),
        
        "history": ('тетрадь'),
        
        "open_browser_steam": ('стим', 'запусти стим'),
        
        "open_browser_server": ('сервер', 'запусти сервер'),
    
        "open_sharex": ('снимок экрана', 'запусти снимок'),
        
        "open_OBS": ('запись', 'запись экрана'),
        
        "open_vs": ('код', 'программирование'),
        
        "open_vtube": ('аватар', 'виртуальная студия'),
        
        "open_discord": ('общение', 'друзья'),
        
        "joke": ('расскажи анекдот', 'шутка', 'расскажи шутку', 'пошути'),
        
        "history": ('истории','навык'),
        
        "exit": ( 'заврешение работы', 'конец работы', 'закрыть')
        
    }

print(f"{VE_NAME}", f"{VA_ALIAS}", tts.va_speak("Ассистент, начал свою работу"))


print('--Список команд:-- \n- list: список команд, команды, что ты умеешь\n- time: время, текущее время, сейчас времени, который чаc\n - history: навык,\n- open_browser: гугл хром, браузер\n- open_steam: стим, запусти стим \n- open_browser_server: сервер, запусти сервер \n- open_sharex: снимок, снимок экрана \n- open_OBS: запись, запись экрана \n- open_vs: код, программирование \n- open_vtube: аватар, виртуальная студия \n- open_discord: общение, друзья \n- joke: расскажи анекдот, рассмеши, шутка, расскажи шутку, пошути, развесели\n- exit: заврешение работы, конец работы, закрыть\n\n')






def va_respond(voice: str):
    print(voice)
    if voice.startswith(VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in VA_CMD_LIST.keys():
            tts.va_speak("чего тебе надо? , скажи моё имя, а потом команды!")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice
    
    for x in VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in VA_TBR:
        cmd = cmd.replace(x, "").strip()
    
    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

def execute_cmd(cmd: str):
    if cmd == 'list':
        # help
        text = "Я умею следующие команды: ..."
        text += "рассказывать анекдот+ы ..."
        text += "рассказывать стих+и ..."
        text += "открыв+ать браузер, сайты..." 
        text += 'запускать приложения...'
        tts.va_speak(text)
        pass
    
    elif cmd == 'time':
        now = datetime.datetime.now()
        text = "В данный момент " + num2text(now.hour) + ":"  + num2text(now.minute)
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['конечно, я могу рассказать парочку шуток. Например: какая боль, какая боль, повсюду скидки, а денег - ноль', 'конечно, я могу рассказать парочку шуток. Например: сколько программистов нужно, чтобы вкрутить одну лампочку?']
        tts.va_speak(random.choice(jokes))
        
    elif cmd == 'open_browser':
        text = 'открываю браузер'
        tts.va_speak(text)
        webbrowser.open("https://www.google.ru/?hl=ru")
        text1 = 'открыла браузер'
        tts.va_speak(text1)
        
        
    elif cmd == 'open_browser_server':
        text = 'открываю сервер веб ю'
        tts.va_speak(text)
        webbrowser.open("https://127.0.0.1:7860")
        text1 = 'открыла сервер веб ю'
        tts.va_speak(text1)
        
    elif cmd == 'open_browser_steam':
        text = 'Открываю стим'
        tts.va_speak(text)
        webbrowser.open('https://store.steampowered.com/?l=russian')
        text1='открыла стим'
        tts.va_speak(text1)   
        
    elif cmd == 'open_OBS':
        text = 'Открываю запись экрана'
        tts.va_speak(text)
        webbrowser.open("steam://rungameid/1905180")
        text1='открыла запись'
        tts.va_speak(text1)  
        
    elif cmd == 'open_vs':
        text = 'Открываю кодинг'
        tts.va_speak(text)
        os.startfile(r'J:\Microsoft VS Code\Code.exe')
        text1='открыла'
        tts.va_speak(text1)
        
    elif cmd == 'open_discord':
        text = 'Открываю дискорд'
        tts.va_speak(text)
        webbrowser.open('https://discord.com/channels/@me')
        text1='открыла'
        tts.va_speak(text1)
        
    elif cmd == 'open_vtube':
        text = 'Открываю виртулальную студию'
        tts.va_speak(text)
        webbrowser.open('steam://rungameid/1325860')
        text1='открыла'
        tts.va_speak(text1) 
        

    elif cmd == 'open_sharex':
        text = 'Открываю снимок экрана'
        tts.va_speak(text)
        os.startfile(r'D:/steamT1/steamapps/common/ShareX/ShareX_Launcher')
        text1='открыла'
        tts.va_speak(text1)       
        
    elif cmd  == "exit":
        text = "выключаюсь"
        tts.va_speak(text)
        quit()
    
    elif cmd == 'history':
        tts.va_speak('Хорошо, активирован, навык, истории, Какую историю, Вы, хотите выбрать?')
        print('pls input History: hs1, hs2, hs3')
        
        uy = str(input())
  
        
        if uy == 'hs1':
            print('---------------------history-1---------------------')
            text = 'Хорошо, давайте, придумаем, занимательную историю'
            text+= 'Объяснительная, об, опоздании'
            tts.va_speak(text)
        
        
            tts.va_speak('Для начала, скажи, куда мы опоздали')
            locally_1 = str(input())
        
            tts.va_speak('теперь, назови животное, муж+ского рода')
            genus_m = str(input())
        
            tts.va_speak('теперь, назови, животное, женского рода')
            genus_w = str(input())
        
            tts.va_speak('где?')
            locally_2 = str(input())
        
            tts.va_speak('животное, во множественном, числе')
            animals = str(input())
        
            tts.va_speak('куда?')
            locally_3 = str(input())
        
            tts.va_speak('и, на последок, скажи, имя, твоего знакомого')
            input_us = str(input())
        
            tts.va_speak(f'И так, объяснительная, сегодня когда я шёл {locally_1}, \
            на меня внезапно свалился мокрый {genus_m}, я закричал как {genus_w},\
            и потерял сознание, очнулся я в {locally_2}, и сказал, отвезите меня {locally_1},\
            мне очень надо, но эти мои {animals}, почему то, отвезли меня {locally_3},\
            и от туда, я шёл пешком, пока меня не подвёз пьяный {input_us}. Вот, почему я опоздал\
            на {locally_1}. Мне кажется, получилось прикольно. Хотите, соченить еще?')
            
            print('pls input number_history') 
            intHS1 = str(input())
            
            if intHS1 == 'hs2':
                print('---------------------history-2---------------------')
                text = 'Отлично,'
                text+= 'Текст, про, ци+рк'
                tts.va_speak(text)
            
                tts.va_speak('Для начала, назови, знаменитого мужчину')    
                puple_1 = str(input())
            
                tts.va_speak('какой?')    
                quality_1 = str(input())
            
                tts.va_speak('Назови, еще, одного, знаменитого мужчину')    
                puple_2 = str(input())
            
                tts.va_speak('Какой? в несколько слов')    
                quality_2 = str(input())
            
                tts.va_speak('Теперь ,назови, предмет, мужчкого рода')    
                item_1 = str(input())
            
                tts.va_speak('Какой?')    
                quality_item = str(input())
            
                tts.va_speak('Назови, ещё, один предмет, мужчкого рода')    
                item_2= str(input())
            
                tts.va_speak('И, последний вопрос. Какой?')    
                quality_3 = str(input())
            
            
                tts.va_speak(f'Внимание!!, вот что получилось,: вчера, я ходила в цирк, сначала на арену, \
            выскочил {quality_1}, {puple_1}, за ним выполз {quality_2}, {puple_2}, и они бросались тухлой рыбой целый час,\
            за тем вышел, клоун у которого в руках был {item_2}, клоун бросил этот{item_2} в зрителей,\
            и попал прямо в меня. Я обидилась, Достала из своего кармана {quality_3}, {item_1}, \
            кинула в клоуна, и попала, прямо в лоб. Мне понравился этот цирк. По моему, получилась прикольная история. Соченим еще?')
        
            if intHS1 == 'hs3':
                print('---------------------history-3---------------------')
                text = 'Извини,'
                text+= ',Но она недоступна,'
                text+='введи, занчение ноль,-0-, или любое, другое'
                tts.va_speak(text)
                print(text)
                pass2=str(input())
                if pass2 == '0':
                    pass
                else:
                    pass
        
            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass
            
            
        if uy == 'hs2':
            print('---------------------history-2---------------------')
            text = 'Отлично,'
            text+= 'Текст, про, ци+рк'
            tts.va_speak(text)
            
            tts.va_speak('Для начала, назови, знаменитого мужчину')    
            puple_1 = str(input())
            
            tts.va_speak('какой?')    
            quality_1 = str(input())
            
            tts.va_speak('Назови, еще, одного, знаменитого мужчину')    
            puple_2 = str(input())
            
            tts.va_speak('Какой? в несколько слов')    
            quality_2 = str(input())
            
            tts.va_speak('Теперь ,назови, предмет, мужчкого рода')    
            item_1 = str(input())
            
            tts.va_speak('Какой?')    
            quality_item = str(input())
            
            tts.va_speak('Назови, ещё, один предмет, мужчкого рода')    
            item_2= str(input())
            
            tts.va_speak('И, последний вопрос. Какой?')    
            quality_3 = str(input())
            
            
            tts.va_speak(f'Внимание!!, вот что получилось,: вчера, я ходила в цирк, сначала на арену, \
            выскочил {quality_1}, {puple_1}, за ним выполз {quality_2}, {puple_2}, и они бросались тухлой рыбой целый час,\
            за тем вышел, клоун у которого в руках был {item_2}, клоун бросил этот{item_2} в зрителей,\
            и попал прямо в меня. Я обидилась, Достала из своего кармана {quality_3}, {item_1}, \
            кинула в клоуна, и попала, прямо в лоб. Мне понравился этот цирк. По моему, получилась прикольная история. Соченим еще?')
            
            
            print('pls input number_history') 
            intHS2 = str(input()) 
            
            
            if intHS2 == 'hs1':
                print('---------------------history-1---------------------')
                text = 'Хорошо, давайте, придумаем, занимательную историю'
                text+= 'Объяснительная, об, опоздании'
                tts.va_speak(text)
        
        
                tts.va_speak('Для начала, скажи, куда мы опоздали')
                locally_1 = str(input())
        
                tts.va_speak('теперь, назови животное, муж+ского рода')
                genus_m = str(input())
        
                tts.va_speak('теперь, назови, животное, женского рода')
                genus_w = str(input())
        
                tts.va_speak('где?')
                locally_2 = str(input())
        
                tts.va_speak('животное, во множественном, числе')
                animals = str(input())
        
                tts.va_speak('куда?')
                locally_3 = str(input())
        
                tts.va_speak('и, на последок, скажи, имя, твоего знакомого')
                input_us = str(input())
        
                tts.va_speak(f'И так, объяснительная, сегодня когда я шёл {locally_1}, \
            на меня внезапно свалился мокрый {genus_m}, я закричал как {genus_w},\
            и потерял сознание, очнулся я в {locally_2}, и сказал, отвезите меня {locally_1},\
            мне очень надо, но эти мои {animals}, почему то, отвезли меня {locally_3},\
            и от туда, я шёл пешком, пока меня не подвёз пьяный {input_us}. Вот, почему я опоздал\
            на {locally_1}. Мне кажется, получилось прикольно. Хотите, соченить еще?')
            
            print('pls input number_history') 
            intHS3 = str(input())
            
            if intHS3  == 'hs3':
                print('---------------------history-3---------------------')
                text = 'Извини,'
                text+= ',Но она недоступна,'
                text+='введи, занчение ноль,-0-, или любое, другое'
                tts.va_speak(text)
                print(text)
                pass2=str(input())
                if pass2 == '0':
                    pass
                else:
                    pass
             
            if intHS2 == 'hs3':
                print('---------------------history-3---------------------')
                text = 'Извини,'
                text+= ',Но она недоступна,'
                text+='введи, занчение ноль,-0-, или любое, другое'
                tts.va_speak(text)
                print(text)
                pass2=str(input())
                if pass2 == '0':
                    pass
                else:
                    pass

            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass


        if uy  == 'hs3':
            print('---------------------history-3---------------------')
            text = 'Извини,'
            text+= ',Но она недоступна,'
            text+='введи, занчение ноль,-0-, или любое, другое'
            tts.va_speak(text)
            print(text)
            pass2=str(input())
            if pass2 == '0':
                pass
            else:
                pass
    
stt.va_listen(va_respond)
