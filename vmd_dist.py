from vmd import atomsel
from vmd import molecule
from pymol import cmd

molid = molecule.load("pdb", "two_h2o.pdb")
print(molid)
sel = atomsel('type O')
print(sel.x)
print(sel[0].x)