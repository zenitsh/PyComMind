from commind.core import *
from commind.v import *
from commind.ui import *
from commind.help import *

import commind.ui.mainwindow

def main():
    print(commind.help())
    commind.ui.mainwindow.run()