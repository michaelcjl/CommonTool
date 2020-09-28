import os
import re
import sys

src_path = r"/home/chengjialin/04A10_ct_5429_lux_10.9_gain_15.5X_exp_20000_hcg/"

raw_filelist = []

filelist = os.listdir(src_path)
for x in filelist:
    if ".raw" in x:
        raw_filelist.append(x)


raw_filelist.sort(key=lambda x: int(x.split('_')[-1][:-4]))

os.chdir(src_path)

#print(raw_filelist)

print(len(raw_filelist))

total_num = len(raw_filelist)

target_path = r"/home/chengjialin/target_dir/"


#num = 0
for i in range(0,total_num):
    new_filename = 'OS04A10_ct_5429K_lux_10.9_gain_0015.5X_exp_20000_hcg_' + str(i).zfill(3) + ".raw"
    
#    new_filename = target_path +new_filename
    
    os.rename(raw_filelist[i], new_filename)
    #num = num +1




