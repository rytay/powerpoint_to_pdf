import os
import subprocess

files = [f for f in os.listdir('.') if ".ppt" in f or ".pptx" in f]

delete = input('Delete powerpoint files after conversion? (y to delete): ')

remove = False

if delete is 'y':
    remove = True
    print('Will delete files after conversion...')


for f in files:
    raw_proc = "unoconv -f pdf " + f
    proc = raw_proc.split()
    print('Converting : ' + f + ' to pdf.')
    subprocess.run(proc)
    if remove:
        print('Deleting : ' + f + '...')
        os.remove(f)
        
print('Done. Converted '+ len(files) + ' documents.')
exit()

