from utils.colors import Colors
from . import os, argparse


class Listing:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            add_help=False,
            exit_on_error=False,
            prog='ls',
            description="List directory content",
            epilog="Programme réécrit par felis78")
        self.parser.add_argument('-a', '--all', action='store_true', help="Affiche tout le contenu d'un dossier")
        self.parser.add_argument('-h', '--help', action='store_true', help="Affiche l'aide")
        self.parser.add_argument('-A', '--almost_all', action='store_true', help=' omettre les fichiers "." et ".."')
        self.parser.add_argument('--author', action='store_true', help="afficher l'auteur des fichiers")

    def listing(self, args):
        check = 0
        arg = self.parser.parse_args(args[1:])
        options = {
            arg.help: self.parser.print_help,
            arg.all: self.all,
            arg.almost_all: self.almost_all,
            arg.author: self.author
            }
        try:
            for i in options:
                if i is True:
                    options[i]()
                    check += 1

            if check == 0:
                self.default()

        except SystemExit as exc:
            if exc.code == 2:
                print(exc)
            else:
                print(f'Argument non reconnu, veuillez vérifier vos arguments: {args}')

    @staticmethod
    def author():
        for content in os.listdir(os.getcwd()):
            if os.path.isfile(content):
                print(type(os.stat(content)))
        return 0

    @staticmethod
    def all():
        for content in os.listdir(os.getcwd()):
            if os.path.isdir(content):
                print(Colors.Fg.blue + content + Colors.reset)
            if os.path.isfile(content):
                print(Colors.Fg.yellow + content + Colors.reset)
        return 0

    @staticmethod
    def almost_all():
        for content in os.listdir(os.getcwd()):
            if os.path.isdir(content):
                print(Colors.Fg.blue + content + Colors.reset)
            if os.path.isfile(content) and not content.startswith('.'):
                print(Colors.Fg.yellow + content + Colors.reset)
        return 0

    @staticmethod
    def default():
        for content in os.listdir(os.getcwd()):
            if os.path.isdir(content) and not content.startswith('.'):
                print(Colors.Fg.blue + content + Colors.reset)
            if os.path.isfile(content):
                print(Colors.Fg.yellow + content + Colors.reset)
        return 0
