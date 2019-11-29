#%%
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse
import os
import time
import random
import re
import pickle
from selenium.webdriver.chrome.options import Options
#%%
download_dir = 'D:\\chris_useful\\中国环境检测爬虫\\contents\\全国地表水质月报'
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    }
)
#%%
url_list = ['http://www.cnemc.cn/jcbg/qgdbsszyb/index.shtml',
            'http://www.cnemc.cn/jcbg/qgdbsszyb/index_1.shtml',
            'http://www.cnemc.cn/jcbg/qgdbsszyb/index_2.shtml',
            'http://www.cnemc.cn/jcbg/qgdbsszyb/index_3.shtml',
            'http://www.cnemc.cn/jcbg/qgdbsszyb/index_4.shtml',
            'http://www.cnemc.cn/jcbg/qgdbsszyb/index_5.shtml']
#%% start chrome
browser = webdriver.Chrome(options = chrome_options)
ROOT_URL = 'http://www.cnemc.cn/jcbg/qgdbsszyb/'
#%% useful funcitons
def show_html(html_str):
    '''
    把html文件存到当前目录show.html文件中
    '''
    with open('show.html', 'wt', encoding='utf-8') as f:
        f.write(html_str)

def get_url_contents(url, show=False, path=None):
    '''
    ---待修改---：加入网页等待过程，暂时没成功
    得到动态网页的html文件，用于后序分析
    args: 
        url: 网页地址
        path: 保存路径
    notes:
        browser 需要在文件开始地方初始化，初始化语句如下
                from selenium import webdriver
                browser = webdriver.Chrome()
    '''
    browser.get(url) # 模拟浏览器访问这个页面
    time.sleep(2) # 等待2秒，保证页面正确加载, 使用动态网页暂时没成功
    html = browser.page_source # 得到页面的html
    bf = BeautifulSoup(html, 'html.parser')
    html_str = bf.prettify() # 美化html文档
    if show == True:
        show_html(html_str)
    if path != None:
        with open(path, 'wt', encoding='utf-8') as f:
            f.write(html_str) 
    return html_str

def get_url_file(url, save_path):
    '''
    从url获取文件，并保存到save_path文件夹下
    '''
    browser.get(url) # 模拟浏览器访问这个页面
    

#%% main 
for i in range(6):
    html = get_url_contents(url_list[i], show=True)
    bf = BeautifulSoup(html, 'html.parser')
    ans = bf.find('ul', attrs={'id':'contentPageData'})
    bns = ans.find_all('a', attrs={'target':'_blank'})
    for result in bns:
        link = result.attrs['href']
        link = parse.urljoin(ROOT_URL, link)
        file_name = result.get_text().strip()
        if link[-3:] == 'pdf':
            # 通过pdf连接下载pdf文件
            browser.get(link)
            # 判断文件夹中名字是否都是.pdf 不是则等待
            while len(os.listdir(download_dir)) == 0 or not all([i[-3:]=='pdf' for i in os.listdir(download_dir)]):
                time.sleep(1)
            # 重命名这个文件
            old_filename = max([os.path.join(download_dir, f) for f in os.listdir(download_dir)], key=os.path.getctime)
            newfilename = file_name
            os.rename(old_filename, os.path.join(download_dir, newfilename+'.pdf'))
        elif link[-5:] == 'shtml':
            # 根据链接
            html = get_url_contents(link, show=True)
            bf = BeautifulSoup(html, 'html.parser')
            bf_find = bf.find('a', attrs={'class':'pdf_link'})
            info = re.search(r'href="[.]/\w{22}[.]pdf', html)
            if bf_find != None:
                pdf_name = bf_find.attrs['href']
            elif info != None:
                pdf_name = info.group(0)
                pdf_name = pdf_name[6:]
            else:
                print(link, " ", file_name)
                continue
            link_pdf = parse.urljoin(link, pdf_name)
            # 下载PDF
            browser.get(link_pdf)
            # 判断文件夹中名字是否都是.pdf 不是则等待
            while len(os.listdir(download_dir)) == 0 or not all([i[-3:]=='pdf' for i in os.listdir(download_dir)]):
                time.sleep(1)
            # 重命名这个文件
            old_filename = max([os.path.join(download_dir, f) for f in os.listdir(download_dir)], key=os.path.getctime)
            newfilename = file_name
            os.rename(old_filename, os.path.join(download_dir, newfilename+'.pdf'))
        else:
            print(link, " ", file_name)
            continue