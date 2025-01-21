
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ClassSystem.article import Article
from ClassSystem.months import Month

month = Month(1,1962)

print(month.info)


