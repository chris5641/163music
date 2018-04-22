# -*- coding:utf-8 -*-
import requests
import time


API_URL = 'http://localhost:3001/'
headers = {
        'Connection': 'keep-alive',
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Referer': 'http://music.163.com/',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36"
    }
LIMIT = 30


def search(data, stype):
    start = time.time()
    if stype == 'song':
        d = dict(type=1, keywords=data, limit=LIMIT)
    elif stype == 'album':
        d = dict(type=10, keywords=data, limit=LIMIT)
    elif stype == 'playlist':
        d = dict(type=1000, keywords=data, limit=LIMIT)
    else:
        d = dict()
    r = requests.get(API_URL+'search', d, headers=headers)
    if r.status_code != 200:
        return False
    result = r.json()['result']
    end = time.time()
    print('search time: {}s '.format(end - start))
    return result


def get_song_info(song_id):
    url = API_URL + 'song/detail'
    r = requests.get(url, {'ids': song_id}, headers=headers)
    if r.status_code != 200:
        return False
    try:
        result = r.json()['songs'][0]
    except IndexError:
        return False
    return result


def get_album_info(album_id):
    url = API_URL + 'album'
    r = requests.get(url, {'id': album_id}, headers=headers)
    if r.status_code != 200:
        return False
    result = r.json()
    return result


def get_playlist_info(playlist_id):
    url = API_URL + 'playlist/detail'
    r = requests.get(url, {'id': playlist_id}, headers=headers)
    if r.status_code != 200:
        return False
    try:
        result = r.json()['playlist']
    except KeyError:
        return False
    return result
