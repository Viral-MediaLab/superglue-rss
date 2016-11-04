'''
    feedgen_facebook.instant_article
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce Facebook InstantArticle.

    :copyright: 2016, Jonathan Vanasco <jonathan@findmeon.com>

    :license: FreeBSD
'''

from lxml import etree

from feedgen.ext.base import BaseExtension
from feedgen.ext.base import BaseEntryExtension


NS_CONTENT = 'http://purl.org/rss/1.0/modules/content/'


class FacebookInstantArticleExtension(BaseExtension):
    """
    FeedGenerator extension for FacebookInstantArticle.

    We don't need any properties on the feed, just the entry.

    Sample Usage:

    fg = FeedGenerator()
    fg.register_extension('facebook_ia',
                          feedgen_facebook.FacebookInstantArticleExtension,
                          feedgen_facebook.FacebookInstantArticleEntryExtension,
                          atom=False, rss=True)
    for posting in postings:
        fe = fg.add_entry()
        fe.facebook_ia.content(posting_encoded)


    The article content will then appear in a CDATA element identified as <content:encoded>
    """
    pass


class FacebookInstantArticleEntryExtension(BaseEntryExtension):
    def __init__(self):
        self.__fb_content = None

    def extend_rss(self, entry):
        if self.__fb_content:
            _key = etree.SubElement(entry, '{%s}encoded' % NS_CONTENT)
            _key.text = etree.CDATA(self.__fb_content)
        return entry
# -*- coding: utf-8 -*-
'''
    feedgen.ext.facebook_instant_article
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce Facebook InstantArticle.

    :copyright: 2016, Jonathan Vanasco <jonathan@findmeon.com>

    :license: FreeBSD
'''

from lxml import etree

from feedgen.ext.base import BaseExtension
from feedgen.ext.base import BaseEntryExtension


NS_CONTENT = 'http://purl.org/rss/1.0/modules/content/'


class FacebookInstantArticleExtension(BaseExtension):
    """
    FeedGenerator extension for FacebookInstantArticle.

    We don't need any properties on the feed, just the entry.

    Sample Usage:

    fg = FeedGenerator()
    fg.register_extension('facebook_ia',
                          feedgen_facebook.FacebookInstantArticleExtension,
                          feedgen_facebook.FacebookInstantArticleEntryExtension,
                          atom=False, rss=True)
    for posting in postings:
        fe = fg.add_entry()
        fe.facebook_ia.content(posting_encoded)


    The article content will then appear in a CDATA element identified as <content:encoded>
    """
    pass


class FacebookInstantArticleEntryExtension(BaseEntryExtension):
    def __init__(self):
        self.__fb_content = None

    def extend_rss(self, entry):
        if self.__fb_content:
            _key = etree.SubElement(entry, '{%s}encoded' % NS_CONTENT)
            _key.text = etree.CDATA(self.__fb_content)
        return entry

    def content(self, content=None):
        '''Get or set the content:encoded.

        :param content: The encoded content.
        :returns: The content.
        '''
        if content is not None:
            self.__fb_content = content
        return self.__fb_content

    def content(self, content=None):
        '''Get or set the content:encoded.

        :param content: The encoded content.
        :returns: The content.
        '''
        if content is not None:
            self.__fb_content = content
        return self.__fb_content
