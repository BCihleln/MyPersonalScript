import os
import glob
import shutil
from tqdm import tqdm

SourceDir = r"Corpus\noisy"
TargetDir = r"Corpus\Nagetive"
Target = os.path.join(SourceDir,"*\*.wav")

assert os.path.exists(SourceDir)
assert os.path.exists(TargetDir)


SourceFiles = glob.glob(Target)

if len(SourceFiles):
    for file in tqdm(SourceFiles):
        shutil.move(file,TargetDir)
else:
    print("Target files Not Found !")