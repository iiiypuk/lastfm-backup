# Last.fm Backup

![Version](https://img.shields.io/pypi/v/lastfm-backup.svg?style=for-the-badge)
![License](https://img.shields.io/pypi/l/lastfm-backup.svg?style=for-the-badge)
![PyVersion](https://img.shields.io/pypi/pyversions/lastfm-backup.svg?style=for-the-badge)

### Features:
* Simple
* Three formats for export data:
    1. `dump` - JSON, direct from API
    2. `simple` - Artist, track name, album & date as JSON  
    3. `csv` - Artist, track name, album & date as comma separated values

### How to use:
* Stop scrobbling!
* Modify `config.json`.
* [Get API Key](http://www.last.fm/api/account/create).
* Run `lastfm_backup.py`.
* WAIT =)

### TODO:
- [ ] web service [see lfmbak](https://github.com/iiiypuk/lfmbak)
- [x] more output types (sqlite, csv)
- [ ] configurable output
- [ ] continue backup
- [ ] multi-threading
