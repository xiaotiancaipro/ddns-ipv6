import os


def get_path_dirs_files(path):
    """
    获得路径下所有路径及文件

    :param path: 路径
    :return: 返回一个列表, 列表中第一个元素为路径列表, 列表中第二个元素为文件列表
    """

    for root, dirs, files in os.walk(path):
        return [dirs, files]


def get_project_abspath():
    """获得当前项目的绝对路径"""
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    return "/".join(current_file_path.split("/")[:-1])
