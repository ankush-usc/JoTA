import paramiko
import subprocess
import time

print "Phase 2 mapper"
ssh = paramiko.SSHClient()


ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('ec2-52-32-237-39.us-west-2.compute.amazonaws.com', username='hadoop', password='', key_filename='/Users/meerapatil/JoTA/firstscraper/EE542_Oregon_keyPair.pem')

cmd_to_execute = "/home/hadoop/bin/hadoop jar /home/hadoop/contrib/streaming/hadoop-streaming.jar -files s3://jotabucket/mapperreducers/mapper_skill2.py,s3://jotabucket/mapperreducers/reducer_skill.py -mapper mapper_skill2.py -reducer reducer_skill.py -input s3://jotabucket/input2/ -output s3://jotabucket/output1/";

stdin, stdout, stderr = ssh.exec_command('aws s3 rm --recursive s3://jotabucket/output1')

stdin, stdout, stderr = ssh.exec_command(cmd_to_execute)

print stdout.readlines()
stdin,stdout,stderr = ssh.exec_command('aws s3 ls s3://jotabucket/output1')

check_for_sleep =  stdout.readlines()
print check_for_sleep

while "output1" not in str(check_for_sleep):
	print check_for_sleep
	time.sleep(20)

print "Mapper and reducer completed\n";

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


print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem gen_input_for_2phase.py hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:", shell=True, stdout=subprocess.PIPE).stdout.read()


stdin,stdout,stderr = ssh.exec_command('python gen_input_for_2phase.py output_folder2')

print stdout.readlines();

print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./output_folder2 .", shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./input2skill.txt .", shell=True, stdout=subprocess.PIPE).stdout.read()



ssh.close()
