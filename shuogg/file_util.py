import sys
import os
import codecs
import natsort


def get_file_content(file_path):
    """
    读取文件, 暂时只支持utf8和gbk编码的文件, 自动去除BOM
    :param file_path:
    :return: str
    """
    try:
        with open(file_path, encoding='utf-8') as f1:
            raw = f1.read()
            # 去掉BOM
            bom_head = raw.encode(encoding='utf-8')[:3]
            if bom_head == codecs.BOM_UTF8:
                raw = raw.encode(encoding='utf-8')[3:].decode(encoding='utf-8')
            return raw
    except Exception as e:
        with open(file_path, encoding='GBK') as f2:
            return f2.read()


def write_file_content(file_path, text, encoding='utf8'):
    """
    写文件
    :param file_path: str
    :param text: str
    :param encoding: str
    :return: None
    """
    try:
        with open(file_path, mode='wb') as f1:
            f1.write(text.encode(encoding=encoding))
    except Exception as e:
        print(e)


def write_file_content_append(file_path, text, encoding='utf8'):
    """
    写文件-append模式
    :param file_path: str
    :param text: str
    :param encoding: str
    :return: None
    """
    try:
        with open(file_path, mode='ab') as f1:
            f1.write(text.encode(encoding=encoding))
    except Exception as e:
        print(e)


def quick_mkdir(name):
    """
    当前目录下建一个文件夹
    :param name: 文件夹名称
    :return: 新建的文件夹的完整路径
    """
    new_directory = os.getcwd() + '\\' + name + "\\"
    if not os.path.exists(new_directory):
        try:
            os.mkdir(os.getcwd() + '\\' + name)
        except Exception as e:
            print(e)
    return new_directory



if __name__ == '__main__':
    pass