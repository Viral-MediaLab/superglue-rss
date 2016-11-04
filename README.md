# superglue-rss
generating rss feed for adding Superglue data to Media Cloud

## RSS Spec:
The SuperGlue system will generate an RSS file nightly, one for each channel tracked.  This will include the latest N stories, such that N guarantees that it includes all the segments from the previous day (ie. around 500). We sketched out how SuperGlue data will be mapped onto an RSS feed:

## RSS Channel Elements:
**Title**: name of network (“MSNBC”)
**link**: url of channel (“msnbc.com”)
**description**: channel description from TMS?

## RSS Items:
one item for each “segment” in SuperGlue
**Title**: title of the show (ie. “MSNBC Live with Stephanie Rule”)
**link**: url to video of that show, starting at that segment’s timecode (note: this data won’t be available publicly)
**description**: closed caption text of the segment
**pubDate**: date it aired (in RSS standard format)
**guid**: the database id of the video and segment to uniquely identify it in SuperGlue
**segment:duration**: the duration, in seconds of the segment
**enclosure**: url to JPG still frame from segment(note: this data won’t be available publicly)
