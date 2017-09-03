# -*- coding: cp936 -*-
import requests
from bs4 import BeautifulSoup
def url_fund(code):
    return 'http://fund.eastmoney.com/' + code + '.html?spm=search'
def inquire_fund(fund_url):
    res = requests.get(fund_url)
    res.encoding = 'utf-8'
    soup1 = BeautifulSoup(res.text)
    for i in soup1.select('#Li1 tr'):
        print i.text
    print '\n'
   

print '�� ͨ �� �� ��--161601(�ֲ�)����0.68'
inquire_fund(url_fund('161601'))    
print '�� �� �� �� �� �� �� ��--202019'
inquire_fund(url_fund('202019'))
print '�� ȫ �� �� �� ��--340008'
inquire_fund(url_fund('340008'))
print '�� �� �� �� �� ��--519983(�ֲ�)����'
inquire_fund(url_fund('519983'))
print '�� �� �� ֤ �� ��--161024(�ֲ�)����'
inquire_fund(url_fund('161024'))
print '�� �� �� ��--100022(�ֲ�)����1.0'
inquire_fund(url_fund('100022'))
print '�� ͨ �� ֤ 100--161604(�ֲ�)����1.813'
inquire_fund(url_fund('161604'))
print '�� �� �� ��--163803(�ֲ�)����1.066'
inquire_fund(url_fund('163803'))
print '�� �� �� �� �� ѡ--202005(�ֲ�)����0.8-1.4'
inquire_fund(url_fund('202005'))
print '�� �� �� ��--217005(�ֲ�)����1.0145'
inquire_fund(url_fund('217005'))
print '�� Ͷ Ħ ��--377016(�ֲ�)����0.81456'
inquire_fund(url_fund('377016'))

cunjinbao_url = requests.get('https://cjb.alipay.com/gold/guide.htm;jsessionid=B68B29987841CF87D2A56E1A94EA30B7')
soup_cunjinbao = BeautifulSoup(cunjinbao_url.text)
gold_price = soup_cunjinbao.select('.ft-56')
print '��𱦽��ս��',gold_price[0].text.strip()
