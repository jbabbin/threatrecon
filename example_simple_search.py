#
import urllib
import urllib2
from urllib2 import urlopen,quote
import simplejson 

### python SSL error work around 
import httplib
import ssl
from functools import partial

class fake_ssl:
    wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_SSLv3)

httplib.ssl = fake_ssl


indicator = 'serval.essanavy.com'

api_key = '8fd950d13d14306164dc28da97fbf09d'

#def query_threat_recon(indicator, api_key):
parameters = { "api_key" : api_key, "indicator" : indicator }
params = urllib.urlencode(parameters) 
#params = urllib.urlencode({'api_key': api_key, 'indicator': indicator})
f = urllib2.urlopen("https://api.threatrecon.co/api/v1/search",params)
data = simplejson.load(f)
results = data["Results"]
print simplejson.dumps(data, indent=4, sort_keys=False)
#	return results

#results = query_threat_recon(search,api_key)
