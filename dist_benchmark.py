import numpy as np
import MDAnalysis as mda
from MDAnalysis.coordinates import PDB
from MDAnalysis.analysis import distances
import mdtraj
from pymol import cmd
from vmd import molecule, atomsel, measure


def get_dist_mda():
    u = mda.Universe("data/two_h2o.pdb")
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
    traj = mdtraj.load_pdb("data/two_h2o.pdb")
    i = 0
    while i < 100:
        print(mdtraj.compute_distances(traj, [[0, 1]]))
        i += 1
    # The distance found using this method is 10x smaller than the other methods


def get_dist_pymol():
    cmd.load("data/two_h2o.pdb")
    i = 0
    while i < 100:
        print(cmd.distance("index 1", "index 2"))
        i += 1
    # PyMol not running message, not sure if that is intended.


def get_dist_vmd():
    molid = molecule.load("pdb", "data/two_h2o.pdb")
    sel = atomsel('type O')
    i = 0
    while i < 100:
        print(measure.bond(0, 1))
        i += 1


u = mda.Universe("data/two_h2o.pdb")
ox = u.select_atoms("name O")
a = ox.positions[0]
b = ox.positions[1]
get_dist_np(a, b)

get_dist_mdtraj()
get_dist_mda()
get_dist_pymol()
get_dist_vmd()

