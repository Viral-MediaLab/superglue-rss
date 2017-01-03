# a script to generate an RSS file fore each channel from the begining of time,
# in order to backfill Media Cloud data
from generate_rss import generate_rss_feed

channels = [
"002",
"025",
"202",
"206",
"229",
"231",
"232",
"237",
"242",
"244",
"249",
"264",
"276",
"278",
"284",
"349",
"350",
"351",
"353",
"355",
"356",
"357",
"360",
"375"]

for channel in channels:
    rss_str = generate_rss_feed(channel, since_time=-1)
    filename = "backfilling_data/%s.rss"%channel
    if rss_str:
        with open(filename, "w") as f:
            f.write(rss_str)
    else:
        print "channel %s is empty"%channel
