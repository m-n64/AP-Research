import sys
import os
from pathlib import Path

def parent_path(parents = 1, crpth = Path(__file__)):

    for i in range(parents):
        crpth = crpth.parent

    return crpth

print(parent_path())