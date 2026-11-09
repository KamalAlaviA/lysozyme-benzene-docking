from pymol import cmd

cmd.load("C:/docking_project/L99A_clean.pdb", "mut")
cmd.load("C:/docking_project/WT_clean.pdb", "wt")

def seq(obj):
    fasta = cmd.get_fastastr(obj)
    return "".join(l for l in fasta.splitlines() if not l.startswith(">"))

a, b = seq("mut"), seq("wt")
print("lengths:", len(a), len(b))
for i, (x, y) in enumerate(zip(a, b), 1):
    if x != y:
        print("position", i, ": wild-type", y, "-> L99A file", x)