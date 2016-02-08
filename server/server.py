import os.path
from flask import Flask, send_file

app = Flask(__name__, static_url_path='/static')


@app.route('/tiles/<zoom>/<y>/<x>', methods=['GET', 'POST'])
def tiles(zoom, y, x):
    default = './data/JTileDownloader/USA/5/4/13.png'
    filename = './data/JTileDownloader/USA/%s/%s/%s.png' % (zoom, x, y)
    if os.path.isfile(filename):
        return send_file(filename)
    else:
        return send_file(default)


@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
