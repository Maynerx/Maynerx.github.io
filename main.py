import argparse
import time

class Args:
    def __init__(self):
        parser = argparse.ArgumentParser(description='A test program.')
        parser.add_argument("g", help="Prints the supplied argument.")
        self.args = parser.parse_args()

    def Run(self):
        if self.args._get_kwargs()[0][0] == "g":
            with open("a.txt", "w+") as f:
                f.write("True")

Args().Run()