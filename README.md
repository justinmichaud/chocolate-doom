# PagerDuty Doom - Deadliest incident management solution

Get revenge on your incidents by shooting them! This mod of doom spawns an enemy for every open incident on your account,
and resolves them when shot.

Disclaimer: This is not in any way affiliated with or endorsed by PagerDuty. I just made this for fun.

Screenshots:

TODO screenshots

To build:
```
mkdir build
./autogen.sh
./configure prefix=~/workspace2/chocolate-doom/build/
make -j4
make install
build/bin/chocolate-doom -iwad doom1.wad
```

To run with modded level, buy original doom.wad (non shareware), put it in the root directory, and run
```
build/bin/chocolate-doom -iwad doom.wad -file edit.wad
```

Heavily inspired by (and including code from) https://github.com/orsonteodoro/psdoom-ng1