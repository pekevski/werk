 #!/usr/bin/python
import subprocess


# open code
CODE = ['code']

# open slack
SLACK = ['open', '-ga', 'slack']

# open chrome
CHROME = ['open', '-ga', 'Google Chrome']

# open JIRA
JIRA = ['open', '-ga', 'jira']

# open source tree
VC = ['open', '-ga', 'SourceTree']

APPS = [SLACK, JIRA, VC, CHROME, CODE]


for app in APPS:
    run_apps = subprocess.run(app)
    print("The exit code was: %d" % run_apps.returncode)

