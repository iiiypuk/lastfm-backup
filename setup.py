from distutils.core import setup

import lastfm_import

setup(
    name='lastfm_import',
    version=lastfm_import.__version__,
    description='Last.fm backup scrobbles library'
                ' and standartalone program.',
    author=lastfm_import.__author__,
    author_email='iiiypuk@fastmail.fm',
    url='https://github.com/iiiypuk/lastfm-import',
    py_modules=['lastfm_import'],
    scripts=['lastfm_import.py'],
    license=lastfm_import.__license__,
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
