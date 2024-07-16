import requests
from bs4 import BeautifulSoup 

inp = input('Weather or time ')

cookies = {
    'TADANON': 'SDg0K01XZU14L2haY2tGNFI0ejZpOTB5WVpDZEJLanpPc2hTMkdKOHduWVRVMDdmZytQcGpSTzcxaGFpWktlKw--',
    '_sharedID': '79049df9-f63b-40e9-b2ac-37be65abd6e9',
    '_sharedID_cst': 'zix7LPQsHA%3D%3D',
    '__qca': 'P0-1044938889-1704077553940',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_sharedid': '836d9438-40a9-43d7-b11f-efab808ddb65',
    '_cc_id': 'fd671d0c3af659592a1591d3f2a5c96c',
    'panoramaId_expiry': '1704682355873',
    'panoramaId': 'dee852cb74dcfe775cab9872cdb94945a7020df6b7d4003b84663f9c4ae19ac1',
    'panoramaIdType': 'panoIndiv',
    'cto_bidid': 'nwDe6F8zRXJwM09kd2xZQUJHMUhwUldOMjloejhGTjZtNjM5UURHOGhpSlhiViUyQjdzTnolMkY0dnBFZSUyRiUyQktLaUswVzBPMm9POE1DJTJCZSUyRmo5NUp1QkprdW9sbkpubjNLakdVa0xmb09UNiUyQnVtQVlCZEE1SHpOSll1amhXd1MxSHglMkZmV2x0cmM',
    'cto_bundle': 'QwWgNl82bzJ1bnFqbTNKT294Z2lzS1g4SUxHdGlsQUdGem5WSmVjSmZYQmxwcWFWVWYxZGp3OUJ4RnZoeHNJQjI5ZHIlMkZNeTRSMTNDRTVOTjVlbDZ5QXlOTXMlMkJmVnlVeUMyRmtFTiUyRlVabGVnY1F4cUxKa0tmQTQzaFR3TFNCJTJGOG1LTDBMcXd4SUFuJTJGWWoweWJkNmZWWHA3V0dqenJxVllObGpiNkoyJTJGdjIzQmFwWCUyQkVRQk1tQmVocFFLM3dPMyUyRjc4a2RMdmw3STR6NWw2NUslMkZ6UTBPNjVjeHVBJTNEJTNE',
}

headers = {
    'authority': 'www.timeanddate.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'TADANON=SDg0K01XZU14L2haY2tGNFI0ejZpOTB5WVpDZEJLanpPc2hTMkdKOHduWVRVMDdmZytQcGpSTzcxaGFpWktlKw--; _sharedID=79049df9-f63b-40e9-b2ac-37be65abd6e9; _sharedID_cst=zix7LPQsHA%3D%3D; __qca=P0-1044938889-1704077553940; _pbjs_userid_consent_data=3524755945110770; _sharedid=836d9438-40a9-43d7-b11f-efab808ddb65; _cc_id=fd671d0c3af659592a1591d3f2a5c96c; panoramaId_expiry=1704682355873; panoramaId=dee852cb74dcfe775cab9872cdb94945a7020df6b7d4003b84663f9c4ae19ac1; panoramaIdType=panoIndiv; cto_bidid=nwDe6F8zRXJwM09kd2xZQUJHMUhwUldOMjloejhGTjZtNjM5UURHOGhpSlhiViUyQjdzTnolMkY0dnBFZSUyRiUyQktLaUswVzBPMm9POE1DJTJCZSUyRmo5NUp1QkprdW9sbkpubjNLakdVa0xmb09UNiUyQnVtQVlCZEE1SHpOSll1amhXd1MxSHglMkZmV2x0cmM; cto_bundle=QwWgNl82bzJ1bnFqbTNKT294Z2lzS1g4SUxHdGlsQUdGem5WSmVjSmZYQmxwcWFWVWYxZGp3OUJ4RnZoeHNJQjI5ZHIlMkZNeTRSMTNDRTVOTjVlbDZ5QXlOTXMlMkJmVnlVeUMyRmtFTiUyRlVabGVnY1F4cUxKa0tmQTQzaFR3TFNCJTJGOG1LTDBMcXd4SUFuJTJGWWoweWJkNmZWWHA3V0dqenJxVllObGpiNkoyJTJGdjIzQmFwWCUyQkVRQk1tQmVocFFLM3dPMyUyRjc4a2RMdmw3STR6NWw2NUslMkZ6UTBPNjVjeHVBJTNEJTNE',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://www.timeanddate.com/worldclock/kazakstan/astana', cookies=cookies, headers=headers)
# print(response.text)
src = response.text

soup = BeautifulSoup(src, 'html.parser')

def get_time():
    print(soup.find(id="ct", class_='h1').text)

def get_weather():
    print(soup.find(id='wt-tp').text)



if 'weather' in inp or '1' in inp:
    get_weather()
elif 'time' in inp or '2' in inp:
    get_time()
else:
    print('try again')
