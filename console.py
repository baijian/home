# -*- coding: utf-8 -*-
import sys
from nas import Nas


def help_info():
    print "console.py sync-to-nas [src_dir]"

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "copy-to-nas":
        src_dir = sys.argv[2]
        nas = Nas()
        nas.copy_to_nas(src_dir)
