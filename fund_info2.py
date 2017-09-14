# -*- coding: cp936 -*-
import requests
from bs4 import BeautifulSoup
def url_fund(code):
    return 'http://fund.eastmoney.com/' + code + '.html?spm=search'
def inquire_fund(fund_url):
    res = requests.get(fund_url)
    res.encoding = 'utf-8'
    soup1 = BeautifulSoup(res.text)
    predict_date = soup1.select('#gz_gztime')
    predict_price = soup1.select('#gz_gsz')
    print '��ֵ����:',predict_date[0].text,predict_price[0].text
    for i in soup1.select('#Li1 tr'):
        print i.text.strip()
    print '\n'
   
try:
    print '�� �� �� �� �� ��--519983(�ֲ�)����1.5830'
    inquire_fund(url_fund('519983'))
    print '�� �� �� ֤ �� ��--161024(�ֲ�)����0.92'
    inquire_fund(url_fund('161024'))
    print '�� ͨ �� ֤ 100--161604(�ֲ�)����1.813//����1.2030'
    inquire_fund(url_fund('161604'))
    print '�� ͨ �� �� ��--161601(�ֲ�)����0.68'
    inquire_fund(url_fund('161601'))    
    print '�� �� �� �� �� �� �� ��--202019'
    inquire_fund(url_fund('202019'))
    print '�� ȫ �� �� �� ��--340008'
    inquire_fund(url_fund('340008'))
    print '�� �� �� ��--100022(�ֲ�)����0.9-1.0'
    inquire_fund(url_fund('100022'))
    print '�� �� �� ��--163803(�ֲ�)����0.533'
    inquire_fund(url_fund('163803'))
    print '�� �� �� �� �� ѡ--202005(�ֲ�)����0.8-1.4'
    inquire_fund(url_fund('202005'))
    print '�� �� �� ��--217005(�ֲ�)����1.0145'
    inquire_fund(url_fund('217005'))
    print '�� Ͷ Ħ ��--377016(�ֲ�)����0.81456'
    inquire_fund(url_fund('377016'))
    print '�� ��--161725'
    inquire_fund(url_fund('161725'))
    print 'ԭ ��--501018'
    inquire_fund(url_fund('501018'))
except:
    print '''     -----------------
    ���粻�ȶ�����������һ��!
    -----------------------'''

cunjinbao_url = requests.get('https://cjb.alipay.com/gold/guide.htm;jsessionid=B68B29987841CF87D2A56E1A94EA30B7')
soup_cunjinbao = BeautifulSoup(cunjinbao_url.text)
gold_price = soup_cunjinbao.select('.ft-56')
date = soup_cunjinbao.select('.date') 
print date[0].text,gold_price[0].text.strip()
