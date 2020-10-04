#!/usr/bin/env python3

import lastfm_backup as lfm

API_KEY = "0"
USERNAME = "admin"

if __name__ == "__main__":
    pages = lfm.get_pages(USERNAME, API_KEY)
    count = 0

    for page in range(1, pages + 1):
        tracks = lfm.get_scrobbles(USERNAME, API_KEY, page)

        for track in tracks:
            print(
                "%s - %s"
                % (
                    track["artist"]["#text"],
                    track["name"],
                )
            )
            count = count + 1

    print("\nTotal scrobbling tracks: %d" % count)
