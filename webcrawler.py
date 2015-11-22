# WEB CRAWLER

import urllib2

rank={}
bucketsize=24
crawled=[]
to_crawled=["http://www.rediff.com"]
keywords=[]
index={}
hashlist=[]
graph={}


def url_open(url):
   try:
       return urllib2.urlopen(url).read()
   except Exception:
       print "shan"
       return "false"

def crawl():
    i=0
  # while len(to_crawled)!=0:
    while i<1:
          url=to_crawled.pop()
          if url not in crawled and url[0:len(url)-1] not in crawled:
             print "crawl"+url
             crawled.append(url)
             content=url_open(url)
             i=i+1
             if content!="false":
                lis=findkeyword(content)
                print lis
                addkeyword(lis,url)
                add_hashkeyword(lis,url)
                adddictionary(lis,url)
                findurl(content,url)
    return "finished"

def findurl(content,link):
    if link not in graph:
       graph[link]=[]
    position=content.find('"http://')
    while position>0:
          endpos=content.find('"',position+1)
          url=content[position+1:endpos]
          graph[link].append(url)
          if url not in to_crawled:
             print "new"+url
             to_crawled.append(url)
          position=content.find('"http://',endpos)

def findkeyword(content):
    flag=0
    string=""
    string2=''
    lis=[]
    if "keyword" in content:
        string="keyword"
        string2='content'
        flag=1
    elif "Keyword" in content:
        string="Keyword"
        string2='Content'
        flag=1
    elif "KEYWORD" in content:
        string="KEYWORD"
        string2='CONTENT'
        flag=1
    if flag==1:
       print string
       pos=content.find(string)
       p=content.find(string2,pos)
       if p!=-1:
          begpos=content.find('"',p)
          endpos=content.find('"',begpos+1)
          lis=content[begpos+1:endpos].split(", ")
    return lis

def addkeyword(lis,url):
    flag=0
    for i in lis:
        flag=0
        for j in keywords:
            #print j[0]
            if j[0].lower()==i.lower():
              j[1].append(url)
              flag=1
              break
        if flag==0:
           l=[i.lower(),[url]]
           keywords.append(l)
       
def adddictionary(lis,url):
     for i in lis:
          if i.lower() in index:
           index[i.lower()].append(url)
          else :
           index[i.lower()]=[url]

def add_hashkeyword(lis,url):
    flag=0
    for i in lis:
        flag=0
        bucket=computebucket(i.lower())
        for j in hashlist[bucket]:
            if j[0].lower()==i.lower():
               j[1].append(url)
               flag=1
               break
        if flag==0:
           hashlist[bucket].append([i.lower(),[url]])

def computebucket(key):
     h=0    
     for i in key:
         h=(h+ord(i))%bucketsize
     return h

def buildbucket():
    for i in range(0,bucketsize):
        hashlist.append([])
               

def calc_rank():
    rank={}
    for node in graph:
        rank[node]=1/len(graph)
    for i in range(0,4):
      newrank={}
      for node in graph:
        newr=(1-0.8)/len(graph)
        for n in graph:
            if node in graph[n]:
               newr+=0.8*(rank[n]/len(graph[n]))
        newrank[node]=newr
      rank=newrank
    return rank
    

        
buildbucket()
print crawl()
print keywords
print index
print hashlist
print calc_rank()
#print rank


#a=["Rediffmail N"]
#addkeyword(a,"shan.com")
#print keywords
          



      




