#
# Name each Creality build v110_crs_<timestamp>.bin
# The printer bootloader skips a .bin name it has already seen.
#
Import("env")

from datetime import datetime

env["PROGNAME"] = "v110_crs_" + datetime.now().strftime("%Y%m%d_%H%M%S")
