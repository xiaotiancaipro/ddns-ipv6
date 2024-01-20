import os


class PathUtil(object):

    @classmethod
    def get_absolute_path(cls):
        """Get absolute path for api part"""
        return os.path.dirname(os.getcwd())
