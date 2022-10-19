import sys
import subprocess
from scour.scour import scourString

with open(sys.argv[1]) as fin:
    with open('s.svg', 'w') as fout:
        fout.write(scourString(fin.read()))

subprocess.check_call(['rsvg-convert', '-o', 'orig.png', sys.argv[1]])
subprocess.check_call(['rsvg-convert', '-o', 'new.png', 's.svg'])
with open('orig.png', 'rb') as forig:
    with open('new.png', 'rb') as fnew:
        assert forig.read() == fnew.read(), 'original and reduced files differ'
