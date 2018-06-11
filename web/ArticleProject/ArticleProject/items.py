# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    summary = scrapy.Field()
    project_id = scrapy.Field()
    tag_id = scrapy.Field()
    views_count = scrapy.Field()
    mobile_views_count = scrapy.Field()
    app_views_count = scrapy.Field()
    monographic_id = scrapy.Field()
    domain_id = scrapy.Field()
    goods_id = scrapy.Field()
    is_tovc = scrapy.Field()
    is_free = scrapy.Field()
    column_name = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    template_info = scrapy.Field()
    published_at = scrapy.Field()
    column_id = scrapy.Field()
    user_id = scrapy.Field()
    extraction_tags = scrapy.Field()
    user_info = scrapy.Field()
    highlight = scrapy.Field()
    _type = scrapy.Field()
    _score = scrapy.Field()
    favourite_num = scrapy.Field()
