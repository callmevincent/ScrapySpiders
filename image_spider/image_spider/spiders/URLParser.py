# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 17:40
# @Author  : Vincent Wang
# @Email   : wangyanbin@iyunbao.com
# @Desc URLParser.py href URL parser
from scrapy.http.response.html import HtmlResponse


class URLParser(object):

    @staticmethod
    def get_current_url_domain(response):
        # if isinstance(response, type(HtmlResponse)):
        #     print("is an instance of scrapy.http.response.html.HtmlResponse. ")
        _s = response.url.split('/')
        print(_s)
        _root = '/'.join(_s[0:3])
        print(_root)
    #
    # def __init__(self, current_url, href_url) -> None:
    #     super().__init__()
    #     self.domain = domain
    #     self.url = url
    #
    # def parse_url(self):
    #     if self.domain is None or self.url is None:
    #         return None
    #     if url.startswith('..'):
    #         url = _root + url.replace("..", "")
    #     if url.startswith('/'):
    #         url = '/'.join(_current_url.split('/')[0:3]) + url
    #     elif url.startswith('http') or url.startswith('www'):
    #         url = url
    #     else:
    #         # 相对路径
    #         if _current_url.endswith('/'):
    #             url = _current_url + url
    #         else:
    #             url = '/'.join(_current_url.split('/')[0:-1]) + '/' + url
