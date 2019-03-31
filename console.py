# -*- coding: utf-8 -*-
import sys
from nas import Nas


def help_info():
    print "console.py nas [upload|ls] {dir}"
    exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_info()
    module = sys.argv[1]
    if module == "nas":
        if len(sys.argv) < 4:
            help_info()
        cmd = sys.argv[2]
        nas = Nas()
        if cmd == "upload":
            src_dir = sys.argv[3]
            nas.copy_to_nas(src_dir)
        elif cmd == "ls":
            dir = sys.argv[3]
            nas.ls_dir(dir)
        else:
            help_info()
    else:
        help_info()
