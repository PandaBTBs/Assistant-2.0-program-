import os
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
import random
import replicate




name = ('ассистент')

alt_name = ('ассистент', 'робот', 'Алиса')

short_programs = ('ответь', 'переведи', 'скажи', 'говори', 'сколько вермя')

cmd_list = {
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
        
        "chat_llama": ('Ответ', 'Вопрос'),
        
        "work_zone": ('рабочая зона', 'зона'),
        
        "exit": ( 'заврешение работы', 'конец работы', 'закрыть')
        
    }

print(f"{name}", f"{alt_name}", tts.va_speak("Ассистент, начал свою работу"))


print('--Список команд:-- \n- list: список команд, команды, что ты умеешь\n- time: время, текущее время, сейчас времени, который чаc\n - history: навык,\n- open_browser: гугл хром, браузер\n- open_steam: стим, запусти стим \n- open_browser_server: сервер, запусти сервер \n- open_sharex: снимок, снимок экрана \n- open_OBS: запись, запись экрана \n- open_vs: код, программирование \n- open_vtube: аватар, виртуальная студия \n- open_discord: общение, друзья \n- joke: расскажи анекдот, рассмеши, шутка, расскажи шутку, пошути, развесели\n- exit: заврешение работы, конец работы, закрыть\n\n')


def va_respond(voice: str):
    print(voice)
    if voice.startswith(alt_name):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in cmd_list.keys():
            tts.va_speak("чего тебе надо? , скажи моё имя, а потом команды!")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice
    
    for x in alt_name:
        cmd = cmd.replace(x, "").strip()

    for x in short_programs:
        cmd = cmd.replace(x, "").strip()
    
    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in cmd_list.items():

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
        
    elif cmd == 'work_zone':
        tts.va_speak('Открываю рабочую зону')
        
        webbrowser.open("https://www.google.ru/?hl=ru")
        os.startfile(r'J:\Microsoft VS Code\Code.exe')
        os.startfile(r'D:/steamT1/steamapps/common/ShareX/ShareX_Launcher')
    
    
    
    # BETA
    
    elif cmd == 'chat_llama':
        tts.va_speak('Хорошо, можете задать любой вопрос, и я, постараюсь ответить на него.')
        import json, pyaudio
        from vosk import Model, KaldiRecognizer

        model = Model("vosk_model_small_ru_0.4")
        rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                frames_per_buffer=8000)

        stream.start_stream()

        def lisen():
            while True:
                data = stream.read(4000, exception_on_overflow=False)
                if (rec.AcceptWaveform(data)) and (len(data) > 0):
                    answer = json.loads(rec.Result())
                    if answer['text']:
                        yield answer['text']
                
        for text in lisen():
            print(text)

            # Point to the local server
            from openai import OpenAI
            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
            True_chat = True
            while True_chat == True:

                if True_chat == True:
            
                    completion = client.chat.completions.create(
                model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
                messages=[
                {"role": "system", "content": "Always answer briefly."},
                {"role": "user", "content": text} 
                ],
                temperature=0.5,
                )


                    l = str(completion.choices[0].message)
                    print(completion.choices[0].message)
                    tts.va_speak(l)
                    break

        # tts.va_speak('Хорошо, можете задать любой вопрос, и я, постараюсь ответить на него.')

        # fileW_save = open('chat_save.txt', 'a', encoding='utf-8') # print chat
        # print('-AI_chat- \n input your your question: \n Для выхода: -выход- / -exit-' )

        # from openai import OpenAI

        # # Point to the local server
        # client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        # True_chat = True
        # while True_chat == True:

        #     if True_chat == True:

        #         login = str(input())


        #         if login == 'выход' or login == 'exit':
        #             break
        #         else: 
        #             fileW_save.write(f'Login: {login} \n')

        #             completion = client.chat.completions.create(
        #             model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
        #             messages=[
        #             {"role": "system", "content": "Always answer briefly."},
        #             {"role": "user", "content": login} 
        #             ],
        #             temperature=0.7,
        #             )


        #             l = str(completion.choices[0].message)
        #             fileW_save.write(f'AI: {l} \n')

        #             print(completion.choices[0].message)

        #             tts.va_speak(l)

                 
    elif cmd == 'history':
        tts.va_speak('Хорошо, активирован, навык, истории, Какую историю, Вы, хотите выбрать?')
        print('pls input History: hs1, hs2, hs3, hs4')
        
        hs = str(input())
        
        
        if hs == 'hs1':
            print('---------------------history-1---------------------')
            text = 'Хорошо, давайте, придумаем занимательную историю,'
            text+= 'Объяснительная, об, опоздании'
            tts.va_speak(text)
        
        
            tts.va_speak('Для начала, скажи, куда мы опоздали')
            locally_1 = str(input())
        
            tts.va_speak('теперь, назови животное, мужского рода')
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
             {locally_1}. Мне кажется, получилось прикольно. Хотите, соченить еще?')
            
            print('pls input number_history') 
            intHS1 = str(input())
            
            if intHS1 == 'hs2':
                print('---------------------history-2---------------------')
                text = 'Отлично,'
                text+= 'Текст, про цирк'
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
                intHS2  = str(input())
        
            if intHS1 == 'hs3' or intHS2 == 'hs3':
                print('---------------------history-3---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп, для близнецов'
                tts.va_speak(text)
            
                tts.va_speak('Для начал, назови своего любимого актёра')
                hs3_1 = str(input())
            
                tts.va_speak('Какое любимое занятие, у этого человека?')
                hs3_2 = str(input())
            
                tts.va_speak('Теперь, назови имя человека, который тебе не нравится')
                hs3_3 = str(input())
            
                tts.va_speak('Как думаешь, чем любит заниматься этот человек?')
                hs3_4 = str(input())
            
                tts.va_speak('И, на последок, какие люди тебя окружают?')
                hs3_5 = str(input())
            
                tts.va_speak(f'Весной вам вдруг покажется, что у вас раздвоение личности. Вы вроде {hs3_1}, ив тоже время\
                {hs3_3}. временами они будут ругаться, и очень утомлять, Вас, этим. Осенью у вас могут появиться вредные привычки\
                , такие как {hs3_2} ночью на крыше, {hs3_4}, на красной площади, ковырять в насу, с крикаим нашёл.  В декабре,\
                в Кремле, вам вручат золотоую медаль, {hs3_5}, близнецы страны. Почаще советуйтесь со своим внуртенним голосом. И всё будет отлично.\
                Я думаю получилось неплохо, придумаем ещё?')
                
                intHS3 = str(input())
            
            
        
            if intHS1 == 'hs4' or intHS2 == 'hs4' or intHS3 == 'hs4':
                print('---------------------history-4---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп для тельцов.'
                tts.va_speak(text)
            
                tts.va_speak('Сперва, назови существо, мужского рода.')
                hs4_1 = str(input())     
            
                tts.va_speak('Теперь, какойнибудь напиток.')
                hs4_2 = str(input())  
            
                tts.va_speak('Какой?')
                hs4_3 = str(input()) 
            
                tts.va_speak('Назови имя, кинозвезды...')
                hs4_4 = str(input())

                tts.va_speak('Теперь, большой предмет, женского рода.')
                hs4_5 = str(input())
            
                tts.va_speak('И последнее, назови число, которе тебе не нравиться.')
                hs4_6 = str(input())
            
                tts.va_speak(f'И так, гороскоп для тельцов. Ваша любимая рифма - телец, молодец, и это правда. Вам всё\
                удаётся, и друзья завидуя, называют вас {hs4_3}, {hs4_1}. Весной вы поставите рекорд, выпьете залпом\
                {hs4_6} своего любимого напитка, {hs4_2}, а ещё, вы получите приглашение на телевидение, где вас\
                будет ждать большая {hs4_5}, которую вручит {hs4_4}. Не надо нинакого бычиться, и всё будет превосходно.\
                По-моему, чудесный гороскоп. Давай придумаем что-то ещё?')
        
            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass
            
            
        if hs == 'hs2':
            print('---------------------history-2---------------------')
            text = 'Отлично,'
            text+= 'Текст, про, цирк'
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
            intHS4 = str(input()) 
            
            
            if intHS4 == 'hs1':
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
                {locally_1}. Мне кажется, получилось прикольно. Хотите, соченить еще?')
            
                print('pls input number_history') 
            
                intHS5 = str(input())
                                
            if intHS4 == 'hs3' or intHS5 == 'hs3':
                print('---------------------history-3---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп, для близнецов'
                tts.va_speak(text)
            
                tts.va_speak('Для начал, назови своего любимого актёра')
                hs3_1 = str(input())
            
                tts.va_speak('Какое любимое занятие, у этого человека?')
                hs3_2 = str(input())
            
                tts.va_speak('Теперь, назови имя человека, который тебе не нравится')
                hs3_3 = str(input())
            
                tts.va_speak('Как думаешь, чем любит заниматься этот человек?')
                hs3_4 = str(input())
            
                tts.va_speak('И, на последок, какие люди тебя окружают?')
                hs3_5 = str(input())
            
                tts.va_speak(f'Весной вам вдруг покажется, что у вас раздвоение личности. Вы вроде {hs3_1}, ив тоже время\
                {hs3_3}. временами они будут ругаться, и очень утомлять, Вас, этим. Осенью у вас могут появиться вредные привычки\
                , такие как {hs3_2} ночью на крыше, {hs3_4}, на красной площади, ковырять в насу, с крикаим нашёл.  В декабре,\
                в Кремле, вам вручат золотоую медаль, {hs3_5}, близнецы страны. Почаще советуйтесь со своим внуртенним голосом. И всё будет отлично.\
                Я думаю получилось неплохо, придумаем ещё?')

                intHS6 = str(input())
            
        
            if intHS4 == 'hs4' or intHS5 == 'hs4' or intHS6 == 'hs4':
                print('---------------------history-4---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп для тельцов.'
                tts.va_speak(text)
            
                tts.va_speak('Сперва, назови существо, мужского рода.')
                hs4_1 = str(input())     
            
                tts.va_speak('Теперь, какойнибудь напиток.')
                hs4_2 = str(input())  
            
                tts.va_speak('Какой?')
                hs4_3 = str(input()) 
            
                tts.va_speak('Назови имя, кинозвезды...')
                hs4_4 = str(input())

                tts.va_speak('Теперь, большой предмет, женского рода.')
                hs4_5 = str(input())
            
                tts.va_speak('И последнее, назови число, которе тебе не нравиться.')
                hs4_6 = str(input())
            
                tts.va_speak(f'И так, гороскоп для тельцов. Ваша любимая рифма - телец, молодец, и это правда. Вам всё\
                удаётся, и друзья завидуя, называют вас {hs4_3}, {hs4_1}. Весной вы поставите рекорд, выпьете залпом\
                {hs4_6} своего любимого напитка, {hs4_2}, а ещё, вы получите приглашение на телевидение, где вас\
                будет ждать большая {hs4_5}, которую вручит {hs4_4}. Не надо нинакого бычиться, и всё будет превосходно.\
                По-моему, чудесный гороскоп. Давай придумаем что-то ещё?')
                print('pls input number_history') 

            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass
               
                   
        if hs == 'hs3':
            print('---------------------history-3---------------------') 
            text = 'Хорошо, давайте, придумаем занимательную историю,'
            text+= 'Гороскоп, для близнецов'
            tts.va_speak(text)
            
            tts.va_speak('Для начал, назови своего любимого актёра')
            hs3_1 = str(input())
            
            tts.va_speak('Какое любимое занятие, у этого человека?')
            hs3_2 = str(input())
            
            tts.va_speak('Теперь, назови имя человека, который тебе не нравится')
            hs3_3 = str(input())
            
            tts.va_speak('Как думаешь, чем любит заниматься этот человек?')
            hs3_4 = str(input())
            
            tts.va_speak('И, на последок, какие люди тебя окружают?')
            hs3_5 = str(input())
            
            tts.va_speak(f'Весной вам вдруг покажется, что у вас раздвоение личности. Вы вроде {hs3_1}, ив тоже время\
            {hs3_3}. временами они будут ругаться, и очень утомлять, Вас, этим. Осенью у вас могут появиться вредные привычки\
            , такие как {hs3_2} ночью на крыше, {hs3_4}, на красной площади, ковырять в насу, с крикаим нашёл.  В декабре,\
            в Кремле, вам вручат золотоую медаль, {hs3_5}, близнецы страны. Почаще советуйтесь со своим внуртенним голосом. И всё будет отлично.\
            Я думаю получилось неплохо, придумаем ещё?')
            
            print('pls input number_history') 
            intHS7 = str(input())
            
            if intHS7 == 'hs1':
                print('---------------------history-1---------------------')
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Объяснительная, об, опоздании'
                tts.va_speak(text)
        
        
                tts.va_speak('Для начала, скажи, куда мы опоздали')
                locally_1 = str(input())
        
                tts.va_speak('теперь, назови животное, мужского рода')
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
                intHS8 = str(input())
            
            if intHS7 == 'hs2' or intHS8 == 'hs2':
                print('---------------------history-2---------------------')
                text = 'Отлично,'
                text+= 'Текст, про цирк'
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
                intHS9 = str(input())
            
            if intHS7 == 'hs4' or intHS8 == 'hs4' or intHS9 == 'hs4':
                print('---------------------history-4---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп для тельцов.'
                tts.va_speak(text)
            
                tts.va_speak('Сперва, назови существо, мужского рода.')
                hs4_1 = str(input())     
            
                tts.va_speak('Теперь, какойнибудь напиток.')
                hs4_2 = str(input())  
            
                tts.va_speak('Какой?')
                hs4_3 = str(input()) 
            
                tts.va_speak('Назови имя, кинозвезды...')
                hs4_4 = str(input())

                tts.va_speak('Теперь, большой предмет, женского рода.')
                hs4_5 = str(input())
            
                tts.va_speak('И последнее, назови число, которе тебе не нравиться.')
                hs4_6 = str(input())
            
                tts.va_speak(f'И так, гороскоп для тельцов. Ваша любимая рифма - телец, молодец, и это правда. Вам всё\
                удаётся, и друзья завидуя, называют вас {hs4_3}, {hs4_1}. Весной вы поставите рекорд, выпьете залпом\
                {hs4_6} своего любимого напитка, {hs4_2}, а ещё, вы получите приглашение на телевидение, где вас\
                будет ждать большая {hs4_5}, которую вручит {hs4_4}. Не надо нинакого бычиться, и всё будет превосходно.\
                По-моему, чудесный гороскоп. Давай придумаем что-то ещё?')
            
            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass
            
            
            
        
        if hs == 'hs4':
            print('---------------------history-4---------------------') 
            text = 'Хорошо, давайте, придумаем занимательную историю,'
            text+= 'Гороскоп для тельцов.'
            tts.va_speak(text)
            
            tts.va_speak('Сперва, назови существо, мужского рода.')
            hs4_1 = str(input())     
            
            tts.va_speak('Теперь, какойнибудь напиток.')
            hs4_2 = str(input())  
            
            tts.va_speak('Какой?')
            hs4_3 = str(input()) 
            
            tts.va_speak('Назови имя, кинозвезды...')
            hs4_4 = str(input())

            tts.va_speak('Теперь, большой предмет, женского рода.')
            hs4_5 = str(input())
            
            tts.va_speak('И последнее, назови число, которе тебе не нравиться.')
            hs4_6 = str(input())
            
            tts.va_speak(f'И так, гороскоп для тельцов. Ваша любимая рифма - телец, молодец, и это правда. Вам всё\
            удаётся, и друзья завидуя, называют вас {hs4_3}, {hs4_1}. Весной вы поставите рекорд, выпьете залпом\
            {hs4_6} своего любимого напитка, {hs4_2}, а ещё, вы получите приглашение на телевидение, где вас\
            будет ждать большая {hs4_5}, которую вручит {hs4_4}. Не надо нинакого бычиться, и всё будет превосходно.\
            По-моему, чудесный гороскоп. Давай придумаем что-то ещё?')
            
            print('pls input number_history') 
            intHS10 = str(input())
            
            if intHS10 == 'hs1':
                print('---------------------history-1---------------------')
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Объяснительная, об, опоздании'
                tts.va_speak(text)
        
        
                tts.va_speak('Для начала, скажи, куда мы опоздали')
                locally_1 = str(input())
        
                tts.va_speak('теперь, назови животное, мужского рода')
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
                {locally_1}. Мне кажется, получилось прикольно. Хотите, соченить еще?')
            
                print('pls input number_history') 
                intHS11 = str(input())
            
            if intHS10 == 'hs2' or intHS11 == 'hs2':
                print('---------------------history-2---------------------')
                text = 'Отлично,'
                text+= 'Текст, про цирк'
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
                intHS12 = str(input())
            
            if intHS10 == 'hs3' or intHS11 == 'hs3' or intHS12 == 'hs3':
                print('---------------------history-3---------------------') 
                text = 'Хорошо, давайте, придумаем занимательную историю,'
                text+= 'Гороскоп, для близнецов'
                tts.va_speak(text)
            
                tts.va_speak('Для начал, назови своего любимого актёра')
                hs3_1 = str(input())
            
                tts.va_speak('Какое любимое занятие, у этого человека?')
                hs3_2 = str(input())
            
                tts.va_speak('Теперь, назови имя человека, который тебе не нравится')
                hs3_3 = str(input())
            
                tts.va_speak('Как думаешь, чем любит заниматься этот человек?')
                hs3_4 = str(input())
            
                tts.va_speak('И, на последок, какие люди тебя окружают?')
                hs3_5 = str(input())
            
                tts.va_speak(f'Весной вам вдруг покажется, что у вас раздвоение личности. Вы вроде {hs3_1}, ив тоже время\
                {hs3_3}. временами они будут ругаться, и очень утомлять, Вас, этим. Осенью у вас могут появиться вредные привычки\
                , такие как {hs3_2} ночью на крыше, {hs3_4}, на красной площади, ковырять в насу, с крикаим нашёл.  В декабре,\
                в Кремле, вам вручат золотоую медаль, {hs3_5}, близнецы страны. Почаще советуйтесь со своим внуртенним голосом. И всё будет отлично.\
                Я думаю получилось неплохо, придумаем ещё?')
            
            else:
                print('Выход, введите любое значение.')
                i = str(input())
                if i == 'exit':
                    pass
                else:
                    pass
    
stt.va_listen(va_respond)


