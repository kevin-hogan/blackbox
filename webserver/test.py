import pexpect
import os

os.chdir("/src/reconfig/stack")

child = pexpect.spawn('bus -v demo')
child.expect("Enter a command:")
child.sendline("u")
child.expect("Enter an integer:")
child.sendline("1")

child.expect(r'Pushed (\d)')
print(child.match.group(1))
