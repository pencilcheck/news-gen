import news
import scraper
import random
import unicodedata

def gen_latex(name, cols, art_list):
    news.setName(name)
    news.setColumns(cols)
    random.seed()
    
    for (title, url) in art_list:
        news.addArticle(news.convert(scraper.scrape(url)), title)

    news.Generate()
    text = news.Latex
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

    f_stub = 'newspaper-'+str(random.randrange(0, 2000))
    f_name = 'static/'+f_stub+'.tex'
    f = open(f_name, 'w')
    f.write(text)
    f.close()

    return (f_stub, f_name)

        
