# -*- coding: utf-8 -*-
'''
Functions to perform public ip query for the host machine
'''

# Import Python Libs
import contextlib
import socket
import urllib2

# Import salt libs
from salt.utils.validate.net import ipv4_addr as _ipv4_addr


def get_pubipv4(checkurl=None, timeout=1):
    '''
    Return the external IP v4 address
    '''
    default_urls = ('http://ip.appspot.com/',
                    'http://whatismyip.akamai.com/',
                    'http://ns1.dnspod.net:6666/',
                    'http://ipecho.net/plain',
                    'http://ifconfig.me/ip',
                    )
    check_urls = checkurl or default_urls
    check_timeout = timeout or 2

    for url in check_urls:
        try:
            with contextlib.closing(urllib2.urlopen(url, timeout=check_timeout)) as req:
                ipv4 = req.read().strip()
                if not _ipv4_addr(ipv4):
                    continue
            return ipv4
        except (urllib2.HTTPError,
                urllib2.URLError,
                socket.timeout):
            continue

    # Return an empty value as a last resort
    return ""
