#!/usr/bin/env python3

import json
import urllib.request

__author__ = 'Alexander Popov'
__version__ = '0.1.1'
__license__ = 'Unlicense'


def get_pages(username, api_key):
    response = urllib.request.urlopen(
           'http://ws.audioscrobbler.com/2.0/'
           '?method=user.getrecenttracks&user=%s&api_key=%s&format=json' %
           (username, api_key,)).read().decode("utf8")
    pages = int(json.loads(response)['recenttracks']['@attr']['totalPages'])

    return(pages)


def get_scrobbles(username, api_key, page):
    response = json.loads(
               urllib.request.urlopen(
                'http://ws.audioscrobbler.com/2.0/'
                '?method=user.getrecenttracks&user=%s'
                '&api_key=%s&page=%d&format=json' %
                (username, api_key, page,))
               .read().decode("utf8"))['recenttracks']['track']

    return(response)

if __name__ == '__main__':
    with open('./config.json') as f:
        CONFIG = json.loads(f.read())

    PAGES = get_pages(CONFIG['username'], CONFIG['api_key'])
    COUNT = 1
    TRACKS = []
    while COUNT <= PAGES:
        print('\r%d%%' % (COUNT * 100 / PAGES), end='')
        response = get_scrobbles(CONFIG['username'], CONFIG['api_key'], COUNT)

        for track in response:
            TRACKS.append({'artist': track['artist']['#text'],
                           'name': track['name'],
                           'album': track['album']['#text'],
                           'date': track['date']['uts']})

        COUNT += 1

    with open('%s.json' % (CONFIG['username']), 'w+', encoding='utf-8') as f:
        f.write(
            json.dumps(TRACKS, indent=4, sort_keys=True, ensure_ascii=False))
    print('\r%d tracks saved in %s.json!' % (len(TRACKS), CONFIG['username'],))
