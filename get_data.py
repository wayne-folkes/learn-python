import urllib2

def get_data_from_api(url)
    try:
        data = urllib2.urlopen(url).read()
        return data
    except urllib2.HTTPError, e:
        print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
        print "Network error: %s" % e.reason.args[1]

