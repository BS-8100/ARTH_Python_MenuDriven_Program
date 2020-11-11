def namenode(location):
    if location==1:
        #Configure and start namenode in local host
        os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
        os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
        hdfs_site("name",location)
        core_site("name",location)
        os.system('hadoop namenode -format')
        os.system('hadoop-daemon.sh start namenode')
        os.system('jps')
    elif location==2:
        #Configure and start namenode in remote host
        os.system('scp /root/jdk-8u171-linux-x64.rpm /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/'.format(ip))
        os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(ip))
        os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(ip))
        hdfs_site("name",location)
        core_site("name",location)
        os.system('ssh {} hadoop namenode -format'.format(ip))
        os.system('ssh {} hadoop-daemon.sh start namenode'.format(ip))
        os.system('ssh {} jps'.format(ip))
