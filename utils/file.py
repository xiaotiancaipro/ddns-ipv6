import os


def textfile_create(path, text):
    """
    新建文本文件并写入内容或在已存在的文本文件中追加新内容

    :param path: 文件位置
    :param text: 写入的文本
    """

    with open(file=path, mode="a+", encoding="utf-8") as file:
        file.write(str(text))
        file.close()


def get_text_last_line(textfile):
    """
    获取文本文件最后一行内容

    :param textfile: 文本文件路径
    :return: 该文本文件最后一行内容, 返回类型为bytes
    """

    file_size = os.path.getsize(textfile)
    block_size = 1024

    with open(textfile, "rb") as dat_file:
        if file_size > block_size:
            max_seek_point = (file_size // block_size)
            dat_file.seek((max_seek_point - 1) * block_size)
        elif file_size:
            dat_file.seek(0, 0)
        lines = dat_file.readlines()
        last_line = lines[-1].strip() if lines else ""
        dat_file.close()

    return last_line
