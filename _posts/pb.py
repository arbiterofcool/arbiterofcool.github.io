from sys import argv
import subprocess as sp

script, msg = argv

print(msg)
sp.call(['git','add','.'])
sp.call(['git','commit','-m', msg])
sp.call(['git','push'])
