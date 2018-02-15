# -*- coding: utf-8 -*-
import requests
import matplotlib.pyplot as plt
import pylab as pl
import time,datetime
from bs4 import BeautifulSoup
def url_fund(code):
    return 'http://fund.eastmoney.com/' + code + '.html?spm=search'
def inquire_fund(fund_url):
    res = requests.get(fund_url)
    res.encoding = 'utf-8'
    soup1 = BeautifulSoup(res.text)
    predict_date = soup1.select('#gz_gztime')
    predict_price = soup1.select('#gz_gsz')
    print '净值估计:',predict_date[0].text,predict_price[0].text
    plot_data = []
    for i in soup1.select('#Li1 tr'):
        print i.text.strip()
        plot_data.append(i.text.strip())
    print '\n'


def plot(fund_url):
    res = requests.get(url_fund(fund_url))
    res.encoding = 'utf-8'
    soup1 = BeautifulSoup(res.text)
    predict_date = soup1.select('#gz_gztime')
    predict_price = soup1.select('#gz_gsz')
    #print '净值估计:',predict_date[0].text,predict_price[0].text
    plot_data = []
    date = []
    price = []
    for i in soup1.select('#Li1 tr'):
        info = i.text.strip()
        date.append(info[0:5])
        price.append(info[6:12])
        #plot_data.append(i.text.strip())
    del date[0]
    del price[0]
    for i in range(len(price)):
        price[i] = float(price[i])
    for i in range(len(date)):
        t = datetime.datetime.strptime(date[i],'%m-%d')
        year = t.year + 118
        mon = t.month
        day = t.day
        d = datetime.date(year,mon,day)
        date[i] = d
    date.reverse()
    x = date
    price.reverse()
    y = price
    plt.plot(x,y,'ob-')
    plt.gcf().autofmt_xdate()#旋转日期
    plt.title('Price Evaluation:'+str(predict_date[0].text)+' '+str(predict_price[0].text))
    plt.show()
    """
if __name__ == '__main__':
    plot('161725')
"""
if __name__ == '__main__':
    try:
        print 'mckee头条：'
        print "2017-12-31 跨年 基金走高！"
        print '2018-1-16 大盘11连阳结束！'
        print '2018-2-6 年前一周 所有基金跳水，如白酒！'
        print '年前建议：千万别买。尽量清仓！！！'
        print '中银增长曾从0.7涨到1.7，即10万份10万元'
        print '富国天瑞，中银，南方成分精选'
        print '2-5 决策失误，煤炭买高了，买了即暴跌'
        print '----------------------'
        print '富 安 达--000755(持仓)￥￥1.0807'
        inquire_fund(url_fund('000755'))
        print '计 算 机 C--001630'
        inquire_fund(url_fund('001630'))
        print '证 券--161720'
        inquire_fund(url_fund('161720'))
        print '保 险c -- 001553(持仓)--￥￥0.7679(2k+2.5k)'
        inquire_fund(url_fund('001553'))
        print '长 信 量 化 先 锋--519983(持仓)￥￥1.5830--(1.51加仓&1.57考虑加仓)//￥￥1.4730(1W)'
        inquire_fund(url_fund('519983'))
        print '富 国 中 证 军 工--161024(持仓)￥￥0.92--(低迷)--￥￥0.705(2.8k)'
        inquire_fund(url_fund('161024'))
        print '融 通 深 证 100--161604(持仓)￥￥1.403//￥￥1.2030//￥￥1.22(6.8K)'
        inquire_fund(url_fund('161604'))
        print '融 通 新 蓝 筹--161601(持仓)￥￥0.733---(0.89加仓)'
        inquire_fund(url_fund('161601'))
        print '南 方 策 略 优 化 混 合--202019'
        inquire_fund(url_fund('202019'))
        print '富 国 天 瑞--100022(持仓)￥￥0.219--（0.73卖）'
        inquire_fund(url_fund('100022'))
        print '中 银 增 长--163803(持仓)￥￥0.229--（0.47卖）'
        inquire_fund(url_fund('163803'))
        print '南 方 成 分 精 选--202005(持仓)[￥￥0.8-1.4-(1.17分红0.2563)]-->￥￥0.5437-1.1437--（1.05卖）'
        inquire_fund(url_fund('202005'))
        print '招 商 先 锋--217005(持仓)￥￥1.0145'
        inquire_fund(url_fund('217005'))
        print '煤 炭--161724--￥￥1.1940(1.8k)--￥￥1.0920(3k)'
        inquire_fund(url_fund('161724'))
        print '白 酒--161725--(1.11加仓)'
        inquire_fund(url_fund('161725'))
        print '原 油--501018--(1.01加仓)'
        inquire_fund(url_fund('501018'))
    except:
        print '''     -----------------
        网络不稳定，请重新试一次!
        -----------------------'''
    cunjinbao_url = requests.get('https://cjb.alipay.com/gold/guide.htm;jsessionid=B68B29987841CF87D2A56E1A94EA30B7')
    soup_cunjinbao = BeautifulSoup(cunjinbao_url.text)
    gold_price = soup_cunjinbao.select('.ft-56')
    date = soup_cunjinbao.select('.date')
    print date[0].text,gold_price[0].text.strip()
    a = True
    while a:
        code = raw_input('想看哪只基金走势图：code / no ?\n command:')
        if code == 'no':
            a = False
        else:
            plot(code)
#"""
