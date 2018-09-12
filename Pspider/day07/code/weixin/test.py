# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 10:18
@Author  : Fate
@File    : test.py
'''
html = '''
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="format-detection" content="telephone=no">


        <script nonce="" type="text/javascript">
            window.logs = {
                pagetime: {}
            };
            window.logs.pagetime['html_begin'] = (+new Date());
        </script>
        <title>华商报 </title>

<link rel="stylesheet" href="https://res.wx.qq.com/open/libs/weui/0.2.0/weui.css">
<link rel="stylesheet" href="//res.wx.qq.com/mmbizwap/en_US/htmledition/style/page/profile/sougou_profile3de35e.css">
<!--[if lt IE 9]>
<link rel="stylesheet" type="text/css" href="//res.wx.qq.com/mmbizwap/en_US/htmledition/style/page/profile/sougou_profile_pc3de35e.css">
<![endif]-->

    </head>
    <body id="" class="en_US    ">

        <link rel="dns-prefetch" href="//res.wx.qq.com">
<link rel="dns-prefetch" href="//mmbiz.qpic.cn">
<link rel="shortcut icon" type="image/x-icon" href="//res.wx.qq.com/mmbizwap/en_US/htmledition/images/icon/common/favicon22c41c.ico">
<script nonce="" type="text/javascript">
    String.prototype.html = function(encode) {
        var replace =["&#39;", "'", "&quot;", '"', "&nbsp;", " ", "&gt;", ">", "&lt;", "<", "&amp;", "&", "&yen;", "¥"];
        if (encode) {
            replace.reverse();
        }
        for (var i=0,str=this;i< replace.length;i+= 2) {
             str=str.replace(new RegExp(replace[i],'g'),replace[i+1]);
        }
        return str;
    };

    window.isInWeixinApp = function() {
        return /MicroMessenger/.test(navigator.userAgent);
    };

    window.getQueryFromURL = function(url) {
        url = url || 'http://qq.com/s?a=b#rd';
        var tmp = url.split('?'),
            query = (tmp[1] || "").split('#')[0].split('&'),
            params = {};
        for (var i=0; i<query.length; i++) {
            var arg = query[i].split('=');
            params[arg[0]] = arg[1];
        }
        if (params['pass_ticket']) {
        	params['pass_ticket'] = encodeURIComponent(params['pass_ticket'].html(false).html(false).replace(/\s/g,"+"));
        }
        return params;
    };

    (function() {
	    var params = getQueryFromURL(location.href);
        window.uin = params['uin'] || "" || '';
        window.key = params['key'] || "" || '';
        window.wxtoken = params['wxtoken'] || '';
        window.pass_ticket = params['pass_ticket'] || '';
        window.appmsg_token = "";
    })();

    function wx_loaderror() {
        if (location.pathname === '/bizmall/reward') {
            new Image().src = '/mp/jsreport?key=96&content=reward_res_load_err&r=' + Math.random();
        }
    }

</script>

<script nonce="" type="text/javascript">
            window.no_moon_ls = 0;
    </script>

<div class="page_profile_info">
    <div class="page_profile_info_inner">
        <div class="profile_info_area">
            <div class="profile_info_group">
                <span class="radius_avatar profile_avatar">
                                        <img src="http://wx.qlogo.cn/mmhead/6a2Gd4BZHuWXO5rY1kbZCk0sicOicK7s09C0j2A9Gk2ic0/0">
                                    </span>
                <div class="profile_info">
                    <strong class="profile_nickname">
                      华商报
                    </strong>
                                        <p class="profile_account">微信号: hsb88880000</p>
                                    </div>
            </div>
            <ul class="profile_desc">
                <li>
                    <label class="profile_desc_label" for="">功能介绍</label>
                    <div class="profile_desc_value" title="奉献最有价值的新闻和信息">奉献最有价值的新闻和信息</div>
                </li>
                <li>
                    <label class="profile_desc_label" for="">帐号主体</label>
                    <div class="profile_desc_value"><img class="icon_verify success" src="//res.wx.qq.com/mmbizwap/en_US/htmledition/images/icon/common/icon_verify_success.2x2a26be.png">《华商报》社</div>
                </li>
            </ul>

            <div class="profile_opr"  style="display:none">
                            <a href="javascript:void(0);" id="copyBt" class="weui_btn weui_btn_plain_primary">复制微信号</a>
                        </div>

        </div>
        <div class="weui_category_title">最近10条群发</div>
        <div class="weui_msg_card_list" id="history">

        </div>
        <div class="msg_card_tips">仅显示最近10条群发</div>

        <div class="loadmore" style="display:none;" id="js_loading">
            <div class="tips_wrp"><i class="icon_loading"></i><span class="tips">正在加载</span></div>
        </div>
        <div class="loadmore with_line" style="display:none;" id="js_nomore">
            <div class="tips_wrp"><span class="tips">已无更多</span></div>
        </div>
    </div>
    <div id="js_pc_qr_code" class="qr_code_pc_outer">
        <div class="qr_code_pc_inner">
            <div class="qr_code_pc">
                <img id="js_pc_qr_code_img" class="qr_code_pc_img" src="/rr?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=fSEfaZBSnOBlNEJfI8qHrpxeSdAtS-TYq8Tg1cxX8Pjk1xXK-YB9ES*Hq*CRbAq178JHxcqtcknsgm6CjlKt6BWVtEBFHFzIRm9hSWjtzaY=">
                <p>Scan QR Code via WeChat <br> to follow Official Account</p>
            </div>
        </div>
    </div>
</div>


        <script nonce="">
    var __DEBUGINFO = {
        debug_js : "//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/debug/console3a696a.js",
        safe_js : "//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/safe/moonsafe3a696a.js",
        res_list: []
    };
</script>

<script nonce="" type="text/javascript">
(function() {
	var totalCount = 0,
			finishCount = 0;

	function _loadVConsolePlugin() {
		window.vConsole = new window.VConsole();
		while (window.vConsolePlugins.length > 0) {
			var p = window.vConsolePlugins.shift();
			window.vConsole.addPlugin(p);
		}
	}

	function _addVConsole(uri, cb) {
		totalCount++;
		var url = '//res.wx.qq.com/mmbizwap/zh_CN/htmledition/js/vconsole/' + uri;
		var node = document.createElement('SCRIPT');
		node.type = 'text/javascript';
		node.src = url;
		node.setAttribute('nonce', '');
		if (cb) {
			node.onload = cb;
		}
		document.getElementsByTagName('head')[0].appendChild(node);
	}
	if (
		(document.cookie && document.cookie.indexOf('vconsole_open=1') > -1)
		|| location.href.indexOf('vconsole=1') > -1
	) {
		window.vConsolePlugins = [];
		_addVConsole('3.0.0/vconsole.min.js', function() {

			_addVConsole('plugin/vconsole-mpopt/1.0.1/vconsole-mpopt.js', _loadVConsolePlugin);
		});
	}
})();
</script>

        <script>window.__moon_host = 'res.wx.qq.com';window.moon_map = {"biz_common/utils/respTypes.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/utils/respTypes3a696a.js","biz_common/utils/url/parse.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/utils/url/parse3a696a.js","biz_common/template-2.0.1-cmd.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/template-2.0.1-cmd3a696a.js","biz_wap/jsapi/core.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/jsapi/core3d3b86.js","biz_wap/utils/mmversion.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/utils/mmversion3de208.js","biz_common/dom/class.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/dom/class3a696a.js","biz_common/utils/string/emoji.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/utils/string/emoji3a696a.js","biz_wap/utils/ajax.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/utils/ajax3ff7ef.js","history/profile_history.html.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/history/profile_history.html3a696a.js","biz_common/utils/string/html.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/utils/string/html3a696a.js","history/template_helper.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/history/template_helper3a696a.js","appmsg/cdn_img_lib.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/appmsg/cdn_img_lib3de0e1.js","biz_common/dom/event.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_common/dom/event3a696a.js","history/profile_history.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/history/profile_history3a696a.js","sougou/profile.js":"//res.wx.qq.com/mmbizwap/en_US/htmledition/js/sougou/profile3a696a.js"};</script><script type="text/javascript">window.__wxgspeeds={}; window.__wxgspeeds.moonloadtime=+new Date()</script><script  type="text/javascript" src="//res.wx.qq.com/mmbizwap/en_US/htmledition/js/biz_wap/moon3f6b3e.js"></script>
<script type="text/javascript">

    var biz = "ODUzMjkwMzYx" || "";
    var src = "3" ;
    var ver = "1" ;
    var timestamp = "1534903201" ;
    var signature = "oWQ6l0dmX*b6mEconHeAMfakPTodfbM75Dd*-IZ57RSuE-TtzhIObCOECmhZF0BXhUNrhmmEUp0Ejj*HQW7zIQ==" ;
    var name="hsb88880000"||"华商报";
        var msgList = {"list":[{"app_msg_ext_info":{"audio_fileid":0,"author":"🌏华商君","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8bDe7inpsUCHTMqMkJ0zrNVPgy1*i0WQ8cmhZ4pUzxTosBcTXKOVmgNPor0U86xpPfuwSog60SuHTkJ8Ma2nNw4=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnWfk6EexsIfBPIibyPPOB3AD9dt6uRJ4ATk04pUxDA6aM3EHMoV2H2XQ/0?wx_fmt=jpeg","del_flag":1,"digest":"🍀昨日今晨，最新最快最有价值的讯息简报","duration":0,"fileid":507118904,"is_multi":0,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[],"play_url":"","source_url":"","subtype":9,"title":"8月22日周三【新闻速览一分钟】"},"comm_msg_info":{"content":"","datetime":1534891859,"fakeid":"853290361","id":1000001937,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*kHZUuAyXqPqlggSro6Gx1UWdmzHL7eLQUIHW1lrUczSmohrQ8pHZtFhbtNydalues=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpAic132KX4fuK5SVHu4vj6sYgVEmEY0QGNztpibsEjRTPRBdNiabejnYrgQ/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507119039,"is_multi":1,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*kF449PMHcr38OhG84P9y8xAKf5ScnNNzqVj3uYdcSrjo6Npz6BYgjU2A862GMbXvE=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpA8LpTPNdXLlMjjKV5wtFlN5J2BPj9bHaFzRRGYYuK3gQzphVbISP6kQ/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507119032,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"还有17户不同意拆迁方案，宝鸡一9层居民楼被强行推倒"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*nOTt9f-imn0g9j75rEzHvR8MDmPZoGCFEJ1oHaMjypNuu-1--9ujBdkJls8qkxlWU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpAcpjTXlWpkib5JUdXzxJ25cumOMLPic5DETvbs40bFDIh5TxpxvW25zlw/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507119003,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"一线城市房租普涨，西安房租却降了！原因是..."},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*lLsc7w7BHztf8FA5-0rdWac661v1HlyhtmiYGkpHT1jU2J7H4Unb0EGL7RtnhUeco=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpARngb9388RvkPjxFlSVGELsYcjuZeQhbSmzrJq0OKC9Mvw8IOvGrQdg/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507119025,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"亲妈逼女儿卖掉3套房，拿出百万替儿子还债！女儿做出惊人决定"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*n0KciQb7qwzYdBDfSVNFkdfFJq2qHR8HUfxbwsnJwW7RgDHL77ZNt4HosCAQsNOOI=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpAlhuVbHV0iaxnwsWfqh4wpBSiaOV71MqsQunLtEdYKyk0YWAfkjPXU5hw/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507119026,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"女司机被5人抢车后遭挟持杀害！一秒抢车案例，视频太吓人！"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ReoiSwbsuthAsRBXiNpe*lrgmWAHolmu0jtTMI5Z0IDrehL262GQ9p8mPCfZV*QvD7GobekwlS5Ot4dIGt5wUU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpAGaanqfamWdWbCUEuWWicfHI9hFMFFwGDLCWFsXqMiczq08LXTDjNl0ew/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118999,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"沿着西安这条公交线路走，据说可以穿越40年！"}],"play_url":"","source_url":"","subtype":9,"title":"被继母虐待的鹏鹏还没“醒”来，生母即将生产，如今他身边只有护工陪伴"},"comm_msg_info":{"content":"","datetime":1534854433,"fakeid":"853290361","id":1000001936,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Z83Pgb1G9ePRxvl7-zWbGuvK4WihIMBfg5G0Qn52suL9ociEi4zp6uYQycNaWUyteyTeR2fuHxwicD3ErL16AM=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiajiblRbXaHWe0urCicZOjjibpAgepU6Rw9ea1QSEibTGOA3rMgIxhA1cOPdDKCXwMBvNibjVFXAsPtNJUA/0?wx_fmt=jpeg","del_flag":1,"digest":"","duration":0,"fileid":507118988,"is_multi":0,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[],"play_url":"","source_url":"","subtype":9,"title":"华商快讯：西安莲湖官方通报扔烟头拍照事件调查结果（附视频）"},"comm_msg_info":{"content":"","datetime":1534819416,"fakeid":"853290361","id":1000001935,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"🌏华商君","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8YZkcBOHJsv47n88h135NVEb*z0sHexxdq*QT03l6aR6yeKxq51NrBRncytLSKeDrTPK08ThzFpxxmZ1wIwIgRU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnUMJS7Pvcq8QOz4nibksDn3eyAfeb7VTvhyBMysmeSZIfO2yA4f1aNFg/0?wx_fmt=jpeg","del_flag":1,"digest":"🍀昨日今晨，最新最快最有价值的讯息简报","duration":0,"fileid":507118901,"is_multi":1,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8YZkcBOHJsv47n88h135NVH92FFobtU2jZu3xDm5M9rS68x6DlAztNEDbZ0z2zaUbTSHuvn2Ci5x*CJuHmIg82c=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnEEL9m182TQT5x91zHR4zHKKzjRrh2cfReS0gpiaGGlxmgMLWVlTlOUg/0?wx_fmt=jpeg","del_flag":1,"digest":"冬枣又叫做雁来红、苹果枣、冰糖枣等，是品质最好的鲜食枣品种。冬枣不仅好吃，营养价值也很丰富，","duration":0,"fileid":507118912,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"https://j.youzan.com/iHbuNY","title":"不是所有冬枣都叫“大荔冬枣”!"}],"play_url":"","source_url":"","subtype":9,"title":"8月21日周二 【新闻速览一分钟】"},"comm_msg_info":{"content":"","datetime":1534805543,"fakeid":"853290361","id":1000001934,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gRGAQoFRE30vd5dEdZcxd29ujVc1QogQ4Rmj7cH5RXvTRsQ8Icbr4Dz0mZv19pgJ-U=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnFib2OykiaT5XQazqFkjtFUrwkj3YIGsUl8DfSKlV6yxeEDXUIRRyIv2A/0?wx_fmt=jpeg","del_flag":1,"digest":"西安人挺住，熬过这两天，天就要凉快了！接下来，还有这些事值得期待","duration":0,"fileid":507118952,"is_multi":1,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gQoPzqGH-YBGyv0ymEqESw0xc*gVJA-QbddYsKj0WT22IQ9Dd2RA7DDtnHXp9uejck=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnNUsBytYHdpjYu3aY3J8Dt0UN9fCcyq5j59icHd9qKEu6BBOdiagrrfTQ/0?wx_fmt=jpeg","del_flag":1,"digest":"明年，西安甲醇出租车将达一万辆！不达标企业和司机将退出行业","duration":0,"fileid":507118935,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"明年，西安甲醇出租车将达一万辆！不达标企业和司机将退出行业"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gTlYyq85clJzCUKwATdbiqEH9e8wd2fQbtke7S49QxMfkgl0sAelff1OBwfk8W-h1k=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnplttATb7pia9LB7v5lIS5sGXSNbtrWtXqibwdp3qd6fibLu4MtV3w1KYw/0?wx_fmt=jpeg","del_flag":1,"digest":"网传“西安市临潼区某街办查封灶台”，临潼区刚刚回应","duration":0,"fileid":507118948,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"网传“西安市临潼区某街办查封灶台”，临潼区刚刚回应"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gRSxe1Sp8pXoekGVnrVCX-QpPg16cVkMzsS0tUhlATc-jR1EVSd*169XNQDpZyq8h4=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqndk5fT4FLRXWgqiaib00ONQVqGU8u1VCtLQrO8qJu6eMfI486yuicaY8iaQ/0?wx_fmt=jpeg","del_flag":1,"digest":"西安这位女乘客，今早打车11元你微信错付了5568元，的哥急寻你退款！","duration":0,"fileid":507118947,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"西安这位女乘客，今早打车11元你微信错付了5568元，的哥急寻你退款！"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gTV7WZX1gZLJmVa8dhSZSZw5LrfB09QSUERccwdnuvtF1auOsSjH90tyimtWoDsj8A=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqn5tqUPtELyG6OEvWOziahBBEWSt8nicngJmI9rLXtibU4bYg8GcgxUtp6Q/0?wx_fmt=jpeg","del_flag":1,"digest":"27岁年轻人感冒后死亡，8个脏器5个衰竭,只因做了这件事!","duration":0,"fileid":507118921,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"27岁年轻人感冒后死亡，8个脏器5个衰竭，只因做了这件事!"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gQS9gdDWKhJvqHbvHZpdF095gXfWWKLeufdtO*9pIBATd4eRy5b20dFtCNbeEJhfG8=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnSkwDLOeebjeoECdibsNoQCPh9BYWuKwK3tZykwa0jHxOxTfT1PzuJzA/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118925,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"西安人，想知道你出生的那年发生了哪些大事？快来这条路找答案"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8RILtQjYQ3VqTzCX91fC6gSOIKww8g8WjA65TMe3sg-jS0*L6K31bwoX*Rf59SiksJDlfGUTkWekekTIvrY0UnU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagq04xYZ0zWT8BiaUBfLicWqnxCbKiakKAw5MLba4YSqF6d6rQHj2NPPv0diaDxhfYcu5lwkia1O4f3KJQ/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118878,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"中国消费者挑剔？ 看全新BMW X3如何满足中国用户的期许！"}],"play_url":"","source_url":"","subtype":9,"title":"西安人挺住，熬过这两天，天就要凉快了！接下来，还有这些事值得期待"},"comm_msg_info":{"content":"","datetime":1534755022,"fakeid":"853290361","id":1000001933,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"🌏华商君","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8TCMRFHgqgJUsf-ZeQ1OZ8U59Vmdaux3HvwXl7B3Y50H9AJ025VIZXa14PTKksNWLO*3suLhLfNidiv8b75LQL0=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiahQpr58W0G1M4qNoazovbGuNMAwYibI3Gfk27Neypcg9vARbSYAnAEeTGbb03l7ltyD1DYxiaxx5vyQ/0?wx_fmt=jpeg","del_flag":1,"digest":"🍀昨日今晨，最新最快最有价值的讯息简报","duration":0,"fileid":507118654,"is_multi":0,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[],"play_url":"","source_url":"","subtype":9,"title":"8月20日周一 【新闻速览一分钟】"},"comm_msg_info":{"content":"","datetime":1534718524,"fakeid":"853290361","id":1000001932,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Y6P*XtFVVGoxw4SS12fSdd7ufgwEL1759oaTpd-ILpcKNlsjsArJkityK86O6Efw7guy1GwpuPvKEOKwHGfXc8=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib050XzVyGzytpcpo1YlvgXolnUNucXPOqspWX3NqYFyHDGclMRzuVlecQ/0?wx_fmt=jpeg","del_flag":1,"digest":"小伙将新房租给漂亮女生， 一年后进门快吐了：好几个保洁阿姨被吓跑！","duration":0,"fileid":507118822,"is_multi":1,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Y6P*XtFVVGoxw4SS12fSdeeycMuABG0V4Ds8uE-2*vG8NkRnlqSvRG9eV3Xv9YAqMxWMsK*oSByoSfbei*zhsU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiahzIH5as3sExl4vLAxSvCnXceC0oiaU8JNZ8nG0DgCGI4yk84uIk4ah4H7HrV7jFz1ZTAtmvb1I8CQ/0?wx_fmt=jpeg","del_flag":1,"digest":"收到高中录取书第三天，陕西15岁男孩突发怪病！","duration":0,"fileid":507118826,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"收到高中录取书第三天，陕西15岁男孩突发怪病！"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Y6P*XtFVVGoxw4SS12fSdf0RwiVrMAVAJ26miBLbTMb2CE7-f4Hj-iLE1SBmVTyQcBl5BjR5l9k1dfhGs0*ve0=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib05Xc2wZT5wM5Zy4FVWxRpWhHiapHyjBemoCua3Inib84tyFtnTaDKKrhIw/0?wx_fmt=jpeg","del_flag":1,"digest":"男子上门寻仇，发现只有对方女儿和女友在家，他竟然…","duration":0,"fileid":507118823,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"男子上门寻仇，发现只有对方女儿和女友在家，他竟然…"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Y6P*XtFVVGoxw4SS12fSdfYp0HEXo9GyioDP1mynGdY1qP80EtUFJnDh5sGygU9eoRqxXFbZM*3mJLNDloFQJk=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiahzIH5as3sExl4vLAxSvCnXcAoSR9eNBOe7Z76Ton3oz8MzqfqUw4zY8EvfYOBJSibS1JePyIic8mVA/0?wx_fmt=jpeg","del_flag":1,"digest":"35套房4000万家财，却为40万车贷躲了十年…这两口子火了","duration":0,"fileid":507118827,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"35套房4000万家财，却为40万车贷躲十年…这两口子火了"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8Y6P*XtFVVGoxw4SS12fSdeN47vSUSi5lazOJBS-RY45L605Zm2ugt-1Mdmeuk3N-vXa5WMRlS4WkCGd6hKIPGI=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiahzIH5as3sExl4vLAxSvCnXl2gxE5Yvric0fjownLUKQVgntP21rrs9p7PoLx8unbntcXCNCZPtAtA/0?wx_fmt=jpeg","del_flag":1,"digest":"不是奶茶是“毒药”！这两款奶茶竟检出禁用物质，喝多会慢性中毒","duration":0,"fileid":507118830,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"不是奶茶是“毒药”！这两款奶茶竟检出禁用物质，喝多会慢性中毒"}],"play_url":"","source_url":"","subtype":9,"title":"小伙将新房租给漂亮女生， 一年后进门快吐了：好几个保洁阿姨被吓跑"},"comm_msg_info":{"content":"","datetime":1534666413,"fakeid":"853290361","id":1000001931,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"🌏华商君","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8cUg3vl9TNzHSmSpkR7*iN1yKtAjUwxgzc7t8XXRdfr16XGB5sw9PR3d3DvvyIN9JpuLcczvdPChTqOeOBowYU8=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagn3BpcXqITNgwmb61uzPOXINY3I23aFib6Urm1RsmMw9CAcj9vyP7VshjhFZgNAPQYDsTLibIvYjKQ/0?wx_fmt=jpeg","del_flag":1,"digest":"🍀昨日今晨，最新最快最有价值的讯息简报","duration":0,"fileid":507118592,"is_multi":0,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[],"play_url":"","source_url":"","subtype":9,"title":"发现秦岭北麓违建  4种途径可举报【8月19日周日 新闻速览一分钟】"},"comm_msg_info":{"content":"","datetime":1534632077,"fakeid":"853290361","id":1000001930,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8T43BixtEKvFhcEsTjpU1KJvztKxqx3lMK3AtWOB4s3YqCeg2keSp0YfOBATKhqj3lw6vB77jyZZpgAa6leDH5U=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib054ibhcxtXiaicDDua9ZjUP7GlzISEcIYDtZibnHaz2xQpKiaxkCJ6b3yH8wQ/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118791,"is_multi":1,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8T43BixtEKvFhcEsTjpU1KIGay3hCV9oXBVKXbJxKRk9rWbmGpuvHuuRVnNJjQeR*yCk7M400c1tf5uy-CYJmfo=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib05OTTaadSpyc9FqtA1L5tG3UD0VyMqwHI3GLzSdNd6GRDl2FDskZicibMw/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118786,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"7岁男孩悬空，爬在七楼窗外！爸爸一个举动惊呆众人"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8T43BixtEKvFhcEsTjpU1KJJZks1EppjBYK*MN*9zYsM*eS16SyzDQEDf69Yjz0cDTFlyOBOD3cFf1ahjCsLTdU=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib05p7suVldXMmYoMnYiaa5v5rmacbZ8WiavwhOILLaNDjBOt2eEE9IoqGxg/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118785,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"“妈妈，假装我是你唯一的儿子”8岁男孩写给妈妈的信，令人心碎"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8T43BixtEKvFhcEsTjpU1KJ5p0hA7FYtVC8Odb7DW3t4x6ij2yoL0QccQY4IUqwrqqjvA1ZOYskmZjdCckleeeo=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib05DsIaXxNibbFoEicxlHo8SEQJy1YSq0WU8A12ia4kDKMleicOlrq3YLISJA/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118784,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"比地沟油还损！很多人都爱喝，还供不应求！"},{"audio_fileid":0,"author":"","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8T43BixtEKvFhcEsTjpU1KJ4lc1pCtO*9vouvCKnzuRnqn1EtLrTMQiie72e*5*rwwer5sRvYmzAiQQZVdTu*GQ=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiagWBrFPm8Khd8CcK1InCib05DPZj74P0uCmyViaaPleZUg1UicnKy7MJsZAIYBo0ClEZbvuooYDG6B5Q/0?wx_fmt=jpeg","del_flag":1,"digest":"点击上方“华商报”可快速关注哦！","duration":0,"fileid":507118781,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"play_url":"","source_url":"","title":"男子频频上厕所，一查竟患了癌！他很喜欢吃这个……"}],"play_url":"","source_url":"","subtype":9,"title":"八旬瘫痪老人与保姆结婚遗赠房屋，老人过世后保姆被赶出家门，法院这样判"},"comm_msg_info":{"content":"","datetime":1534581451,"fakeid":"853290361","id":1000001929,"status":2,"type":49}},{"app_msg_ext_info":{"audio_fileid":0,"author":"🌏华商君","content":"","content_url":"/s?timestamp=1534904272&amp;src=3&amp;ver=1&amp;signature=YixWUCsR7Gsd6yyMVXdyyvhweqZD2B8e1NPQM3JFWVMXAcuXNlQVPwnBGeMY01a8lEhf1ADxtv238Rp-8ZDc8ceO52ZdZJK1ALHO8Wlxca55Axd1m7HLuvw-xKvRJciP8cfxDWNChpNfoN1-gzuYfWqRMkyOur9wsix1q1P11Do=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/Jyco923vDiahxqnn1mkicDf8iatlDO4L2icX4oBTpejEict6qcglCoZyUib9k3vmrefhUKibKo3XWY8lCicoe2vGXRCPSw/0?wx_fmt=jpeg","del_flag":1,"digest":"🍀昨日今晨，最新最快最有价值的讯息简报","duration":0,"fileid":507118740,"is_multi":0,"item_show_type":0,"malicious_content_type":0,"malicious_title_reason_id":0,"multi_app_msg_item_list":[],"play_url":"","source_url":"","subtype":9,"title":"秦岭北麓40栋违建别墅开拆 总面积达上万平方米【8月18日周六 新闻速览一分钟】"},"comm_msg_info":{"content":"","datetime":1534546576,"fakeid":"853290361","id":1000001928,"status":2,"type":49}}]};
        seajs.use("sougou/profile.js");
</script>

    </body>
    <script nonce="" type="text/javascript">document.addEventListener("touchstart", function() {},false);</script>
</html>
'''

import re
import json
import datetime

articleRe = "var msgList = (.*)?;"

res = re.findall(articleRe, html)[0]
# print(res)
data = json.loads(res)
print(len(data['list']))
# for articleList in data['list']:
# article_msg_ext_info = articleList['app_msg_ext_info']['multi_app_msg_item_list']
# # print(article_msg_ext_info)
# if article_msg_ext_info:
#     for article_msg in article_msg_ext_info:
#         print(article_msg['title'])


for articleList in data['list']:
    article_msg_item_list = articleList['app_msg_ext_info']['multi_app_msg_item_list']
    # 文章标题1
    title1 = articleList['app_msg_ext_info']['title']
    # 文章1时间
    time1 = articleList['comm_msg_info']['datetime']

    time1 = datetime.datetime.fromtimestamp(time1)
    print(title1,time1)

    if article_msg_item_list:
        for article_msg in article_msg_item_list:
            # 文章标题2
            title2 = article_msg['title']
            print(title2, time1)
