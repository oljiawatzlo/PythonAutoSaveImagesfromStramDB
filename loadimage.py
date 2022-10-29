import urllib.request as urllib2
import pandas as pd
import time



df = pd.read_excel('D:/Python Playground/PytonJinja2/game.xlsx', sheet_name='Sheet1')
#df.rename({"Round" : "Price(Baht)"}, axis=1, inplace=True)

def download_image1(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib2.urlretrieve(url, full_path)

def download_image2(url, file_name):
    request = urllib2.Request(url)
    img = urllib2.urlopen(request).read()
    with open (file_name + '.jpg', 'w') as f: f.write(img)

for i in df['ID'].to_list():

    print(str(i))

    url = "https://cdn.cloudflare.steamstatic.com/steam/apps/" + "{}".format(str(i)) + "/header.jpg"

    download_image1(url, "images/", str(i))
#    download_image2(url, str(i))

    time.sleep(2)


