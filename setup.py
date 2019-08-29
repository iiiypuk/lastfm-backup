import setuptools

import lastfm_backup

setuptools.setup(
    name='lastfm-backup',
    version=lastfm_backup.__version__,
    description='Last.fm scrobbles backup',
    author=lastfm_backup.__author__,
    author_email='iiiypuk@fastmail.fm',
    url='https://github.com/iiiypuk/lastfm-backup',
    py_modules=['lastfm_backup'],
    scripts=['lastfm_backup.py'],
    license=lastfm_backup.__license__,
    platforms='any',
    keywords=['last.fm', 'lastfm', 'backup'],
    classifiers=['License :: Public Domain',
                 'Programming Language :: Python :: 3',
                 'Operating System :: OS Independent'],
    python_requires='>=3.0'
)
