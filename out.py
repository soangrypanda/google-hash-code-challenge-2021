# THIS MODULE MAKES AN OUTPUT DIR (IF NECESSARY) AND OUTPUT FILES

from pathlib import Path
from os import mkdir, listdir
from os.path import isfile, join


def give_out_name(inp_name):
    out_name = inp_name

    if out_name[len(out_name) - 3:] == ".in":
        out_name = out_name[:len(out_name) - 3] + ".out"
    else:
        out_name = out_name + ".out"

    return out_name


def make_out_file(info, inp_name, out_path):
    print("Entering make_out_file...")

    out_name = out_path / give_out_name(inp_name)

    f = open(out_name, "w")
    f.write(str(info["deliveries"])+"\n")

    deliveries = info["piz_to_team"]
    for team, pizzas in deliveries:
        line = ""
        line += str(team) + " "
        line += " ".join([str(item) for item in pizzas])
        f.write(line+"\n")

    print(f"File {out_name} created!")
    return


def handle_out_dir(dir_path):
    new_path = dir_path / "out"

    if not new_path.is_dir():
        print("No out directory! Creating...")
        mkdir(str(new_path))

    return new_path


def give_inp_files(dir_path):
    inp_path = dir_path / "inp"

    if not inp_path.is_dir():
        print("No folder with input files! Aborting program...")
        exit(1)

    inp_files = [f for f in listdir(inp_path) if isfile(join(inp_path, f))]
    return inp_files, inp_path
