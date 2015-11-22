import urllib
from bs4 import BeautifulSoup
from pymongo import MongoClient

fish_url = 'http://apollohospitalsbangalore.com/'
fish_url_com = 'http://apollohospitalsbangalore.com'

fish_url1 = 'http://www.fortishealthcare.com/india/'
fish_url_com1 = 'http://www.fortishealthcare.com/india/'

fish_url2 = 'http://www.fortishealthcare.com/'
fish_url_com2 = 'http://www.fortishealthcare.com/india/'




fish_url2 = 'http://www.vanivilashospital.in/'
fish_url_com2 = 'http://www.vanivilashospital.in/'

fish_url2 = 'http://www.sgito.org/'
fish_url_com2 = 'http://www.sgito.org/'


fish_url2 = 'http://www.hopkinsmedicine.org/the_johns_hopkins_hospital/'
fish_url_com2 = 'http://www.hopkinsmedicine.org/the_johns_hopkins_hospital/'

fish_url2 = 'http://www.massgeneral.org/'
fish_url_com2 = 'http://www.massgeneral.org/'


fish_url2 = 'http://my.clevelandclinic.org/'
fish_url_com2 = 'http://my.clevelandclinic.org/'




'''
fish_url2 = 'http://www.hosmatnet.com/'
fish_url_com2 = 'http://www.hosmatnet.com/'
'''
links = []
'''
def get_link(url):
    page = urllib.request.urlopen(url)
    html_doc = page.read()
    sock = urllib.request.urlopen(url) 
    htmlSource = sock.read()                            
    sock.close()   
    soup = BeautifulSoup(htmlSource)
    urllinks = []
    for link in soup.find_all('a'):
        
        links = link.get('href')
        links = str(links)
        if links.startswith('/') or fish_url in links:
            urllinks.append(links)
    return urllinks
'''
mongo_client = MongoClient()
db = mongo_client.hospitals
#db.drop_collection('Apollo_Hospital');
#db.drop_collection('Fortis_Hospital');
'''
    
def get_page(url):
    flag = 1
    try:
        page = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
        flag = 0
    if flag == 1:
        html_doc = page.read()
        sock = urllib.request.urlopen(url) 
        htmlSource = sock.read()                            
        sock.close()                                        
        soup = BeautifulSoup(htmlSource)
        links = soup.find_all("p")
        title = soup.find("title")
        for link in links:
            db.Apollo_Hospital.insert({"data": link.text,"title":title.text})




links = get_link(fish_url_com)
newlinks = []
print("................................................links......................................................")
for i in links:
    if fish_url not in i:
        i = fish_url_com + i
    newlinks.append(i)

print("................................................new_____links......................................................")

newlinks = list(set(newlinks))

print("................................................new____new______links......................................................")
del links[:]
for j in newlinks:
    get_page(j)






def get_link1(url):
    page = urllib.request.urlopen(url)
    html_doc = page.read()
    sock = urllib.request.urlopen(url) 
    htmlSource = sock.read()                            
    sock.close()   
    soup = BeautifulSoup(htmlSource)
    urllinks = []
    for link in soup.find_all('a'):
        links = link.get('href')
        links = str(links)
        if links.startswith('/') or fish_url1 in links:
            urllinks.append(links)
    return urllinks



def get_page1(url):
    req = ".pdf"
    if req not in url:
        flag = 1
        try:
            page = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            flag = 0
        if flag == 1:
            html_doc = page.read()
            sock = urllib.request.urlopen(url) 
            htmlSource = sock.read()                            
            sock.close()                                        
            soup = BeautifulSoup(htmlSource)
            links = soup.find_all("p")
            title = soup.find("title")
            for link in links:
                db.Fortis_Hospital.insert({"data": link.text,"title": title.text})





links = get_link1(fish_url_com1)
newlinks = []
print("................................................links......................................................")
for i in links:
    if fish_url1 not in i:
        i = fish_url_com1 + i
    newlinks.append(i)

print("................................................new_____links......................................................")

newlinks = list(set(newlinks))

print("................................................new____new______links......................................................")
del links[:]
for j in newlinks:
    get_page1(j)


'''

def get_link2(url):
    req = ".pdf"
    if req not in url and ".jpg" not in url and ".jpeg" not in url:
        flag = 1
        try:
            page = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            flag = 0
        if flag == 1:
            page = urllib.request.urlopen(url)
            html_doc = page.read()
            sock = urllib.request.urlopen(url) 
            htmlSource = sock.read()                            
            sock.close()   
            soup = BeautifulSoup(htmlSource)
            urllinks = []
            for link in soup.find_all('a'):
                #print(link)
                links = link.get('href')
                links = str(links)
                print(links)
                #if links.startswith('/') or fish_url2 in links:
                 #   print(links)
                urllinks.append(links)
            return urllinks


def get_moreLinks(url):
    print("inside more_links")
    print(url)
    req = ".pdf"
    if req not in url and ".jpg" not in url and ".jpeg" not in url:
        flag = 1
        try:
            page = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            flag = 0
        if flag == 1:
            page = urllib.request.urlopen(url)
            html_doc = page.read()
            sock = urllib.request.urlopen(url) 
            htmlSource = sock.read()                            
            sock.close()   
            soup = BeautifulSoup(htmlSource)
            urllinks = []
            urllinks.append(url)
            for link in soup.find_all('a'):
                #print(link)
                links = link.get('href')
                links = str(links)
                print(links)
                #if links.startswith('/') or fish_url2 in links:
                 #   print(links)
                urllinks.append(links)
            return urllinks





def get_page2(url):
    print(url)
    req = ".pdf"
    if req not in url and ".jpg" not in url and ".jpeg" not in url:
        flag = 1
        try:
            page = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            flag = 0
        if flag == 1:
            page = urllib.request.urlopen(url)
            html_doc = page.read()
            sock = urllib.request.urlopen(url) 
            htmlSource = sock.read()                            
            sock.close()                                        
            soup = BeautifulSoup(htmlSource)
            links = soup.find_all("p")
            #ind1 = url.rindex("/")
            #ind2 = url.rindex(".")
            #title = url[ind1+1:ind2]
            #print(title)
            title = soup.find("title")
            for link in links:
                db.Fortis_Hospital.insert({"data": link.text,"title": title.text})





links = get_link2(fish_url_com2)
newlinks = []
for i in links:
    #print(i)
    if fish_url2 not in i:
        i = fish_url_com2 + i
    newlinks.append(i)

newlinks = list(set(newlinks))
print("................................................links......................................................")

more_newlinks = []

del links[:]
for j in newlinks:
    print(j)
    more_links = get_moreLinks(j)
    if more_links is not None:
        for i in more_links:
            if fish_url2 not in i:
                i = fish_url_com2 + i
            more_newlinks.append(i)
    get_page2(j)

more_newlinks = list(set(more_newlinks))

print("earlier count")
print(db.Fortis_Hospital.count())
print("................................................new____new______links......................................................")

for j in more_newlinks:
    print(j)
    get_page2(j)

print("new count")
print(db.Fortis_Hospital.count())

'''

get count of records in mongodb before changing this operation and after changing this operation....................

for p in db.Fortis_Hospital.find():
    print(p);

for p in db.Apollo_Hospital.find():
    print(p);
'''
