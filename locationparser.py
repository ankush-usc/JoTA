__author__ = 'meerapatil'
file=open('myInput.txt','r')

for line in file:
    job = line.split('::')
    company = job[1]
    skills = job[2]
    days = job[3]
    link = job[4]



