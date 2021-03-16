from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdmolfiles
from rdkit.Chem.Draw import rdDepictor
from rdkit.Chem.Draw import IPythonConsole
from rdkit import rdBase
import gzip
rdDepictor.SetPreferCoordGen(True)

maemols = rdmolfiles.MaeMolSupplier("glide-dock_XP_4_tcks.mae")
mols = [m for m in maemols]
Draw.MolsToGridImage(mols)