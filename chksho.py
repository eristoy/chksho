#!/usr/bin/env python
import shodan
import sys
import re
#Config
API_KEY = ""

#Input Check
if len(sys.argv) == 1:
    print 'Usage: %s <search query>' % sys.argv[0]
    sys.exit(1)

try:
    api = shodan.Shodan(API_KEY)
    #Do Search
    query = ' '.join(sys.argv[1:])
    result = api.search(query)

    # loop & print
    #info = {}
    for service in result['matches']:
        info = []
        info = ([service['ip_str'],service['hostnames'],service['port'],service['transport'],service['_shodan']])
        #info = str(info)[1:-1]
        ip, uhost, port, transport, _sho  = info
        module = _sho['module']
        #size = len(uhost)
        uhost = str(uhost)[1:-1]
        uhost = re.findall('\'.*\..*\..*', uhost)
        uhost = str(uhost)[1:-1]
        chost = uhost.replace('"','')
        chost = chost.replace("'","")
        #print uhost
        #if uhost:
        #if size == 1:
        #   u, host = uhost
        #else:
        #   host = "NA"
        sport = str(port)
        print "%s,%s,%s,%s,%s" % (ip, sport, chost, transport, module)
except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)
