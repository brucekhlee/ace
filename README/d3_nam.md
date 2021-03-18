

# file location

Go to /home/khlee/work/docking/d3_nam

See InducedFit_*/*.maegz

#
cd /home/khlee/work/docking/d3_nam/InducedFit_7CMU
cp InducedFit_7CMU-out.maegz InducedFit_7CMU-out.mae.gz
gunzip InducedFit_7CMU-out.mae.gz
/share/apps/schrodinger/suite2021-1/utilities/structconvert -imae InducedFit_7CMU-out.mae -opdb d3x.pdb

cd /home/khlee/work/docking/d3_nam/InducedFit_d2active
cp InducedFit_d2active-out.maegz InducedFit_d2active-out.mae.gz
gunzip InducedFit_d2active-out.mae.gz
/share/apps/schrodinger/suite2021-1/utilities/structconvert -imae InducedFit_d2active-out.mae -opdb d2x.pdb


