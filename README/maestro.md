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

# todo (02/26)
1. find a way to covert *.mae into *.pdb (Andy)
2. docking 4 ligands with inward/outward facing (Andy)
3. find a paper and send to everyone (Monday)
4. fragment docking (khlee) protocol needed 
5. need a python script to handle mae file (i.e., grep specific information from mae)

# todo (03/12)
==> we want to calculate ligand rmsd between two different ligands. 

Q. Which software package we should use for ligand rmsd analysis?

Gromacs has a tool that does this. I believe it can be done in command line.

    gmx rms -s cocrystalized_ligand.pdb -f docked_ligand.pdb -fit none -o output.xvg

Reference: https://www.researchgate.net/post/How_can_I_calculate_RMSD_to_crystalographic_ligand_and_a_docked_ligand

I believe we can also just use NumPy to do it.
There is an answer in that link that details the steps to calculate RMSD.
I do not know if this is exactly applicable to what we need.

Q. Can we read mae file in python?

Yes, we can use RDKit.
https://iwatobipen.wordpress.com/2018/11/01/read-maestro-format-file-from-rdkit/

Q. Can we call schrondinger API in python?

I think so. But you have to use Schrodinger's python 3.

    $SCHRODINGER/run python3

So far it looks like you can do it from command line. I believe the above command is used to set up the environment variables.
If we know how to set up the environment, we should be able to set up an environment in PyCharm IDE.

Reference: http://content.schrodinger.com/Docs/r2018-2/python_api/intro.html#:~:text=To%20use%20Schr%C3%B6dinger's%20modules%20%5B1,(see%20Interacting%20with%20Maestro).

Q. mae file format to others?

We can convert other files to and from mae using schrodinger structconvert script:
    
    On cragger, script can be found at path:
    /share/apps/schrodinger/suite2021-1/utilities/structconvert
    
    Example run/protocol:
    module load schrodinger/2021-1
    cd /home/aguan/docking/docking4tcks
    cp glide-dock_SP_4_tcks.maegz glide-dock_SP_4_tcks.mae.gz
    gunzip glide-dock_SP_4_tcks.mae.gz
    /share/apps/schrodinger/suite2021-1/utilities/structconvert -imae glide-dock_SP_4_tcks.mae -opdb test.pdb

Using the file extension in the options (ex. imae) has been deprecated.
You only need to use -i and -o options.

If multiple structures in the .mae file, the structures will be written to separate pdb files.

For more, check:
https://www.schrodinger.com/kb/329
