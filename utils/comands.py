from utils.comand.ls import Listing
from utils.comand.pwd import Pwd


class Commands:

    def __init__(self):
        self.listing = Listing()
        self.pwd = Pwd()
        self.help = Commands.Help()

        self.commands = {
            "pwd": self.pwd,
            "help": self.help.helped,
            "exit": "rien",
            "ls": self.listing.listing,
        }

    def execute(self, command):
        if command[0] in self.commands:
            self.commands[command[0]](command)
        else:
            print("error: " + command + ": commande inconnue")

    class Help:

        def __init__(self):
            self.commands = Commands

        @staticmethod
        def helped(self, args):
            print("Commandes disponibles: ")
            for commands in self.commands.commands:
                print(commands)