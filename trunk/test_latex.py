import news
import re
import simplejson as json
import scraper
import YQL
import HTMLParser
import unicodedata

def main():
    news.setName("The New Illini")
    news.setColumns(4)
    t = YQL.searchNews('china')
    
    ob_j = json.loads(re.sub(r'"result":({[^}]+})', r'"result":[\1]', t))
    #ob_j = json.loads(t)
    for i in xrange(len(ob_j['query']['results']['result'])):
        print ob_j['query']['results']['result'][i]['url']
        news.addArticle(news.convert(scraper.scrape(ob_j['query']['results']['result'][i]['url'])), ob_j['query']['results']['result'][i]['title'])
        
    news.Generate()
    text = news.Latex
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
        
    f = open('latex_one_test.tex', 'w')
    f.write(text)
    f.close()

        

if __name__ == "__main__":
    main()
