# -*- coding: utf-8 -*-
import os
import sys
import oss2
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../common/")
from config import get_config


class OssUtil(object):

    def __init__(self):
        self.access_id = get_config("oss")["access_id"]
        self.access_key = get_config("oss")["access_key"]
        self.endpoint = get_config("oss")["endpoint"]
        self.namespace = get_config("oss")["namespace"]
        auth = oss2.Auth(self.access_id, self.access_key)
        self.bucket = oss2.Bucket(auth, self.endpoint, self.namespace)

    def upload_to_oss(self, file_path):
        """
        上传文件
        :param file_path:
        :return:
        """
        file_list = file_path.split("/")
        obj_name = ""
        mutex = False
        for dir_name in file_list:
            if mutex:
                obj_name += dir_name + "/"
            if dir_name == self.namespace:
                mutex = True
        obj_name = obj_name[0:-1]
        if not self.bucket.object_exists(obj_name):
            self.bucket.put_object_from_file(obj_name, file_path)
            print file_path + " upload to oss success!"
        else:
            print file_path + " exist in the oss, skip to upload!"

    def upload(self, dir):
        pass


if __name__ == "__main__":
    o = OssUtil()
    o.upload_to_oss("/xxxx/bj-zly/yyyy/abc/test.txt")
