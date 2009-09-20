import news
import scraper
import random
import unicodedata
import YQL
import simplejson as json
import re

def gen_latex(name, cols, art_list):
    news.setName(name)
    news.setColumns(cols)
    
    for (title, url) in art_list:
        news.addArticle(news.convert(scraper.scrape(url)), title)

    news.Generate()
    text = news.Latex
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

    f_name = 'static/newspaper-'+str(random.randrange(0, 2000))+'.tex'
    f = open(f_name, 'w')
    f.write(text)
    f.close()

    return f_name

        
def main():
    t = YQL.searchNews('obama')
    ob_j = json.loads(re.sub(r'"result":({[^}]+})', r'"result":[\1]', t))
    news_t = []
    for i in xrange(len(ob_j['query']['results']['result'])):
        news_t.append((ob_j['query']['results']['result'][i]['title'], ob_j['query']['results']['result'][i]['url']))
    name = gen_latex('stuff', 4, news_t)
    print name

if __name__ == "__main__":
    main()
