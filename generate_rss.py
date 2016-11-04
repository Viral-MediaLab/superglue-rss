import time
import datetime
import pymongo
import pytz
from feedgen.feed import FeedGenerator
from pymongo import MongoClient
from channels import get_channel_data

DAY = 86400000
HOUR = 3600000
TEXT_LENGHT_THRESHOLD = 10
def millis():
    return int(round(time.time() * 1000))

def millis_since(num_days=2):
    return millis() - num_days*DAY


def get_segments_by_channel (channel):
    MONGO_URL = 'mongodb://um.media.mit.edu:27017/super-glue'
    collection = MongoClient(MONGO_URL).get_default_database()['media']
    videos_limit = 100
    media_with_segments = collection.find({
        "date_added":{"$gt":millis_since(10)},
        "story_segments":{"$exists": True},
        "is_news":{"$eq": True},
        "channel": {"$eq":channel}},
        sort=[('date_added', pymongo.DESCENDING)], limit=videos_limit)
    print media_with_segments.count()
    segments = []
    for media in media_with_segments:
        for i, segment in enumerate(media['story_segments']):
            if len(segment['text'])>TEXT_LENGHT_THRESHOLD:
                segments.append({
                'title':media['title'],
                'link': "%s#t=%.2f,%.2f"%(media['media_url_no_comm'],segment['start']/1000.0,segment['end']/1000.0),
                'description':segment['text'],
                'pubDate':media['date_added'],
                'guid': '%s_%d'%(media['_id'],i),
                'segment:duration': segment['start']-segment['end'],
                'enclosure': segment['thumbnail_image'] if 'thumbnail_image' in segment else ''
                })
    return segments

def generate_rss_feed (channel):
    segments = get_segments_by_channel(channel)
    channel_data = get_channel_data(channel)
    fg = FeedGenerator()
    fg.title(channel_data['name'])
    fg.link(href=channel_data['link'])
    fg.description(channel_data['description'])

    for segment in segments:
        fe = fg.add_entry()
        fe.guid(segment['guid'])
        fe.title(segment['title'])
        fe.description(segment['description'])
        fe.enclosure(segment['enclosure'], 0, 'image/jpeg')
        fe.link(href=segment['link'])
        fe.pubdate(datetime.datetime.fromtimestamp(segment['pubDate']/1000.0, pytz.utc))

    return fg.rss_str(pretty=True)
