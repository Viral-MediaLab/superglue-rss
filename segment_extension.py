# -*- coding: utf-8 -*-
'''
	Extends the FeedGenerator to produce segments specific feeds.
'''

from lxml import etree
from feedgen.ext.base import BaseExtension,BaseEntryExtension

SEGMENT_NS = 'https://github.com/Viral-MediaLab/superglue-rss'

class SegmentExtension(BaseExtension):
	'''FeedGenerator extension for segment feeds.
	'''
	def extend_ns(self):
		return {'segment' : SEGMENT_NS}


class SegmentEntryExtension(BaseEntryExtension):
	'''FeedEntry extention for segment feeds
	'''
	def __init__(self):
		self.__segment_duration = None

	def extend_rss(self, entry):
		'''Add additional fields to an RSS item.
		:param feed: The RSS item XML element to use.
		'''
		if self.__segment_duration:
			duration = etree.SubElement(entry, '{%s}duration' % SEGMENT_NS)
			duration.text = self.__segment_duration

	def duration(self, segment_duration=None):
		'''Get or set the duration of the video segment.
		:param segment_duration: The duration of the video segment in seconds.
		:returns: The duration of the video segment in seconds.
		'''
		if not segment_duration is None:
			self.__segment_duration = segment_duration
		return self.__segment_duration
