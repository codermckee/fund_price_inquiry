# -*- coding: utf-8 -*-
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
    print '净值估计:',predict_date[0].text,predict_price[0].text
    for i in soup1.select('#Li1 tr'):
        print i.text.strip()
    print '\n'

if __name__ == '__main__':
    try:
        print '长 信 量 化 先 锋--519983(持仓)￥￥1.5830'
        inquire_fund(url_fund('519983'))
        print '富 国 中 证 军 工--161024(持仓)￥￥0.92'
        inquire_fund(url_fund('161024'))
        print '融 通 深 证 100--161604(持仓)￥￥1.813//￥￥1.2030'
        inquire_fund(url_fund('161604'))
        print '融 通 新 蓝 筹--161601(持仓)￥￥0.68'
        inquire_fund(url_fund('161601'))
        print '南 方 策 略 优 化 混 合--202019'
        inquire_fund(url_fund('202019'))
        print '兴 全 有 机 增 长--340008'
        inquire_fund(url_fund('340008'))
        print '富 国 天 瑞--100022(持仓)￥￥0.9-1.0'
        inquire_fund(url_fund('100022'))
        print '中 银 增 长--163803(持仓)￥￥0.533'
        inquire_fund(url_fund('163803'))
        print '南 方 成 分 精 选--202005(持仓)￥￥0.8-1.4'
        inquire_fund(url_fund('202005'))
        print '招 商 先 锋--217005(持仓)￥￥1.0145'
        inquire_fund(url_fund('217005'))
        print '上 投 摩 根--377016(持仓)￥￥0.81456'
        inquire_fund(url_fund('377016'))
        print '白 酒--161725'
        inquire_fund(url_fund('161725'))
        print '原 油--501018'
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
