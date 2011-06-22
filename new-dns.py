#!/usr/bin/python2.6

import ldap
import sys

if __name__ == "__main__":

    # server = raw_input("Enter the ldapserver to connect to: ")
    # query = raw_input("Enter the inforamtion to be queryed: ") 


    server = "ldap://masterldap.csee.wvu.edu"
    dn = "svn004"
    query = "ou=Host, dc=csee, dc=wvu, dc=edu"
    
#connect to ldap
    l = ldap.initialize(server)
    l.search(query)
    
#while stuff in object 
    print host
    print ipHostNumber
    print macAddress
    
    
