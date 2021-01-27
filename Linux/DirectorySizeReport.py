import os
start_path = '.'  # To get size of current directory
for child_path in os.listdir(start_path):
    if os.path.isdir(child_path):
        total_size = 0
        for path, dirs, files in os.walk(child_path):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp)
        print ('{:,.0f}\t'.format(total_size/float(1<<20))+" MB"), 
        print ('{:,.0f}\t'.format(total_size/float(1<<30))+" GB"), child_path # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
