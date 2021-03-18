from pymol import cmd

d3x_1 = cmd.load("d3x-1.pdb")
d3x = cmd.load("d3x.pdb")
cmd.align("d3x_1", "d3x")
cmd.rms("d3x and resn unk, d2x and resn unk")

# load d3x-1, d3x
#
# load d2x-1, d2x
#
#
#
# align d3x, d2x
#
# rms d3x and resn unk, d2x and resn unk
