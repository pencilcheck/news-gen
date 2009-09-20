'''
Created on Sep 17, 2009
This is a YQL query library that returns stuff in JSON
@author: Abhishek
'''
import urllib2
queryurl="http://query.yahooapis.com/v1/public/yql?q="
format="&format=json"
age=""
region=""


def query(input):
    print queryurl+replaceSpaces(input)+format
    filehandle = urllib2.urlopen(queryurl+replaceSpaces(input)+format)
    return filehandle.read()
    
def replaceSpaces(query):
    return query.replace(' ','%20')

def searchNews(newsquery):
    newsquery = "select title,abstract,url from search.news where query=\""+newsquery+ " " + region + "\" " + age
    return query(newsquery)

def setAge(nage):
    global age
    age = " AND age=" + str(nage) +"d"
    
def unsetAge():
    global age
    age = ""
    
def setRegion(regional):
    global region
    region = regional
    
def unsetRegion():
    global region
    region = ""
    
def reset():
    global age, region
    age = ""
    region = ""
