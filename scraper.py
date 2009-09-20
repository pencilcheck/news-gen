import urllib2
import re
import unicodedata
from BeautifulSoup import BeautifulSoup

from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def build_parent_score(para_list):
    l = []
    for para in para_list:
        if not [para.parent, 0] in l:
            l.append([para.parent, 0])
    return l

def num_commas(st):
    return st.count(',')

def get_parent(parent_list, child):
    for t in parent_list:
        if t[0] == child.parent:
            return t

def scrape(url):
    nline_reg = re.compile('\n{3,}.*', re.DOTALL)
    br_reg = re.compile('<br/?>|<br /?>')
    
    st = urllib2.urlopen(urllib2.Request(url)).read()
    st = br_reg.sub('<p>', st)
    st_l = st.splitlines()
    st = '\n'.join(st_l)
    souped = False
    while souped == False:
        try:
            soup = BeautifulSoup(st)
        except HTMLParseError as err:
            st_l = st.splitlines()
            st_l.remove(st_l[err.lineno-1])
            st = '\n'.join(st_l)
        else:
            souped = True

    divs = soup.findAll('div')
    for i in divs:
        try:
            if i['class'] == "cnnWsnr":
                i.extract()
        except:
            pass

        try:
            if i['class'] == "toolbar clearfix":
                i.extract()
        except:
            pass

        try:
            if i['align'] == "right":
                i.extract()
        except:
            pass

            
        
        try:
            if i['id'] == "email":
                i.extract()
        except:
            pass

    for i in soup.findAll('iframe'):
        i.extract()
    for i in soup.findAll('script'):
        i.extract()
    for i in soup.findAll('style'):
        i.extract()
        
    paras = soup.findAll('p')
    parent_list = build_parent_score(paras)

    for p_l in parent_list:
        try:
            p_l[0] = parent
            par_id = parent['id']
            num = 0
            num += par_id.count('comment')
            num += par_id.count('meta')
            num += par_id.count('footer')
            num += par_id.count('footnote')
            if num > 0:
                p_l[1] -= 50
            num = 0
            num += par_id.count('post')
            num += par_id.count('entry')
            num += par_id.count('hentry')
            num += par_id.count('content')
            num += par_id.count('text')
            num += par_id.count('body')
            num += par_id.count('article')
            if num > 0:
                p_l[1] += 25
        except:
            pass

        try:
            par_class = parent['class']
            num = 0
            num += par_class.count('comment')
            num += par_class.count('meta')
            num += par_class.count('footer')
            num += par_class.count('footnote')
            if num > 0:
                p_l[1] -= 50
            num = 0
            num += par_class.count('post')
            num += par_class.count('entry')
            num += par_class.count('hentry')
            num += par_class.count('content')
            num += par_class.count('text')
            num += par_class.count('body')
            num += par_class.count('article')
            if num > 0:
                p_l[1] += 25
        except:
            pass

    for para in paras:
        p_l = get_parent(parent_list, para)
        para = p_l[0]
        if len(str(para)) > 10:
            p_l[1] += 1
        p_l[1] += str(para).count(',')

    m_score = 0
    curr_index = 0
    for index in xrange(len(parent_list)):
        #print parent_list[index][1]
        if parent_list[index][1] > m_score:
            m_score = parent_list[index][1]
            curr_index = index
    #print m_score

    high_parent = parent_list[curr_index][0]
    
    soup1 = BeautifulSoup(str(high_parent))

    ret_st = ''

    for i in soup1.findAll('p'):
        ret_st += strip_tags(str(i))

    #ret_st = nline_reg.sub('', ret_st)
    #return soup1.findAll('p')
    ret_st = ret_st.replace('\xe2\x80\x99', '\'')
    ret_st = re.sub(r'\.([a-zA-Z])', r"\. \1", ret_st)
    ret_st = ret_st.replace('\xe2\x80\x99', '\'')
    ret_st = re.sub(r"E-mail to a friend.*", r'', ret_st)
    return ret_st.decode('utf-8')

    #return str(high_parent)
