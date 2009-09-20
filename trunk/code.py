import web
import simplejson as sjson
import news_wrapper
import YQL
import re
import os
import shutil
import glob

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/gen_news', 'gen_news',
    '/form_test', 'form_test',
    '/newspdf.json', 'newspdf',
    '/test', 'test'
    )

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index()

class test:
    def GET(self):
        return render.test()

class form_test:
    def POST(self):
        i = web.input(json=None)
        if i.json:
            return i.json
        else:
            return "Ahh, I know nothing!"

class gen_news:
    def POST(self):
        i = web.input(json=None)
        if i.json:
            j = sjson.loads(i.json)
            topics = j['topics'].split(',')
            num_articles = int(j['numarts']) / len(topics)
            news_t = []
            for topic in topics:
                s = YQL.searchNews(topic)
                ob_j = sjson.loads(re.sub(r'"result":({[^}]+})', r'"result":[\1]', s))
                for i in xrange(num_articles):
                    news_t.append((ob_j['query']['results']['result'][i]['title'], ob_j['query']['results']['result'][i]['url']))
            (f_stub, f_name) = news_wrapper.gen_latex(j['title'], int(j['numcols']), news_t)
            os.system('pdflatex '+f_name)
            shutil.copyfile(f_stub+'.pdf', 'static/'+f_stub+'.pdf')
            os.system('convert -density 250 '+'static/'+f_stub+'.pdf static/'+f_stub+'.png')
            #return 'convert '+'static\\'+f_stub+'.pdf static\\news'+'.png'
            k = glob.glob('static/'+f_stub+'*.png')
            u = []
            for i in k:
                u.append(re.sub("\\\\", '/', i))
            u = ['static/'+f_stub+'.pdf'] + u
            return sjson.dumps(u)
            #return sjson.dumps(['static/'+f_stub+'.pdf', "static/"+f_stub+"-0.png", "static/"+f_stub+"-1.png"])
            #return [].append

class newspdf:
    def GET(self):
        print '{"page": "/static/pdf_xyz123-1.png"}, {"page": "/static/pdf_xyz123-2.png"}'

if __name__ == "__main__":
    app.run()
