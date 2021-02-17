import numpy as np
import MDAnalysis as mda
from MDAnalysis.coordinates import PDB
from MDAnalysis.analysis import distances
import mdtraj
from pymol import cmd


def get_dist_mda():
    u = mda.Universe("two_h2o.pdb")
    i = 0
    while i < 100:
        print(distances.self_distance_array(u.trajectory.ts.positions))
        i += 1


def get_dist_np(a, b):
    i = 0
    while i < 100:
        print(np.linalg.norm(a - b))
        i += 1


def get_dist_mdtraj():
    traj = mdtraj.load_pdb("two_h2o.pdb")
    i = 0
    while i < 100:
        print(mdtraj.compute_distances(traj, [[0, 1]]))
        i += 1
    # The distance found using this method is 10x smaller than the other methods


def get_dist_pymol():
    cmd.load("two_h2o.pdb")
    cmd.distance("index 1, index 2")
    # Error here. Maybe my syntax is wrong.


u = mda.Universe("two_h2o.pdb")
ox = u.select_atoms("name O")
a = ox.positions[0]
b = ox.positions[1]
get_dist_np(a, b)

get_dist_mdtraj()
get_dist_mda()
get_dist_pymol()

