# -*- coding: utf-8 -*-
import os
import sys
from nas import Nas
# current_path = os.path.abspath(os.path.dirname(__file__))


def help_info():
    print "console.py nas [upload|ls] {dir}"
    print "console.py oss [upload] {dir}"
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
            if not src_dir.startswith("/"):
                print "source dir must start with /"
                help_info()
            nas.copy_to_nas(src_dir)
        elif cmd == "ls":
            dir = sys.argv[3]
            nas.ls_dir(dir)
        else:
            help_info()
    elif module == "oss":
        pass
    else:
        help_info()
