# 中国环境监测总站-爬虫
本项目拟在得到中国环境监测总站中 "[中国环境状况公报](http://www.cnemc.cn/jcbg/zghjzkgb/)"、 "[全国地表水水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/)"、"[长江三峡工程生态与环境检测报告](http://www.cnemc.cn/jcbg/zjsxgcstyhjjcbg/)"、"[中国环境年报](http://www.cnemc.cn/jcbg/zghjtjnb/)"、"[全国生态环境质量报告](http://www.cnemc.cn/jcbg/qgsthjzlbg/)" 的所有报告。   

由于只有“全国地表水水质月报”内容较多，因此对于"[全国地表水水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/)"中的内容使用**网络爬虫**获得。其他报告人工点击下载得到。

# 直接下载已爬取内容
- 链接：https://pan.baidu.com/s/1cwuSd-v_HgHMbnkb6mULEQ 
- 提取码：cc61 
- 下载后解压即可看到下载的所有报告

# 如何运行代码
- 安装Python 3.X环境
- 安装chrome浏览器，以及chrome drive, 如何安装详见：
- 安装Python 依赖库
    ```shell
    $ pip install bs4 selenium re pickle
    ``` 
- 运行spyder.py
    ```shell
    $ cd Web-Crawler-environment
    $ mkdir contents
    $ python spyder.py
    ``` 

# 下载失败案例
在“全国地表水水质月报”中有部分内容无法下载，下面列出：

- [总站报告 | 2019年2月地表水环境质量](https://mp.weixin.qq.com/s/jZSpOCgXHx_ckX5gHEyVtQ) : 微信公众号页面，无pdf文件。

- [2015年全国地表水水质月报（8月份）](http://www.cnemc.cn/jcbg/qgdbsszyb/201509/t20150923_647223.shtml): pdf下载页面无法打开。

- [2012年12期水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/201305/t20130501_647192.shtml) :   无pdf页面。   
- [2012年11期水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/201304/t20130410_647191.shtml)  :   无pdf页面。   
- [暂停水质月报发布的通知](http://www.cnemc.cn/jcbg/qgdbsszyb/201106/t20110621_647188.shtml) : 无pdf页面。   
- [2007年11月水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/200804/t20080417_647183.shtml)  :  pdf下载页面无法打开。




- [2006年10月水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/200804/t20080417_647170.shtml) :  pdf下载页面无法打开。
- [2006年4月水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/200804/t20080417_647164.shtml)   :  pdf下载页面无法打开。
- [2006年3月水质月报](http://www.cnemc.cn/jcbg/qgdbsszyb/200804/t20080417_647163.shtml)  :  pdf下载页面无法打开。
