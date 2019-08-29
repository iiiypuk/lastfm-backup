#!/usr/bin/env python3

import json
import urllib.request
import os.path

__author__ = 'Alexander Popov'
__version__ = '1.0.1'
__license__ = 'Unlicense'


def get_pages(username, api_key):
    response = urllib.request.urlopen(
           'http://ws.audioscrobbler.com/2.0/'
           '?method=user.getrecenttracks&user={0}&api_key={1}&format=json'
           '&limit=200'.format(username, api_key)).read().decode("utf8")
    pages = int(json.loads(response)['recenttracks']['@attr']['totalPages'])

    return(pages)


def get_scrobbles(username, api_key, page):
    response = json.loads(urllib.request.urlopen(
               'http://ws.audioscrobbler.com/2.0/'
               '?method=user.getrecenttracks&user={0}&api_key={1}&format=json'
               '&limit=200&page={2}'.format(username, api_key, page)
               ).read().decode("utf8"))['recenttracks']['track']

    return(response)

if __name__ == '__main__':
    CFG = dict()

    if os.path.exists('./config.json'):
        with open('./config.json') as f:
            CFG = json.loads(f.read())
    else:
        CFG['api_key'] = input('API Key: ')
        CFG['username'] = input('Username: ')

    PAGES = get_pages(CFG['username'], CFG['api_key'])
    curPage = 1
    tracks = []
    while curPage <= PAGES:
        print('\r{0}% [{1} of {2}]'.format((curPage * 100 / PAGES), curPage, PAGES), end='')
        response = get_scrobbles(CFG['username'], CFG['api_key'], curPage)

        for track in response:
            tracks.append({'artist': track['artist']['#text'],
                           'name': track['name'],
                           'album': track['album']['#text'],
                           'date': track['date']['uts']})

        curPage += 1

    with open('%s.json' % (CFG['username']), 'w+', encoding='utf-8') as f:
        f.write(
            json.dumps(tracks, indent=4, sort_keys=True, ensure_ascii=False))

    print('\n{0} tracks saved in {1}.json!'.format(
          len(tracks), CFG['username'],))
