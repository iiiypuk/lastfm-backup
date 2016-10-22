from distutils.core import setup

import lastfm_backup

setup(
    name='lastfm_backup',
    version=lastfm_backup.__version__,
    description='Last.fm backup scrobbles library'
                ' and standartalone program.',
    author=lastfm_backup.__author__,
    author_email='iiiypuk@fastmail.fm',
    url='https://github.com/iiiypuk/lastfm-import',
    py_modules=['lastfm_backup'],
    scripts=['lastfm_backup.py'],
    license=lastfm_backup.__license__,
    platforms='any',
    keywords=['last.fm', 'lastfm', 'import'],
    classifiers=['License :: Public Domain',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 ],
)
