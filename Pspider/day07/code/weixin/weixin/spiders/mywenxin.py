# -*- coding: utf-8 -*-
import datetime
import scrapy
import re
import json


class MywenxinSpider(scrapy.Spider):
    name = 'myweixin'
    # allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    # def start_requests(self):



    def parse(self, response):

        # print(response.text)

        '''
        <div class="txt-box">
		<h3><a uigs="pc_0_42_title" href="http://mp.weixin.qq.com/s?src=11&timestamp=1534901402&ver=1075&signature=LQQLJbYuO09DSEOS2126phPZevkbdWozB9T2NFOPifc8jmTluApKJ5XakGTTBXdhC3GM57qm6hQT8hjnkSTAfwxD6o6stG0MWF0amcek6*MB9gJXd4qDGUToMYhG9zYn&new=1" target="_blank" data-share="http://weixin.sogou.com/api/share?timestamp=1534901402&signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAONG7kiCphK2Wv1Rdx9k2MwdarERAYf4AtUoiJRCg8QtR2uOL-wcB--WLyvxs8TqybYtW0gNzMh1PXHXQeLSFi6OldhCnvwJzqQRT3AQwZNaSnbxDy7qd*LzyHUTUPTVuSknY4b9EAUxpAdsjPVTK7jKDCKrw4T-lITqBkr-x0oKE=">27岁年轻人感冒后死亡，8个脏器5个衰竭，只因做了这件事!</a></h3>
		<p class="txt-info" target="_blank">一位27岁的年轻人感冒后，只因做了一件事，导致8个脏器系统5个衰竭，从入院到去世仅7天。两家三甲医院，数十名医护人员，动用了最先进的抢救措施和设备，但依然没能挽救他的生命。后来他的主治医生写下这篇文章...</p>
		<div class="s-p" t="1534747036">
	  		<a class="account" target="_blank" uigs="pc_0_42_account" i="oIWsFtyh6CJe5de-_2UkatXmmLL0" href="http://mp.weixin.qq.com/profile?src=3&timestamp=1534901402&ver=1&signature=334uomYYEbjRaYvtfI*87GBZmW-gDDOjakPjdvmDurVq7tyUn-fFrfoOKhP-k7T0ABqu*-ZQbFrE2wjCucEbYw==" data-headimage="//img02.sogoucdn.com/app/a/100520090/oIWsFtyh6CJe5de-_2UkatXmmLL0" data-isV="1">扬子晚报</a>
	  		<span class="s2" t="1534747036"></span>
	  		<div class="moe-box">
				<span class="sc" style="display:none;"><a href="javascript:void(0);" class="sc-a" uigs="pc_0_42_share" data-except="1"></a></span>
	  		</div>
		</div>
  	</div></li>	<li d="ab735a258a90e8e1-6bee54fcbd896b2a-0078b32087d851a8b7aa918a13020fcc">	<div class="img-box">
		<a uigs="pc_0_43_img" href="http://mp.weixin.qq.com/s?src=11&timestamp=1534901402&ver=1075&signature=SxelhgtEFkFlZM5iMBDtjDKj9okTKWvDVmPKQH0nkPnuUtqRH0Vcjk5PwhAhL0gRkalVcBvjlluplWFHk6J-1E0Dx4yx1Z6UlTqa5pJXl*pSgHcYECTIJ-BqmFGIXVpS&new=1" target="_blank">

			<img src="//img03.sogoucdn.com/net/a/04/link?appid=100520033&url=http%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F8xAXKWQGCIgKSd4RGYoEbanibTYxOB2F50sYmzr8vs5G60ZnJUUt84ian0e4aOdoSmPu7ocKtK9EmcZ14yx4XCiaw%2F0%3Fwx_fmt%3Djpeg" onload="resizeImage(this)" onerror="errorImage(this)"/>
		</a>
	</div>
        '''
        publicNumList = response.xpath('//div[@class="txt-box"]')
        for wx in publicNumList:
            # 微信公众号url
            wechatPublicNumurl = wx.xpath('.//div[@class="s-p"]/a/@href').extract()[0]

            # 构建请求
            yield scrapy.Request(url=wechatPublicNumurl, callback=self.get_weichatPublic)

            # print(wechatPublicNum,wechatPublicNumurl)

        # 翻页
        for i in range(1, 20):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            }
            url = "http://weixin.sogou.com/pcindex/pc/pc_0/{}.html".format(i)
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def get_weichatPublic(self, response):
        '''
        获取公众号
        :param response:
        :return:
        '''

        html = response.text
        # print(html)
        # 公众号
        wechatPublicNum = response.xpath('//p[@class="profile_account"]/text()').extract()[0]

        # # 昵称
        wechatPublicNickname = response.xpath('//strong[@class="profile_nickname"]/text()').extract()[0].strip()

        # # 二维码
        QRcode = "http://mp.weixin.qq.com" + response.xpath('//img[@id="js_pc_qr_code_img"]/@src').extract()[0].strip()

        # # 文章正则
        articleRe = "msgList = (.*)?;"

        articleJson = re.findall(articleRe, html)[0]
        # print(articleJson, '==============')

        data = json.loads(articleJson)

        for articleList in data['list']:
            article_msg_item_list = articleList['app_msg_ext_info']['multi_app_msg_item_list']
            # 文章标题1
            title1 = articleList['app_msg_ext_info']['title']
            # 文章1时间
            time1 = articleList['comm_msg_info']['datetime']

            time1 = datetime.datetime.fromtimestamp(time1)
            print(title1, time1)

            if article_msg_item_list:
                for article_msg in article_msg_item_list:
                    # 文章标题2
                    title2 = article_msg['title']
                    print(title2, time1)

                    print(wechatPublicNickname, wechatPublicNum, QRcode)
