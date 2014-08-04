#
#
import simplejson
import urllib
import urllib2

# Python SSL v3 bug - workaround 
import httplib
import ssl
from functools import partial

class fake_ssl:
    wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_SSLv3)

httplib.ssl = fake_ssl

# End workaround 

# GLOBALS 

#URL for ThreatRecon API 
my_TR_URL = "https://api.threatrecon.co/api/v1/search"

#API Key for user 
my_api_key = "8fd950d13d14306164dc28da97fbf09d"

# STEP 1 - Take input from CommandLine 
import sys
#
if (len(sys.argv)-1 == 0):
	print "No CLI Arguments, exiting"
	print "Need some value to check "
	print "EXAMPLE: python thisfile.py domain_name" 
	sys.exit(1)
else:
	#Working found data 
	num_args = len(sys.argv)-1
	if num_args > 2: 
		print "ERROR: Too many arguments"
		print "Try again"
		sys.exit(1)

my_data_query = sys.argv[1]

#DEBUG 
print "Checking your search was for [", my_data_query, "] "

# Step 2 - Validate data (taken from original code 
# Next version 

# Step 3 - Connect to API 
#
# Build URL 
parameters = { "api_key" : my_api_key, "indicator" : my_data_query } 
params = urllib.urlencode(parameters) 

# DEBUG - Exit before using URL for testing to prevent flooding of API server 
#sys.exit(1) 

# STEP 4 - Execute Query to ThreatRecon API 
req = urllib2.Request(my_TR_URL,params)

# Some basic HTTP error checking 
try:
 response = urllib2.urlopen(req)
except HTTPError, e:
       print " --------- ERROR ------ "
       print "ERROR CODE", e.code
       print "ERROR REASON", e.read()
json = response.read()
response_dict = simplejson.loads(json)

# STEP 5 - Response and Output 
# RAW - print response_dict 
print simplejson.dumps(response_dict, indent=4, sort_keys=False)

# Done and exiting 
print " Done " 
print " Exit Cleanly " 
sys.exit(1) 

