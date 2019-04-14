# -*- coding: utf-8 -*-
import os
import yaml


def get_config(key):
    home_dir = os.environ["HOME"]
    cfg_file = home_dir + "/.home.cfg"
    f = open(cfg_file)
    c = yaml.load(f)
    f.close()
    return c[key]

if __name__ == "__main__":
    print get_config("nas")
