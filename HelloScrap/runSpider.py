# -*- coding: utf-8 -*-
from scrapy import cmdline

# scrapy를 윈도우 상에서 구동하려면 pycharm 환경에서 cmdline.execute() 메서드를 이용하면 된다

cmdline.execute(
    "scrapy runspider currencySpider.py".split()
)

