from . import os


class Pwd:
    @staticmethod
    def pwd(args):
        print(os.getcwd())
