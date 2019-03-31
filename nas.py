# -*- coding: utf-8 -*-
import os
import sys
import paramiko
from termcolor import colored

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lib/")
from config import get_config


class Nas(object):

    def __init__(self):
        self.ip = get_config("nas")["host"]
        self.base_dir = get_config("nas")["base_dir"]
        self.user = get_config("nas")["user"]
        self.passwd = get_config("nas")["passwd"]

    def copy_to_nas(self, dir):
        dir_name_arr = dir.split("/")
        dir_name = dir_name_arr[-1]
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.ip, 22, self.user, self.passwd)
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp = ssh.open_sftp()
        remote_base_dir = self.base_dir + dir_name
        try:
            list_dir = sftp.listdir(remote_base_dir)
            print colored("%s files exist in dir: %s" % (len(list_dir), remote_base_dir), 'green')
        except:
            print colored("dir:%s not exist, create it" % remote_base_dir, 'yellow')
            sftp.mkdir(remote_base_dir, mode=511)
        i = 0
        for root, dirs, files in os.walk(dir):
            for name in files:
                file_dir = os.path.join(root, name)
                remote_file = self.base_dir + dir_name + "/" + name
                sftp.put(file_dir, remote_file)
                sftp.chown(remote_file, 1001, 1000)
                sftp.chmod(remote_file, 416)   # 640
                i += 1
                print colored("copy file:%s to nas done" % name, 'blue')
        print colored("%s files transport done!" % i, 'green')

    def ls_dir(self, dir):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.ip, 22, self.user, self.passwd)
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp = ssh.open_sftp()
        list_dir = sftp.listdir(self.base_dir)
        for dir in list_dir:
            print colored(dir, 'green')
