import os


if not os.path.exists("details.txt"):
    quit("details.txt file not found!")

lines = open("details.txt").read().splitlines()

with open("tokens.txt", "w") as f:
    f.write(f"\n".join([line.split(":")[-1].strip() for line in lines]))
