import json 

with open('J:\\Pack_Ai\\Stella\\stellaPR\\j134.json', 'r', encoding='utf-8') as json_file:
	j134 = json.load(json_file)

with open('J:\\Pack_Ai\\Stella\\stellaPR\\j134.json', 'w', encoding='utf-8') as json_file:
	json.dump(j134, json_file, indent=2)


print(j134["cmd_list"])


name = tuple(j134["name"])

alt_name = tuple(j134["alt_name"])

short_programs = tuple(j134["short_programs"])

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