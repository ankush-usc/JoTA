import paramiko
import subprocess

ssh = paramiko.SSHClient()


ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('ec2-52-32-237-39.us-west-2.compute.amazonaws.com', username='hadoop', password='', key_filename='/Users/ankushhprasad/Documents/JOTA/EE542_Oregon_keyPair.pem')

cmd_to_execute = "/home/hadoop/bin/hadoop jar /home/hadoop/contrib/streaming/hadoop-streaming.jar -files s3://jotabucket/mapperreducers/ahp_word_mapper.py,s3://jotabucket/mapperreducers/ahp_word_reducer.py -mapper ahp_word_mapper.py -reducer ahp_word_reducer.py -input s3://jotabucket/input/ -output s3://jotabucket/output/";


#stdin, stdout, stderr = ssh.exec_command(cmd_to_execute)

#print stdout.readlines()
stdin,stdout,stderr = ssh.exec_command('aws s3 cp --recursive s3://jotabucket/output/ output_folder/')
print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./output_folder/ .", shell=True, stdout=subprocess.PIPE).stdout.read()


#call(["scp","-i EE542_Oregon_keyPair.pem","hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:/output_folder/"])
ssh.close()
