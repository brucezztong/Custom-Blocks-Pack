CUSTOM BLOCKS PACK READ-ME -- VERSION A21.2.001.0033

GOAL:

In short, this modlet provides a common definition of custom blocks that have
previously appeared in multiple modlets. Instead of having each modlet define
the same block with a slightly different name, various POI modlets could
instead share (depend upon) this modlet.

DEPENDENCIES:

This modlet depends only on the Vanilla game and introduces no other
requirements or dependencies.

By design, other modlets depend upon this modlet. This is why the name of this
modlet's folder starts with "00". In this way the game will load this modlet
before any of the dependent modlets.

CLIENT INSTALLATION: (Windows)

1. Go to %APPDATA%/7DaysToDie

2. Locate or Create a "Mods" folder.
    The folder does not exist by default. If this is your first Mod, then you
    will need to create the Mods folder.

3. Place the "00-Custom-Blocks-Pack" folder in the Mods folder:
    %APPDATA%/7DaysToDie/Mods ... %APPDATA/7DaysToDie/Mods/00-Custom-Blocks-Pack

4. Install other modlets.

COMPLICATIONS:

If you use multiple modlets that depend upon this modlet, then you'll want to
use the most recent version of this modlet. Since each of those other modlets
have probably given you a copy of this Custom Blocks Pack modlet, you'll have
to look to the version number at the top of this document to determine which
is the newest.

IS THE MODLET SERVER-SIDE OR CLIENT-SIDE?

This modlet only includes XML definitions. Any other assets included are either
for documenation or testing. Thus, this modlet should work entirely on the
server side and should not need to be distributed to clients.

OVERHAUL MODS:

Overhaul Mods make extensive changes to the game. The interactions cannot be
predicted in advance. Since it only ads content, it shouldn't interfere. More
likely is that an overhaul may change something upon which this modlet depends.

DISTRIBUTION:

Others may choose to distribute this modlet along with other modlets. This is
intended. It is also a largely manual process, at least until 7D2D begins to
include more modlet integration features.

