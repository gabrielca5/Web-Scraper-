from bs4 import BeautifulSoup
import requests
import pandas as pd 



url = 'https://g1.globo.com'

request = requests.get(url)

soup = BeautifulSoup(request.text , 'html.parser')

manchetes = [ ]
contador = 1
for elemento in soup.find_all('a' , class_= 'feed-post-link'):
    
    manchetes.append(f'Manchete {contador}: {(elemento.get_text(strip= False))}')
    contador += 1
df = pd.DataFrame(manchetes , columns=[f'Manchetes do dia '])

df.to_csv('manchetes_g1' , index= False)