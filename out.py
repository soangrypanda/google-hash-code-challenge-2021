# THIS MODULE MAKES AN OUTPUT FILE

def make_out_file(info, inp_name):
    print("Entering make_out_file...")

    out_name = inp_name + ".out"
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
