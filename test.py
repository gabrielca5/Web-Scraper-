from bs4 import BeautifulSoup
import requests
import pandas as pd 
import schedule
import time
import datetime
import pytz
import langchain as lc 

fuso_horario = pytz.timezone('America/Sao_Paulo')



def get_manchetes():
    url = 'https://g1.globo.com'
    horario = datetime.datetime.now(fuso_horario)
    hora_formatada = horario.strftime("%H:%M:%S")
    request = requests.get(url)

    soup = BeautifulSoup(request.text , 'html.parser')

    manchetes = [ ]
    contador = 1
    for elemento in soup.find_all('a' , class_= 'feed-post-link'):
        
        manchetes.append(f'Data:{hora_formatada} Manchete {contador}: {(elemento.get_text(strip= False))}')
        contador += 1
    df = pd.DataFrame(manchetes , columns=[f'Manchetes do dia '])

    df.to_csv('manchetes_g1.csv' , index= False)

    return 


get_manchetes()
schedule.every().day.at('06:30').do(get_manchetes)
schedule.every().day.at('08:30').do(get_manchetes)
schedule.every().day.at('10:30').do(get_manchetes)
schedule.every().day.at('12:30').do(get_manchetes)
schedule.every().day.at('14:30').do(get_manchetes)
schedule.every().day.at('16:30').do(get_manchetes)
schedule.every().day.at('18:30').do(get_manchetes)





print("Agendador rodando...")
print("Horários programados:", [str(job.next_run) for job in schedule.jobs])

while True:
    schedule.run_pending()
    time.sleep(1) 
