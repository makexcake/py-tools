import paramiko
import schedule
import monitor
import aws_info
import time

# The program monitors and outputs the statuses of running ec2
# instances, and the appication that runs on them.
# If the app is unreachable the program connects to the instance
# via ssh, restarts the server and relaunching the container
# the app is running on.

def monitor_app(server_ip, url, container_id, mail):

    # request instance statuses list
    instance_status = aws_info.get_instance_status()
    # check if running instances exist
    if len(instance_status) > 0:
        for instance in instance_status:
            print(f"instance id: {instance['id']}, state: {instance['state']}, status: {instance['status']}")


    # check if the app is responding
    health = monitor.monitor_app(url, mail)

    # if webpage is not alive restart server
    if health == False:

        # reboot server
        print('ERROR rebooting server\n')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server_ip, 
                    username='ec2-user', 
                    key_filename='/Users/vitalik/DEVOPS/AWS/MyKeyPair.pem')
        
        ssh.exec_command('sudo reboot')
        ssh.close

        time.sleep(60)

        # start docker container
        ssh.connect(hostname=server_ip, 
                    username='ec2-user', 
                    key_filename='/Users/vitalik/DEVOPS/AWS/MyKeyPair.pem')
        ssh.exec_command('sudo systemctl start docker')
        ssh.exec_command(f'sudo docker start {container_id}')

        time.sleep(120)
    else: 
        print('app status: ok')



def start_monitor(server_ip, url, container_id, mail):
    schedule.every(5).seconds.do(monitor_app, server_ip, url, container_id, mail)
    while True:    
        schedule.run_pending()

start_monitor('3.126.91.188', "http://3.126.91.188:8081/", '340505b70ed8', "v.nudelman@gmail.com")




