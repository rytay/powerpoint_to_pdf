import os
import subprocess

files = [f for f in os.listdir('.') if ".ppt" in f or ".pptx" in f]

delete = input('Delete powerpoint files?(y to delete): ')

remove = False

if delete is 'y':
    remove = True

i = 0
for f in files:
    raw_proc = "unoconv -f pdf " + f
    proc = raw_proc.split()
    subprocess.run(proc)
    if remove:
        print('Converting : ' + f + ' to pdf')
        os.remove(f)

print('Done. Converted '+ str(i) + ' documents.')
exit()

