import jenkins

server = jenkins.Jenkins('http://52.86.233.190:8080', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()

server.build_job('Hackathon.Pipeline', {'token': 'HackathonToken', 'branchName': 'master'})

print('Hello %s from Jenkins %s' % (user['fullName'], version))