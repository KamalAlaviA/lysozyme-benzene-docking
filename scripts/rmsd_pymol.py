from pymol import cmd
import itertools
import numpy as np

ref = cmd.get_coords("BNZ_crystal and elem C", 1)
print("carbon atoms in crystal ligand:", len(ref))

for st in range(1, 10):
    dock = cmd.get_coords("pose and elem C", st)
    if len(dock) != len(ref):
        print("mode", st, ": atom count mismatch", len(dock), len(ref))
        continue
    # benzene is symmetric: try all atom matchings, keep the best
    best = min(np.sqrt(((ref - dock[list(p)])**2).sum(1).mean())
               for p in itertools.permutations(range(len(ref))))
    cen = np.linalg.norm(ref.mean(0) - dock.mean(0))
    print("mode %d: RMSD = %.2f A, centroid distance = %.2f A" % (st, best, cen))