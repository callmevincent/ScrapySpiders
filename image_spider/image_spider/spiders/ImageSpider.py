# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:40
# @Author  : Vincent Wang
# @Email   : wangyanbin@iyunbao.com
# @Desc ImageSpider.py a image spider to fetch images from the specific domain (urls)
import scrapy
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse


class ImageSpider(scrapy.Spider):
    name = "ImageSpider"
    allowed_domains = [
        "www.ttgood.com", "m.ttgood.com"
    ]
    start_urls = [
        'https://www.ttgood.com/shanghai/'
    ]
    URL = []

    @staticmethod
    def get_current_domain(url):
        return '/'.join(url.split('/')[0:3])

    def parse_href_url(self, current_url, href_url):
        need_domain = False
        current_domain = self.get_current_domain(current_url)

        if '../' in href_url:
            need_domain = True
            href_url = href_url.replace("../", "")
        if './' in href_url:
            need_domain = True
            href_url = href_url.replace("./", "")
        if need_domain:
            href_url = current_domain + "/" + href_url

        if href_url.startswith('/'):
            href_url = '/'.join(current_domain) + href_url
        elif href_url.startswith('http') or href_url.startswith('www'):
            href_url = href_url
        else:
            # 相对路径
            if current_url.endswith('/'):
                href_url = current_url + href_url
            else:
                href_url = '/'.join(current_url.split('/')[0:-1]) + '/' + href_url
        return href_url

    def parse(self, response):

        self.logger.info('A response from %s just arrived!', response.url)
        for href_url in response.xpath("//a/@href").extract():
            if href_url in self.URL:
                continue
            else:
                self.URL.append(response.url)
            url = self.parse_href_url(response.url, href_url)
            yield Request(url, callback=self.parse)
