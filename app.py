from flask import Flask, render_template, jsonify
from generate_rss import generate_rss_feed

app = Flask(__name__)

@app.route("/<channel>")
def get_channel_rss_feed(channel):
    rss_str = generate_rss_feed(channel)
    return rss_str, 200, {'Content-Type': 'text/xml; charset=utf-8'}


if __name__ == "__main__":
    app.run(debug=True)
