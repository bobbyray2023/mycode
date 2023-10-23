#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## create a list already containing IP addresses (strings)
    iplist = ['10.0.0.1', '10.0.1.1', '10.3.2.1']

    ## create a list of ports (strings)
    iplist2 = ['5060', '80', '22']

    ## display list
    print(iplist)

    ## Use the append method on iplist, our list object
    ## append takes whatever it is passed and adds it to the list object (iplist)
    ## this will create a list within a list
    iplist.append(iplist2)

    ## show how iplist has changed
    print(iplist)

    ## just like extend, append expects exactly one item to be passed.
    ## If you'd like, uncomment the code below and see the error caused
    # iplist.append('aa:bb:cc:dd:ee:ff', '00:11:22:33:44:55')

if __name__ == "__main__":
    main()
python3 ~/mycode/listrev04.pyvim ~/mycode/listrev05.pvim ~/mycode/listrev05.py#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## a list of Alta3 classes
    alta3classes = ['python_basics', 'python_api_design', 'python_for_networking', 'kubernetes', \
      'sip', 'ims', '5g', '4g', 'avaya', 'ansible', 'python_and_ansible_for_network_automation']

    ## display the list
    print(alta3classes)

    ## how long is the list? use the built in len function
    ## THEN print (display) the results
    print(len(alta3classes))

    # display python_basics
    print(alta3classes[0])

    # display SIP
    print(alta3classes[4])

    # display Ansible
    print(alta3classes[9])

    ##Uncomment to see a list index out of range error
    #print(alta3classes[99])

    print(alta3classes[0:3])

    print(alta3classes[2:5])

    print(alta3classes[-1])

if __name__ == "__main__":
    main()
t add*
git add *
git commit -m "learning about lists"
git push origin
mkdir ~/mycode/
cd ~/mycode/
vim ~/mycode/dictrev01.py
#!/usr/bin/python3
"""Learning about Dictionaries | Alta3 Research"""

def main():
    """runtime code"""
    hostipdict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    ## Display the current state of our dictionary
    print(hostipdict)

    ## add another entry to the dict
    hostipdict['host04'] = '10.23.43.224'

    ## display the dict with the new entry for host4
    print(hostipdict)

    ## rewrite the value for host02
    hostipdict['host02'] = '192.168.70.55'

    ## display the dict with the new entry applied
    print(hostipdict)

    ## recall from the dict
    ## 'host02' should now point to '192.168.70.55'
    print(hostipdict['host02'])

    ## This will cause a key error
    ## toast01 is not a key
    ##print(hostipdict['toast01'])

if __name__ == "__main__":
Main()
:wq
python3 ~/mycode/dictrev01.py

