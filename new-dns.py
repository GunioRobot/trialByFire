#!/usr/bin/python2.6

import ldap
import sys

if __name__ == "__main__":

    # server = raw_input("Enter the ldapserver to connect to: ")
    # query = raw_input("Enter the inforamtion to be queryed: ") 
#dn = raw_input("Enter the domain for the query")

    server = "ldap://masterldap.csee.wvu.edu"
    dn = "svn004"
    query = "ou=Host, dc=csee, dc=wvu, dc=edu"
    
#connect to ldap
    l = ldap.initialize(server)
    
    
#while stuff in object 
    try:
        result = l.search(query)    

        while 1:
            
            if (data == []):
                break
            else:
                print host
                print ipHostNumber
                print macAddress
    except ldap.LDAPError, e:
        print "ERROR connectiong to Ldap"
        
