import requests
from pushbullet import Pushbullet
from bs4 import BeautifulSoup

def send_notification(title, message):
    pb.push_note(title, message)
    #pb.push_note(title, message, device_iden=otherDevice)
    print("Bildirim gönderildi!")

def save_to_file(url):
    with open(file_name, "a+") as file:
        file.write(url + "\n")
    
def existst_in_file(url):
    with open(file_name, "a+") as file:
        file.seek(0)
        for line in file:
            if url.strip() == line.strip():
                return True
    return False

url = "https://biletinial.com/tr-tr/spor"
base_url = "https://biletinial.com"
ntf_token = "o.K6iy3ZCCaiJ7iDZOsmdzN02vzkSbBTbp"
pb = Pushbullet(ntf_token)
otherDevice = "id"
file_name = "fetched.txt"
version_volleyball = "144" #144

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

events = soup.find('div', class_='voleybolDetay_fikstur').find('ul').find_all('li', attrs={'data-version': version_volleyball})

for event in events:
    eventName = event.find('div', class_='voleybolDetay_fikstur-takimlar text-center').get_text()
    eventLink = event.get('data-link')
    eventLink = base_url + eventLink
    if existst_in_file(eventLink):
        continue;
    send_notification(eventName, eventLink)
    save_to_file(eventLink)



