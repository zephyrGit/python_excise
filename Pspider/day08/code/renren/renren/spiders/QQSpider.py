# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/23 9:17
@Author  : Fate
@File    : QQSpider.py
'''

import scrapy


class MyrenrenSpider(scrapy.Spider):
    name = 'myQQ'
    allowed_domains = ['user.qzone.qq.com']
    start_urls = ['http://user.qzone.qq.com/1687458949']

    cookie = {'RK': 'rmHT7e2LQD', 'pgv_pvi': '9920637952', 'pac_uid': '1_1687458949',
              'eas_sid': 'H1z5Y0H4U3M3f8E004v1F3X6I7', 'LW_uid': 'Y1W590G4O333K87114z6Z4L5J4',
              'pgv_pvid_new': '1687458949_103e8ac4183', 'tvfe_boss_uuid': '5eed6635b6c9405a',
              'mobileUV': '1_15ecd77b5fe_99bfa', 'o_cookie': '1687458949', 'QZ_FE_WEBP_SUPPORT': '1',
              'pgv_pvid': '2040220332', 'ptcz': '1fd2762d2f45e34542eb5fcd75ac829861fc1c6ac443d23fccfd1ce0edd2fc9a',
              '__Q_w_s__QZN_TodoMsgCnt': '1', 'ptui_loginuin': '1687458949', 'pt2gguin': 'o1687458949',
              'LW_sid': 'B1b5G3E3O931C7e8h9X6l7Z0q4', 'luin': 'o1687458949',
              'lskey': '0001000089894b46be89448efe29901858b8f0dc97ddb536699ad2bb0b528d8c0980b2fbd3228a5894bcd854',
              '_qpsvr_localtk': '0.9360270193842759', 'pgv_si': 's4745961472', 'ptisp': 'ctc',
              'pgv_info': 'ssid=s2811748556', 'uin': 'o1687458949', 'skey': '@s6Fnk2wO4', 'p_uin': 'o1687458949',
              'Loading': 'Yes', 'qz_screen': '1366x768', '1687458949_todaycount': '0', '1687458949_totalcount': '0',
              'cpu_performance_v8': '59', 'pt4_token': 'HHnu8SWWN-cYqkZPJkAbqpsPaJ1Qj*3HPVpB5FzJ19U_',
              'p_skey': 'io2JKmEvT9mttLS2ayZAoZAax9N2zSPonIB*m8fPt64_',
              'x-stgw-ssl-info': 'c2a39c2c272775873d1cb51c2782c877|0.102|1534987292.958|36|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|22000|h2|0'}

    # def start_requests(self):
    #     url = "http://user.qzone.qq.com/1687458949"
    #     yield scrapy.FormRequest(url, cookies=self.cookie, callback=self.parse)

    def parse(self, response):
        print(response.text)
