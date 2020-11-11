def hdfs_site(node,location):
    os.system("cp /arth-task/task7.1/dn/temp.xml /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<configuration\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<property\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<name\>dfs.{}.dir\</name\> >> /arth-task/task7.1/dn/hdfs-site.xml".format(node))
    folder=input("Enter the {}node directory to be created and configure: ".format(node))
    if location==1:
        os.system("mkdir {}".format(folder))
    elif location==2:
        os.system("ssh {} mkdir {}".format(ip,folder))
    os.system("echo \<value\>{}\</value\> >> /arth-task/task7.1/dn/hdfs-site.xml".format(folder))
    os.system("echo \</property\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \</configuration\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    if location==1:
        os.system("mv -f /arth-task/task7.1/dn/hdfs-site.xml /etc/hadoop/hdfs-site.xml")
    elif location==2:
        os.system("scp /arth-task/task7.1/dn/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
        os.system("rm -f /arth-task/task7.1/dn/hdfs-site.xml")
