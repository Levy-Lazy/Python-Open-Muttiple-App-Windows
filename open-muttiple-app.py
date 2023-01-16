import subprocess

# List of the applications to open with their path
applications = [
    'D:\Program Files\OperaGX\opera.exe',
    'D:\Program Files\VirtualBox\Virtualbox.exe',
]

# Open each application
for app in applications:
    subprocess.Popen(app)
