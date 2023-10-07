import os


def get_path_dirs_files(path):
    """
    获得路径下所有路径及文件

    :param path: 路径
    :return: 返回一个列表, 列表中第一个元素为路径列表, 列表中第二个元素为文件列表
    """

    for root, dirs, files in os.walk(path):
        return [dirs, files]
