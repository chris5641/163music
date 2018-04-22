from flask import (
    Flask, render_template, request, abort
)

from func import (
    search, get_song_info, get_album_info, get_playlist_info
)

app = Flask(__name__)
config = dict(
    debug=True,
    host='0.0.0.0',
    port=3000,
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search_view():
    data = request.args.get('s')
    stype = request.args.get('type')
    r = search(data, stype)
    if not r:
        abort(404)
    return render_template('search.html', result=r, type=stype, data=data)


@app.route('/player/')
def player_view():
    song_id = request.args.get('song')
    song = get_song_info(song_id)
    if not song:
        abort(404)
    return render_template('player.html', song=song)


@app.route('/playlist/')
def playlist_view():
    album_id = request.args.get('album')
    list_id = request.args.get('playlist')
    if album_id is not None:
        playlist = get_album_info(album_id)
        if not playlist:
            abort(404)
        return render_template('playlist.html', playlist=playlist, albumView=True)
    elif list_id is not None:
        playlist = get_playlist_info(list_id)
        if not playlist:
            abort(404)
        return render_template('playlist.html', playlist=playlist, playlistView=True)


if __name__ == '__main__':
    app.run(**config)
