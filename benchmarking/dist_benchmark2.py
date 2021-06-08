import numpy as np
import MDAnalysis as mda
from MDAnalysis.coordinates import PDB
from MDAnalysis.analysis import distances
import mdtraj
from pymol import cmd
from vmd import molecule, atomsel, measure
from guppy import hpy

h = hpy()


def get_dist_mda(n=5):
    u = mda.Universe("tutorial/data/drd3_gi_pd.pdb")
    sel = u.select_atoms("name N")
    for i in range(n):
        for j in range(n):
            distances.self_distance_array(sel.positions)

    h.heap().dump("benchmarking/heaps/3_mda.out")


def get_dist_np(sel, n=5):
    for i in range(n):
        for j in range(n):
            np.linalg.norm(sel[i] - sel[j])

    h.heap().dump("benchmarking/heaps/2_np.out")


def get_dist_mdtraj(n=5):
    traj = mdtraj.load_pdb("tutorial/data/drd3_gi_pd.pdb")
    dist_arr = np.zeros((n, n))
    # for i in range(n):
    #     for j in range(n):

    i = 0
    while i < 100:
        if i == 0:
            print(mdtraj.compute_distances(traj, [[0, 1]]))
        else:
            mdtraj.compute_distances(traj, [[0, 1]])
        i += 1

    h.heap().dump("benchmarking/heaps/4_mdtraj.out")
    # The distance found using this method is 10x smaller than the other methods


def get_dist_pymol(n=5):
    cmd.load("tutorial/data/drd3_gi_pd.pdb")
    # cmd.select("polymer.protein")
    # atoms = cmd.count_atoms("polymer.protein")
    # print("Atoms selected: ", atoms)
    # residues = len(cmd.get_model("poly and chain C").get_residues())
    # dist_arr = np.zeros((residues, residues))
    # for i in range(residues):
    #     for j in range(residues):
    dist_arr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                ind_a = cmd.index("resi %d" % (i+1))
                ind_b = cmd.index("resi %d" % (j+1))
                temp_dist = []
                for a in range(len(ind_a)):
                    for b in range(len(ind_b)):
                        temp_dist.append(cmd.distance("index %d" % ind_a[a][1], "index %d" % ind_b[b][1]))
                dist_arr[i, j] = min(temp_dist)

    h.heap().dump("benchmarking/heaps/5_pymol.out")

    return dist_arr
    # PyMol not running message, not sure if that is intended.


def get_dist_vmd(n=5):
    molid = molecule.load("pdb", "tutorial/data/drd3_gi_pd.pdb")
    dist_arr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                sel = atomsel("chain A and resid %d" % (i+1))
                sel2 = atomsel("chain A and resid %d" % (j+1))
                temp_dist = []
                for a in range(len(sel)):
                    for b in range(len(sel2)):
                        temp_dist.append(measure.bond(sel.index[a], sel2.index[b]))

                # dist_arr[i, j] = min(temp_dist)

    h.heap().dump("benchmarking/heaps/6_vmd.out")


h.heap().dump('benchmarking/heaps/1_initial.out')

u = mda.Universe("tutorial/data/drd3_gi_pd.pdb")
s = u.select_atoms("protein")
input = s.positions
get_dist_np(input)

get_dist_mda()
get_dist_mdtraj()
pymol_arr = get_dist_pymol()
get_dist_vmd()
