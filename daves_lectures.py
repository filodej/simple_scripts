"""
This simple script traverses the http://www.dabeaz.com site hierarchy
and finds links to all pdf presentations created by David Beazley,
inspirative educator and SWIG creator.

I have created it as a simple excersise of declarative style of
Python programming covered in generator tutorial:

    http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf
"""
import urllib
import urlparse
import re

def gen_find_links( baseurl ):
    """Finds all url links in a HTML document represented by given url"""
    pattern = re.compile(r'href="(?P<url>.*)"')
    for url in pattern.findall( urllib.urlopen( baseurl ).read() ):
        yield urlparse.urljoin( baseurl, url )

def gen_unique_links( baseurl, queue_filter ):
    """Recursively finds all unique local links pointing from given URL"""
    visited_links = set()
    queue = [ baseurl ]
    while queue:
        url = queue.pop()
        for link in gen_find_links( url ):
            if link not in visited_links:
                visited_links.add( link )
                if queue_filter.match( link ):
                    queue.append( link )
                yield link

if __name__ == '__main__':
    baseurl = "http://www.dabeaz.com/"
    queue_filter = re.compile( baseurl + '.*\.html?$' )
    all_links = gen_unique_links( baseurl, queue_filter )
    local_links = ( url for url in all_links if url.startswith( baseurl ) )
    pdf_files = ( url for url in local_links if url.endswith( '.pdf' ) )

    for filename in pdf_files:
        print filename
