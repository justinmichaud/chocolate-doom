# PagerDuty Doom - Deadliest incident management solution

Get revenge on your incidents by shooting them! This mod of doom spawns an enemy for every open incident on your account,
and resolves them when shot.

Disclaimer: This is not in any way affiliated with or endorsed by PagerDuty. I just made this for fun.
Disclaimer: This code is full of potential buffer overruns and shell injection vulnerabilities. Please do not run this on an account you do not control!

Screenshots:

TODO screenshots

To build doom:
```
mkdir build
./autogen.sh
./configure prefix=~/workspace2/chocolate-doom/build/
make -j4
make install
build/bin/chocolate-doom -iwad doom1.wad
```

To build and run the demo:

To run with modded level, buy original doom.wad (non shareware), put it in the root directory, and run

```
export PD_API_KEY="[SNIP]"
pip install -r pd/requirements.txt
build/bin/chocolate-doom -iwad doom.wad -file edit.wad
```

Heavily inspired by (and including code from) https://github.com/orsonteodoro/psdoom-ng1