# Pagerduty Doom - Deadliest incident management solution

Get revenge on your incidents by shooting them! This mod of doom spawns an enemy for every incident on your account.

TODO everything

To build:
```
mkdir build
./autogen.sh
./configure prefix=~/workspace2/chocolate-doom/build/
make -j4
make install
build/bin/chocolate-doom -iwad doom1.wad
```

To run with modded level, buy original doom.wad (non shareware) and run `build/bin/chocolate-doom -iwad doom.wad -file edit.wad`

Inspired by (and including code from) https://github.com/orsonteodoro/psdoom-ng1