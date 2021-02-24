#  Local Schrodinger Documentation

    # On Mac, go to terminal and then
    open /opt/schrodinger/suites2020-2/docs/Documentation.htm

# Using Maestro


# Preparing Protein 
==> User Manuals ==> Protein Preparation Guide

# Preparing Ligand
==> User Manuals ==> LigPrep User Manuals

# Docking
https://www.schrodinger.com/training/videos/docking-ligand-docking/glide-ligand-docking-calculation

## Glide
1. Grid generation
2. Docking

## Induced Fit Docking
1. Documentation ==>  Tutorials ==>  Induced Fit Docking Tutorial
2. See the paper. https://pubmed.ncbi.nlm.nih.gov/16492153/
   Sherman, W., H. S. Beard and R. Farid (2006). "Use of an induced fit receptor structure in virtual screening." Chem Biol Drug Des 67(1): 83-84.


# command to check schrodinger license

    # on cragger
    /share/apps/schrodinger/suite2020-2/licadmin STAT
    # on mac
    /opt/schrodinger/suites2020-2/licadmin STAT


    # Pay attention to prime liceses.
    Users of PSP_PLOP:  (Total of 50 licenses issued;  Total of 0 licenses in use)
    Users of PSP_PLOP_MEMBRANE:  (Total of 50 licenses issued;  Total of 0 licenses in use)




# todo
0. parsing smile text files into individual files. (Andy)*****
1. openbabel converts smi into 3D (khlee)
2. Import ligands to maestro at once 
3. Rename ligand name in ligand.mae 
   preparing a automate script to rename compound names (Andy)*****
4. Do the ligprep for ligand.mae
5. protein strucutres (DAT-inward & DAT-outward)
6. docking and screening using glide ====> (khlee)




