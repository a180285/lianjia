import urllib2
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def getDetail(link):
    # print 'Try open : ' + link
    response = urllib2.urlopen(link)
    html = response.read()
    parsed_html = BeautifulSoup(html, 'lxml')
    price = parsed_html.body.find('div', attrs={'class':'price'})
    totalPrice = price.span.text
    unitPriceValue = price.find('span', attrs={'class':'unitPriceValue'}).text
    tax = price.find('div', attrs={'class':'tax'})
    firstPrice = tax.span.text
    panelDetail = tax.find('span', attrs={'class':'panelDetail'}).text
    print parsed_html.find('span', attrs={'class':'price_red'})
    print 'totalPrice : ', totalPrice
    print 'unitPriceValue : ', unitPriceValue
    print 'firstPrice : ', firstPrice
    print 'panelDetail : ', panelDetail


response = urllib2.urlopen('http://cq.lianjia.com/ershoufang/jiangbei/tf1de1y1sf1bp90ep170/')
html = response.read()

parsed_html = BeautifulSoup(html, 'lxml')
ans = parsed_html.body.find('ul', attrs={
    'class' : 'sellListContent',
    'log-mod' : 'list'})
for c in ans.children:
    title = c.find('div', attrs={'class' : 'title'})
    print title.text
    getDetail(title.a['href'])
