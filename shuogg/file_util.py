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


def get_files_fullpath(dir_path, suffix=''):
    """
    获取dir_path目录下所有.xxx文件的路径
    :param suffix: 后缀如".sql" ".java" ; 若不填则不进行文件过滤
    :return: list of str
    """
    files = list(filter(lambda x: os.path.isfile(
        os.path.join(dir_path, x)), os.listdir(dir_path)))
    if suffix != '':
        # 留下后缀为suffix的文件
        files = list(filter(lambda x: x.endswith(suffix), files))
    all_fullpath = list(map(lambda x: os.path.join(dir_path, x), files))
    return all_fullpath


def get_files_fullpath_recur(dir_path, suffix=None):
    """
    获取dir_path目录及其子目录下所有.xxx文件的路径
    :param suffix: 后缀如".sql" ".java" ; 若不填则不进行文件过滤
    :return: str or list or tuple
    """
    if dir_path == '' or dir_path is None:
        return
    if os.path.isfile(dir_path):
        return
    urls = list()
    for maindir, subdir, filename_list in os.walk(dir_path):
        for file in filename_list:
            full_path = os.path.join(maindir, file)
            ext = os.path.splitext(full_path)[1]
            ok = False
            if suffix is None:
                ok = True
            elif isinstance(suffix, str):
                if suffix == ext:
                    ok = True
            elif isinstance(suffix, list) or isinstance(suffix, tuple):
                if suffix is None or ext in suffix:
                    ok = True
            if ok:
                urls.append(full_path)
    return urls


def get_files_fullpath_curdir(suffix=''):
    """
    获取当前目录下所有.xxx文件的路径
    :param suffix: 后缀如".sql" ".java" ; 若不填则不进行文件过滤
    :return: list of str
    """
    return get_files_fullpath(os.getcwd(), suffix)


def get_dirs_fullpath(dir_path):
    """
     获取dir_path目录下所有文件夹的路径
    """
    dirs = list(filter(lambda x: os.path.isdir(
        os.path.join(dir_path, x)), os.listdir(dir_path)))
    all_fullpath = list(map(lambda x: os.path.join(dir_path, x), dirs))
    return all_fullpath

def split_path_file_ext(path):
    """
    :return: (文件名, .扩展名)
    """
    path, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    return path, name, ext

def path_with_tail(path, tail):
    """
    给文件名加后缀
    eg: newPath = path_with_tai('abc.jpg', '_1') # newPath为 'abc_1.jpg'
    """
    p, name, ext = split_path_file_ext(path)
    if p == '':
        os_sep = ''
    else:
        os_sep = os.path.sep
    return p + os_sep + name + tail + ext

if __name__ == '__main__':
    a = """D:\\git_project\\ShuoPyUtils\\shuogg\\des_util.py"""
    print(split_path_file_ext(a))
