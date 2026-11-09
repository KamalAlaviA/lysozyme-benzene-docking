from pymol import cmd
import numpy as np

cmd.load("C:/docking_project/BNZ_crystal.pdb", "BNZ_crystal")
c0 = cmd.get_coords("BNZ_crystal and elem C", 1).mean(0)

for prot in ["L99A", "WT"]:
    for s in range(1, 6):
        name = "%s_s%d" % (prot, s)
        cmd.load("C:/docking_project/%s.pdbqt" % name, name)
        n = cmd.count_states(name)
        d = [np.linalg.norm(cmd.get_coords("%s and elem C" % name, st).mean(0) - c0)
             for st in range(1, n + 1)]
        print(name, " ".join("%.1f" % x for x in d))