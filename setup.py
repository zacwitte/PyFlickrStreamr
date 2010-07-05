
from distutils.core import setup

setup(
    name = 'PyFlickrStreamr',
    version = '0.1',
    description = 'PyFlickrStreamr provides a continuous, blocking python interface for streaming Flickr photos in near real-time. It is a wrapper around the Flickr photos.getRecent API.',
    author = 'Zachary Witte',
    author_email = 'zacwitte@gmail.com',
    url='http://github.com/zacwitte/PyFlickrStreamr',
    download_url = 'http://pypi.python.org/pypi/PyFlickrStreamr',
    platforms = 'Any',
    license = 'MIT License',
    long_description='''\
=============
 PyFlickrStreamr
=============
    
PyFlickrStreamr provides a continuous, blocking python interface for streaming Flickr photos in near real-time. It is a wrapper around the Flickr photos.getRecent API.

Learn more about the Flickr API at:

http://www.flickr.com/services/api/flickr.photos.getRecent.html

--------------
 Installation
--------------

To install, download the archive at http://pypi.python.org/pypi/PyFlickrStreamr and decompress, run python setup.py install.

-------
 Usage
-------
::
    import PyFlickrStreamr

    fs = PyFlickrStreamr('your_api_key_here', extras=['date_upload','url_m'])
    for row in fs:
        print str(row['id'])+"   "+row['url_m']

''',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
