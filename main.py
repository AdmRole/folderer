from tkinter import filedialog
from pathlib import Path
import os
import shutil

names = []
suffixes = []

sortDir = Path(filedialog.askdirectory())

for path in sortDir.iterdir():
    if path.is_file():
        print(f"Soubor: {path.name}, Přípona: {path.suffix}")
        names += [path.name]
        suffixes += [path.suffix]

tmp = []
for i in suffixes:
    tmp += [i.replace('.', '')]
suffixes = tmp
tmp = ''
suffixes = list(set(suffixes))
for i in suffixes:
    (sortDir/i).mkdir(exist_ok=True)
    
for i in names:
    # Zjistíme příponu souboru (bez tečky) pro určení cílové složky
    ext = Path(i).suffix.replace('.', '')
    
    # Definujeme odkud a kam
    old_path = sortDir/i
    new_path = sortDir/ext/i
    
    # Přesuneme
    shutil.move(old_path, new_path)
    print(f"Moved {i} to {ext}/")
