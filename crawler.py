# 从网上下载多张图片

import urllib.request
import os  # 在当前目录下创建一个新的文件夹
import re
import logging

logger = logging.getLogger(__name__)


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    logging.info('geting url=%s' % url)
    print(url)
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


# 打开需要下载图片的网站
def get_page(url):
    html = url_open(url).decode('utf-8')

    # 有待深究！！！！！！！！！！！！！
    page = re.findall(r'<span class="current-comment-page">\[(.+?)\]</span>',
                      html)

    return page[0] if page else None


# 在给定的网站中找到图片地址
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_address = re.findall(r'img src="(.+?)"', html)  # 把找到的图片地址放在列表中

    return img_address  # 返回一个包含图片地址的列表


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[
            -1]  # 此数据为图片的名字‘img src="http://wx3.sinaimg.cn/mw600/9e4dc7bdgy1fuaubizk6gj20hr0vkdod.jpg’，我们需要取最后一个反斜杠后边的作为保存图片的名字
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_picture(folder='picture', pages=10):
    if not os.path.exists(folder): os.mkdir(folder)  # 创建一个文件夹
    os.chdir(folder)  # 保存到picture文件夹

    url = "https://jandan.net/pic"
    page_num = int(get_page(url))  # 获得页面的地址

    for i in range(pages):
        page_num -= i
        page_url = url + '/page-' + str(page_num) + '#comments'
        img_address = find_imgs(page_url)
        save_imgs(img_address)


if __name__ == '__main__':
    download_picture()
