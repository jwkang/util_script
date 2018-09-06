import os
import re
import sys

def isExistModelDir(dir_list):
    bFound = ""
    regex = r'model_D+.+'
    p = re.compile(regex)
    
    for each_dir in dir_list:
        if p.match(each_dir) is not None:
            bFound = p.match(each_dir).string
            break
        
    return bFound

for each_dir in os.listdir("./"):
    if os.path.isdir(each_dir) == False:
        continue
    target = isExistModelDir(os.listdir(each_dir))
    if len(target):
        try:
                with open(each_dir+"/make/.config") as f:
                    for each_line in f.readlines():
                        if "CONFIG_MAIN_TARGET_NAME" in each_line:
                            print(each_dir+" : "+each_line.split('"')[1])

        except:
            print(each_dir + " has unkown error " + str(sys.exc_info()[0]))

