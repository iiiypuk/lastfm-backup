#!/usr/bin/env python3

import lastfm_import as lfm

API_KEY = '0e5070361556658180f9b1518b341eda'
USERNAME = 'goodgame'

if __name__ == '__main__':
  pages = lfm.get_pages(USERNAME, API_KEY)

  for page in range(1, pages + 1):
    tracks = lfm.get_scrobbles(USERNAME, API_KEY, page)

    for track in tracks:
        print('%s - %s' % (track['artist']['#text'], track['name'],))
