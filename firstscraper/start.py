import os
import time
import paramiko
import subprocess
from flask import Flask, request
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET','POST'])
def whats():
    try:
        os.getcwd()
        cmd = "scrapy crawl indeed"
        """cmd = "sudo scrapy crawl whats" """
        os.system(cmd)

    except:
        pass

    print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem /Users/meerapatil/jobscloud.txt hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./", shell=True, stdout=subprocess.PIPE).stdout.read()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ec2-52-32-237-39.us-west-2.compute.amazonaws.com', username='hadoop', password='', key_filename='EE542_Oregon_keyPair.pem')
    stdin,stdout,stderr = ssh.exec_command('aws s3 cp jobscloud.txt s3://jotabucket/input/')
    print stdout.readlines()

    """ integrate"""
    cmd_to_execute = "/home/hadoop/bin/hadoop jar /home/hadoop/contrib/streaming/hadoop-streaming.jar -files s3://jotabucket/mapperreducers/ahp_word_mapper.py,s3://jotabucket/mapperreducers/ahp_word_reducer.py -mapper ahp_word_mapper.py -reducer ahp_word_reducer.py -input s3://jotabucket/input/ -output s3://jotabucket/output/";
    stdin, stdout, stderr = ssh.exec_command('aws s3 rm --recursive s3://jotabucket/output')

    stdin, stdout, stderr = ssh.exec_command(cmd_to_execute)

    print stdout.readlines()
    stdin,stdout,stderr = ssh.exec_command('aws s3 ls s3://jotabucket/output')

    check_for_sleep =  stdout.readlines()

    while "output" not in str(check_for_sleep):
	    time.sleep(20)


    stdin,stdout,stderr = ssh.exec_command('aws s3 cp --recursive s3://jotabucket/output/ output_folder/')

    stdin,stdout,stderr = ssh.exec_command('ls')
    check_for_sleep =  stdout.readlines()
    print check_for_sleep

    while "output_folder" not in str(check_for_sleep):
        print check_for_sleep
        time.sleep(20)
        stdin,stdout,stderr = ssh.exec_command('ls')
        check_for_sleep =  stdout.readlines()

    print subprocess.Popen("scp -r -i EE542_Oregon_keyPair.pem hadoop@ec2-52-32-237-39.us-west-2.compute.amazonaws.com:./output_folder/ .", shell=True, stdout=subprocess.PIPE).stdout.read()

    merge_cmd = "python merge.py output_folder location"
    os.system(merge_cmd)
    ssh.close()
    return

@app.route("/skills", methods=['GET','POST'])

def doskills():

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

if __name__ == "__main__":
    app.run()



