from pymol import cmd


def align_rms(target1, target2):
    cmd.load(target1, "t1")
    cmd.load(target2, "t2")
    cmd.align("t1", "t2")
    return cmd.rms("t1 and resn unk", "t2 and resn unk")


target1 = "d3x-1.pdb"
target2 = "d2x-1.pdb"
print(align_rms(target1, target2))