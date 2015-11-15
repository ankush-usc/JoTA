
import paramiko
import subprocess
import time

ssh = paramiko.SSHClient()


ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('ec2-52-32-237-39.us-west-2.compute.amazonaws.com', username='hadoop', password='', key_filename='/Users/ankushhprasad/Documents/JOTA/EE542_Oregon_keyPair.pem')

cmd_to_execute = "/home/hadoop/bin/hadoop jar /home/hadoop/contrib/streaming/hadoop-streaming.jar -files s3://jotabucket/mapperreducers/mapper_skill.py,s3://jotabucket/mapperreducers/reducer_skill.py -mapper mapper_skill.py -reducer reducer_skill.py -input s3://jotabucket/input1/ -output s3://jotabucket/output1/";

stdin, stdout, stderr = ssh.exec_command('aws s3 rm --recursive s3://jotabucket/output1')

stdin, stdout, stderr = ssh.exec_command(cmd_to_execute)

print stdout.readlines()
stdin,stdout,stderr = ssh.exec_command('aws s3 ls s3://jotabucket/output1')

check_for_sleep =  stdout.readlines()
print check_for_sleep

while "output1" not in str(check_for_sleep):
	print check_for_sleep
	time.sleep(20)
	
stdin, stdout, stderr = ssh.exec_command('rm -r output_folder2')
stdin,stdout,stderr = ssh.exec_command('aws s3 cp --recursive s3://jotabucket/output1/ output_folder2/')
stdin,stdout,stderr = ssh.exec_command('ls')
check_for_sleep =  stdout.readlines()
print check_for_sleep

while "output_folder2" not in str(check_for_sleep):
        print check_for_sleep
        time.sleep(20)
	stdin,stdout,stderr = ssh.exec_command('ls')
	check_for_sleep =  stdout.readlines()


print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./output_folder2/ .", shell=True, stdout=subprocess.PIPE).stdout.read()

#subprocess.Popen("python merge.py /Users/ankushhprasad/Documents/JOTA/JoTA/output_folder location")

#call(["scp","-i EE542_Oregon_keyPair.pem","hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:/output_folder/"])
ssh.close()
