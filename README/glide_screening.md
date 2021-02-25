
# parsing compound smiles into individual smile files & SDF files
see README file at one drive (docking_DAT/1-ligands/README)


# Maestro to prepare ligprep script/files
Manually setup and write to you schrodinger output directory

## rsync the ligprep script/files from local to remote
rsync -auv --progress ${LOCAL} ${REMOTE}

LOCAL="path of your files"
REMOTE="username@cragger.nida.nih.gov:~/path"

# then go compute node

# load module
module load schrodinger/2021-1 

# check schrodinger version
$ which maestro
/share/apps/schrodinger/suite2021-1/maestro


# excute the script
$ ./ligprep_tck_compounds.sh
JobId: compute-0-0-0-6037d810

## rsync from remote to local
rsync -auv --progress {REMOTE}  ${LOCAL} 

LOCAL="path of your files"
REMOTE="username@cragger.nida.nih.gov:~/path"


## I/O

    # input
    ligprep_tck_compounds.inp
    ligprep_tck_compounds.maegz
    ligprep_tck_compounds.sh*
    # output 
    ligprep_tck_compounds.log        <=== output log
    ligprep_tck_compounds-out.maegz  <=== output file






