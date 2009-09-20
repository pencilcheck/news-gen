'''
Created on Aug 30, 2009

@author: Penn
'''

from string import Template
import re

Name = 'Yahoo HackU News:'
Slogan = ''
Header = 'Yahoo HackU News'
Location = 'Illinois'
Volume = 1
Issue = 1
Orientation = 'Portrait'
Size = 12
Family = 'times'
Columns = 2
Articles = dict()
Dates = dict()
Images = dict()

Latex = ''

def convert(n):
    n = re.sub(r'"(.*?)"', r"``\1''", n)
    return n.replace('\\', '').replace('%', '%%').replace('#', '\\#').replace('$', '\\$').replace('&', '\\&').replace('~', '\\~{}').replace('_', '\\_').replace('^', '\\verb+^+').replace('{', '\\{').replace('}', '\\}')
    
def revert(n):
    return n.replace()

def setName(n):
    global Name
    Name = n

def setSlogan(n):
    global Slogan
    Slogan = n

def setHeader(n):
    global Header
    Header = n

def setLocation(n):
    global Location
    Location = n

def setVolume(n):
    global Volume
    Volume = n

def setIssue(n):
    global Issue
    Issue = n

def setOrientation(n):
    global Orientation
    Orientation = n

def setFontSize(n):
    global Size
    Size = n

def setFontFamily(n):
    global Family
    Family = n

def setColumns(n):
    global Columns
    Columns = n
    
def addArticle(n, t=''):
    global Articles
    if t == '':
        test = 0
        while Articles.has_key(test):
            test += 1
        Articles[str(test)] = n
    else:
        Articles[t] = n

def removeArticle(n):
    if n in Articles.values():
        for k in Articles.keys():
            if Articles[k] == n:
                del Articles[k]

def ArticlesCount():
    return len(Articles)

def ArticleExist(n):
    return n in Articles.values()

def addArticleTitle(n, t):
    removeArticle(n)
    addArticle(n, t)

def getArticleTitle(n):
    if n in Articles.values():
        for k in Articles.keys():
            if Articles[k] == n:
                return k
        
def getArticle(t):
    return Articles[t]

# input k, the title of the article, use getArticleTitle(n) where n is the article content
# input d, the date to put in, please unify the format
def addDatetoArticle(k, d):
    global Dates
    Dates[k] = d

def DateExistforArticle(t):
    return t in Dates

def removeDate(t):
    if DateExistforArticle(t):
        del Dates[t]

def DatesCount():
    return len(Dates)

def addImagetoArticle(n, url, caption=''):
    global Images
    if ArticleExist(n):
        Images[n] = (url, caption)

def addCaptiontoImage(n, caption):
    if ImageExist(n):
        Images[n] = (Images[n][0], caption)

def ImageExist(n):
    return n in Images.keys()

def ImageCount():
    return len(Images)

def removeImagefromArticle(n):
    if ImageExist(n):
        del Images[n]

def getImageUrl(n):
    if ImageExist(n):
        return Images[n][0]
    else:
        return ''

def getImageCaption(n):
    if ImageExist(n):
        return Images[n][1]
    else:
        return ''

def addArticles():
    global Latex
    for n in Articles.values():
        Latex += '{\n'
        try:
            title = int(getArticleTitle(n))
            if(title >= 0):
                title = ''
        except:
            title = getArticleTitle(n)
        if title != '':
            Latex += '\headline{\sc\Large %s}\n'%(title)
        if ImageExist(n):
            Latex += '\\begin{window}[4,l,\includegraphics[width=1.65in]{%s},\\footnotesize{\it %s}]\n'%(getImageUrl(n), getImageCaption(n))
        Latex += n + '\n'
        if ImageExist(n):
            Latex += '\end{window}\n'
        Latex += '\closearticle}\n\n'

def Generate():
    global Latex
    if ArticlesCount() != 0:
        if(Orientation == 'Portrait'):
            Latex += '\documentclass[8pt]{article}\n'
            Latex += '\usepackage{yfonts}\n\usepackage{newspaper}\n\usepackage{utopia}\n\usepackage{graphicx}\n\usepackage{multicol}\n\usepackage{extsizes}\n\usepackage{picinpar}\n'
            Latex += '\pagestyle{empty}\n\hoffset=0pt\n\\voffset=-50pt\n\oddsidemargin=-50pt\n\headsep=10pt\n\marginparsep=0pt\n\marginparwidth=0pt\n\\footskip=0pt\n\\textwidth=570pt\n\\textheight=700pt\n'
        elif(Orientation == 'Landscape'):
            Latex += '\documentclass[8pt,landscape]{article}\n'
            Latex += '\usepackage{yfonts}\n\usepackage{newspaper}\n\usepackage{utopia}\n\usepackage{graphicx}\n\usepackage{multicol}\n\usepackage{extsizes}\n\usepackage{picinpar}\n'
            Latex += '\pagestyle{empty}\n\hoffset=0pt\n\\voffset=-50pt\n\oddsidemargin=-50pt\n\headsep=10pt\n\marginparsep=0pt\n\marginparwidth=0pt\n\\footskip=0pt\n\\textwidth=750pt\n\\textheight=520pt\n'
        s = Template('\date{\\today}\n\currentvolume{$Volume}\n\currentissue{$Issue}\n\SetPaperName{$Name}\n\SetHeaderName{$Header}\n\SetPaperLocation{$Location}\n\SetPaperSlogan{$Slogan}\n')
        Latex += s.substitute(Volume=Volume, Issue=Issue, Name=Name, Header=Header, Location=Location, Slogan=Slogan)
        # begin document
        Latex += '\\begin{document}\n\maketitle\n'
        if(Columns > 1):
            Latex += '\\begin{multicols}{%s}\n'%(Columns)
            addArticles()
            Latex += '\end{multicols}\n\end{document}'
        else:
            addArticles()
            Latex += '\end{document}'
