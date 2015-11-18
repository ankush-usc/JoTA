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
    cmd_to_execute = "/home/hadoop/bin/hadoop jar /home/hadoop/contrib/streaming/hadoop-streaming.jar -files s3://jotabucket/mapperreducers/ahp_word_mapper.py,s3://jotabucket/mapperreducers/ahp_word_reducer.py -mapper ahp_word_mapper.py -reducer ahp_word_reducer.py -input s3://jotabucket/input/ -output s3://jotabucket/output35/";
    stdin, stdout, stderr = ssh.exec_command('aws s3 rm --recursive s3://jotabucket/output35')

    stdin, stdout, stderr = ssh.exec_command(cmd_to_execute)

    print stdout.readlines()
    stdin,stdout,stderr = ssh.exec_command('aws s3 ls s3://jotabucket/output35')

    check_for_sleep =  stdout.readlines()

    while "output35" not in str(check_for_sleep):
        time.sleep(20)
    stdin,stdout,stderr = ssh.exec_command('aws s3 cp --recursive s3://jotabucket/output35/ output_folder/')
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
    #to be decided
    cmdphase2 = "python connect_to_EMR_phase2.py"
    os.system(cmdphase2)

    merge2_cmd = "python merge.py output_folder2 skill"
    os.system(merge2_cmd)
    return


@app.route("/skills", methods=['GET','POST'])
def doskills():
    cmdphase2 = "python EMR_connection_inside.py"
    os.system(cmdphase2)

    merge2_cmd = "python merge.py output_folder2 skill"
    os.system(merge2_cmd)
    return


@app.route("/bestmatch", methods=['GET','POST'])
def matchbest():
    arg1 = str(request.form['arg1'])
    arg2 = str(request.form['arg2'])
    arg3 = str(request.form['arg3'])
    arg4 = str(request.form['arg4'])
    cmdmatch="php joblister.php" + arg1 + arg2 + arg3 + arg4
    os.system(cmdmatch)
    return

if __name__ == "__main__":
    app.run()



