#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
To delete pictures which existed more than some days under folder /ftp/Captured. Default value is 300 days.

Usage: python disk_cleaner.py [number_of_days] OR ./disk_cleaner.py [number_of_days]
"""

import sys
import os
import datetime


FILE_DIR = '/ftp/Captured/'  # folder to be cleaned up
DEFAULT_DAYS = 300  # default days


def remove_file(file_name):
    if os.path.exists(file_name):
        print('Remove file: %s' % file_name)
        os.remove(file_name)
    else:
        print('%s is already deleted.' % file_name)

def is_out_of_date(file_name, number_of_days):
    date = datetime.datetime.fromtimestamp(os.path.getmtime(file_name))
    now = datetime.datetime.now()
    if (now - date).days >= number_of_days:
        return True
    else:
        return False

def run(number_of_days):
    print('Clean files [.png | .jpg] that before %d days under %s' % (number_of_days, FILE_DIR))
    for root, dirs, files in os.walk(FILE_DIR):
        for name in files:
            if name.endswith('.png') or name.endswith('.jpg'):
                file_name = os.path.join(root, name)
                if is_out_of_date(file_name, number_of_days):
                    remove_file(file_name)
                # else:
                #     print('Skip %s' % file_name)
    print('Clean complete.')

def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print('Wrong parameter, exit!')
        print('Usage: python disk_cleaner.py [number_of_days] OR ./disk_cleaner.py [number_of_days]')
        return

    number_of_days = DEFAULT_DAYS

    if len(sys.argv) == 2:
        if not sys.argv[1].isdigit():
            print('Wrong number of days, exit!')
            return
        else:
            number_of_days = int(sys.argv[1])

    run(number_of_days)


if __name__ == '__main__':

    pipeline = os.popen("/bin/df -h | grep 'ip(10.)' | awk '{print $4}' ")
    current_free_disk = pipeline.read()
    #print(type(current_free_disk))
    print("report to the master, currently the free disk is:", current_free_disk)


    l = len(current_free_disk)
 #   print(current_free_disk[l-2])
 #   print(current_free_disk[:l-2])
 #   print(int(current_free_disk[:l-2]))


    if(current_free_disk[l-2] == 'T'):
        print('today the free disk is:', current_free_disk, 'no need to do the clean Job!')
        pass
    elif((current_free_disk[l-2] == 'G') and (int(current_free_disk[:l-2]) > 700)):
        print('today the free disk is less than 1T, strat to do the clean Job!')
        print('Start at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))

        DEFAULT_DAYS -= 50
        main()
 
        print('End at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))  

    elif((current_free_disk[l-2] == 'G') and (500 <= int(current_free_disk[:l-2]) <= 700)):
        print('today the free disk is less than 700G, strat to do the clean Job!')
        print('Start at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))

        DEFAULT_DAYS -= 100
        main()
 
        print('End at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')) 


    elif((current_free_disk[l-2] == 'G') and (int(current_free_disk[:l-2]) < 500)):
        print('today the free disk is less than 500G, strat to do the clean Job!')
        print('Start at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))

        DEFAULT_DAYS -= 150
        main()
 
        print('End at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))


#    #print('Start at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
#    #main()
#    #print('End at: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
