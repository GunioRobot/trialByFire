#!/usr/bin/python2.6

import ldap
import sys




def retrieve_information(cn,key):
    #Defines the base information for connecting to the server
    static_options = {
        'ldap_uri': "ldap://masterldap.csee.wvu.edu",
        'people_dn': "ou=Hosts,dc=csee,dc=wvu,dc=edu",
        }

    #Creates and object of the database
    LDAP_OBJ = connect_to_ldap(static_options)
    #Stores the data
    result_set=[]


    try:
        result_id = LDAP_OBJ.search(static_options["people_dn"], ldap.SCOPE_SUBTREE, "cn=%s" % (cn), [key])
        while 1:
            result_type, result_data = LDAP_OBJ.result(result_id, 0)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        if len(result_set) == 0:
            print("User: %s does not exist in ldap." % (username))
            automount = "ERROR user does not exist."
        else:
            for i in range(len(result_set)):
                for entry in result_set[i]:
                    automount = entry[1][key][0]

    except ldap.LDAPError, e:
        automount = "ERROR connecting to ldap."

    return automount

def connect_to_ldap(static_configs):
    #Attmepts to connect to the ldap server
    try:
        l = ldap.initialize(static_configs["ldap_uri"])
    #If connect fails this returns an error message and exits
    except ldap.LDAPError, e:
        print("(!) Error occured while connecting to ldap")
        print(e)
        print("(!) BAILING!")
        sys.exit(1)
    return l

#def get_dns_info(cn):
 #   ip = retrieve_information(cn,"ipHostNumber")
  #  mac = retrieve_information(cn,"macAddress")
   # return ip, mac

if __name__ == "__main__":
    #val = get_dns_info("svn001")
    host = "svn001"

    ip = retrieve_information(cn,"ipHostNumber")                                                                                                                                                                                          
    mac = retrieve_information(cn,"macAddress")  

    print ip
    print mac 

