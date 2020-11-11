def core_site(node,location):
    os.system("cp /arth-task/task7.1/dn/temp.xml /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<configuration\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<property\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<name\>fs.default.name\</name\> >> /arth-task/task7.1/dn/core-site.xml")
    nnip=input("Enter the ip of the namenode: ")
    port=input("Enter the port number of hadoop cluster: ")
    os.system("echo \<value\>hdfs://{}:{}\</value\> >> /arth-task/task7.1/dn/core-site.xml".format(nnip,port))
    os.system("echo \</property\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \</configuration\> >> /arth-task/task7.1/dn/core-site.xml")
    if location==1:
        os.system("mv -f /arth-task/task7.1/dn/core-site.xml /etc/hadoop/core-site.xml")
    elif location==2:
        os.system("scp /arth-task/task7.1/dn/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
        os.system("rm -f /arth-task/task7.1/dn/core-site.xml")
