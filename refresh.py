import requests

def refresh():    
    
    headers = {'authority' : 'disnity.com' , 'path' : '/api/server/refresh/874183024483377193', 'referer' : 'https://disnity.com/' , 'cookie' : '_ga=GA1.1.1233460131.1640572155; __gads=ID=e582b49cab592b91-22da57b68ccf00c1:T=1640572155:RT=1640572155:S=ALNI_May2vdCHFNt6jh3t-0fPjYxvs4pZg; disnity.sid=s%3APmYaqQbZ7mnZjswBcqoRg3zNPOQtzliH.PbZyoLwW9xZzXpEhV%2BbfrbOUw0EsEarLxq2Bp%2BHtdIk; _ga_TQQHGYWJYE=GS1.1.1642510692.3.1.1642510713.0'}
    response = requests.get(url="https://disnity.com/api/server/refresh/874183024483377193" , headers = headers )
    
    return response.status_code
    

refresh()
