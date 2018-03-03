# -*- coding: utf-8 -*-
import os
import sys
import getopt
import hashlib

class FileCheck(object):
    
    def __init__(self, src, dst):
        self.src_dir = src
        self.dst_dir = dst

    def get_src_file(self):
        src_file_map = {}
        for f in os.listdir(self.src_dir):
            if f.startswith("."):
                continue
            src_file_map[f] = self.src_dir + "/" + f
        return src_file_map

    def get_dst_file(self):
        dst_file_map = {}
        for f in os.listdir(self.dst_dir):
            if f.startswith("."):
                continue
            dst_file_map[f] = self.dst_dir + "/" + f
        return dst_file_map

    def get_file_md5(self, filename):
        myhash = hashlib.md5()
        f = file(filename, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()

    def check_dst_contains_src_files(self):
        src_file_map = self.get_src_file()
        dst_file_map = self.get_dst_file()
        print "dst file count: %s" % str(len(dst_file_map))
        print "src file count: %s" % str(len(src_file_map))
        for f in dst_file_map.keys():
            dst_md5 = self.get_file_md5(dst_file_map[f])
            if not f in src_file_map.keys():
                print "file:%s not in src" % f
                continue
            src_md5 = self.get_file_md5(src_file_map[f])
            if dst_md5 == src_md5:
                print "file:%s in dst equals src, md5sum:%s" % (f, dst_md5)
            else:
                print "file:%s in dst different with src, dst_md5sum: %s, src_md5sum: %s" % (f, dst_md5, src_md5)

def usage():
    print "-src [] -dst []"
    exit()

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hs:d:")
    if len(opts) == 0:
        usage()
        sys.exit()
    src_dir = ""
    dst_dir = ""
    for op, value in opts:
        if op == "-s":
            src_dir = value
            if not os.path.exists(src_dir):
                print "%s not exist" % src_dir
                exit(1)
        elif op == "-d":
            dst_dir = value
            if not os.path.exists(dst_dir):
                print "%s not exist" % dst_dir
                exit(1)
        elif op == "-h":
            usage()
            sys.exit(0)
    file_checker = FileCheck(src_dir, dst_dir)
    file_checker.check_dst_contains_src_files()
