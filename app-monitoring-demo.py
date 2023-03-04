import paramiko
import monitor
import aws_info
import time

# check ec2 server status
#health = monitor.monitor_app("http://3.120.248.228:8080/", "v.nudelman@gmail.com")
health = False

# if webpage is not alive restart server
if health == False:
    
    # reboot server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='3.120.248.228', 
                username='ec2-user', 
                key_filename='/Users/vitalik/DEVOPS/AWS/MyKeyPair.pem')
    
    ssh.exec_command('sudo reboot')
    ssh.close

    time.sleep(60)

    # start docker container
    ssh.connect(hostname='3.120.248.228', 
                username='ec2-user', 
                key_filename='/Users/vitalik/DEVOPS/AWS/MyKeyPair.pem')
    ssh.exec_command('sudo systemctl start docker')
    ssh.exec_command('sudo docker start d3098c566b1b')

    time.sleep(120)
    




