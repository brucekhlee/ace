import MDAnalysis as mda
import mdtraj


# MDAnalysis Method

# u = mda.Universe("SPIKE_ACE2_mut2.pdb")
#
# spike = u.select_atoms("segid A or segid B or segid C")
#
# # 62806 is the target number of atoms
# print("Number of atoms in selection: ", len(spike))
#
# print(spike.center_of_mass())

# mdtraj Method

traj = mdtraj.load_pdb("SPIKE_ACE2_mut2.pdb")

spike_top = traj.topology

spike_traj = spike_top.select("index 1")

print(spike_traj.xyz)

# print(mdtraj.compute_center_of_mass(spike_traj))
