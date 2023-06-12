# Custom Block Pack (A21.0.001)
The motivation to create this modlet was to make it easier to share custom
block definitions between custom POI developers. As a separate modlet, multiple
modlets can depend upon it instead of each modlet creator defining their own
version of the same block definition, plus perhaps avoid block name collisions.

This modlet started at the end of A20 with a bunch of ZZTong custom blocks,
then Stallionsden piled on with a huge collection of ideas bringing along
blocks and other configuration from Pille and MPLogue.

The Future direction for this modlet likely will include adding a libary of
Parts for POI developers to use. You should also expect bug fixes and some
block redefinitions as A21 becomes better known.

### Prefab Editor Tips
All of the blocks in this pack have names that start with a "cbp" prefix, so in
the Prefab Editor when using the block menu, you can type in "cbp" and see a
list of these blocks and placeholders.

Helper blocks are tinted red just like the TFP Helpers/Placeholders are.
Otherwise, blocks from this modlet are tinted blue to make it more obvious to
you if you are building in a dependency to this modlet.

### Tools

Pille's Super Brush is included in this modlet for POI developer convenience.
If you're not aware of this tool, it acts just like a TFP paintbrush but it is
faster.

## Custom Blocks
**ATM Machines** - The pack adds an empty ATM machine, plus a helper which is
described later to allow your POIs to _sometimes_ include an ATM.

* bcpATMEmpty
* bcpATMRandomHelper
* bcpATMRandomHelperAir

**Backpacks** - The game includes a number of packs, purses, and so forth that
give out loot. This pack adds a number of empty (or effectively empty) versions.

* cbpBackpack01Empty
* cbpBackpack03Empty
* cbpDuffle01Empty
* cbpPurse01Empty
* cbpSportsBag01Empty
* cbpSportsBag02Empty

**Barrels** - A couple of fuel barrels have been included that do not give out
any gasoline. They still explode, so I guess they're full of gasoline vapors.

* cbpBarrelGasSingle00Empty
* cbpBarrelGasSingle45Empty

**Bathroom Cabinets** - If you use the TFP kitchen cabinets in a bathroom then
your POI's bathrooms will give out canned food. These blocks offer cabinets
that give out items more appropriate for the bathroom.

* cbpBathroomCabinetRedBottom
* cbpBathroomCabinetRedBottomHelper
* cbpBathroomCabinetRedTop
* cbpBathroomCabinetRedTopHelper
* cbpBathroomCabinetOldBottom
* cbpBathroomCabinetOldBottomHelper
* cbpBathroomCabinetOldTop
* cbpBathroomCabinetOldTopHelper

**Bookcases and Book Shelves** - This is a bookcase that does not give out books and
instead gives out other things you might find on a bookshelf.

* cbpBookcaseBookless
* cbpBookcaseCornerPoor
* cbpBookShelfSingleBottom
* cbpBookShelfSingleTop
* cbpBookShelfDoubleBottom
* cbpBookShelfDoubleTop
* cbpBookShelfSingleCapBottom
* cbpBookShelfSingleCapTop

**Book Piles** - These are decoration versions of book piles.
* cbpBookPile01
* cbpBookPile02
* cbpBookPile03
* cbpBookPile04
* cbpBookPile05
* cbpBookPile06
* cbpBookPile07
* cbpBookPile08
* cbpBookPile09
* cbpBookPile10
* cbpBookPile11
* cbpBookPile12
* cbpBookPile13
* cbpBookPile14
* cbpBookPile15

**Offset Blocks** - Sometimes a POI designer just wants a version of a TFP
block that doesn't sit in the middle of the block's space. Here are a number
of blocks that have been offset so you can place them closer to a wall.

* cbpCoffeeMakerLeftOffset
* cbpCoffeeMakerRightOffset
* cbpCookingPotOffset
* cbpComputerDeskTopOCLeftOffset
* cbpComputerDeskTopOCRightOffset
* cbpMannequinFemaleOffset
* cbpMannequinMaleOffset
* cbpSignExitLightMidOffset
* cbpSignExitLightLowOffset
* cbpSignShopOpenMidOffset
* cbpSignShopOpenLowOffset
* cbpToasterOffset

**Shipping & Storage Crates** - These come in a few varieties. If the name
include "Cube" then it is just a block that looks like a storage crate. It
takes the same amount of punishment that a real crate can take but has no
inventory and gives no loot.

Storage Crates with "Empty" in their name are connected to a largely empty
loot list designed to give out nothing of use, if anything.

Storage Crates with a purpose (Ammo, Building, Weapons, etc.) will give out
minor loot in that vein, typically 1/3 to 1/2 that found in a TFP crate.

* cbpStorageGenericCube
* cbpStorageGenericEmpty
* cbpStorageGenericAmmo
* cbpStorageGenericAmmoCube
* cbpStorageGenericBuilding
* cbpStorageGenericBuildingCube
* cbpStorageGenericExplosives
* cbpStorageGenericExplosivesCube
* cbpStorageGenericFood
* cbpStorageGenericFoodCube
* cbpStorageGenericMedical
* cbpStorageGenericMedicalCube
* cbpStorageGenericWeapons
* cbpStorageGenericWeaponsCube
* cbpShippingCrateShamwayCube
* cbpShippingCrateLabEquipmentCube
* cbpShippingCrateBookstoreCube
* cbpShippingCrateCarPartsCube
* cbpShippingCrateShotgunMessiahCube
* cbpShippingCrateWorkingStiffsCube
* cbpShippingCrateSavageCountryCube
* cbpShippingCrateMoPowerElectronicsCube

There are also Helper blocks for the various Crates. (see below)

**Vending Machines** - The pack adds an empty vending machine.

* cbpVendingMachine2Empty

## Other Blocks
For those interesting in mixing in an homage to Westworld (Movie 1973, TV
Series 2016), there are three blocks available:

* cbpDelosAndroidMale
* cbpDelosAndroidFemale
* cbpDelosStorageCrate

## Helper Blocks
These blocks stand in for a number of possible blocks. This is a normal game
feature POI developers likely already know. For instance, placing TFP's
"carsRandomHelper" block, the Random World Generator will place one of many
different cars. To know what could be placed, you would have to read the game's
blockplaceholders.xml file. You could look in this modlet's
blockplaceholders.xml file as well, but this document attempts to describe the
purpose of each Helper.

### ATM Machine Helpers
*cbpATMRandomHelper* - This placeholder will be replaced by an empty ATM (90%),
or a TFP ATM with loot (10%).

*cbpATMRandomHelperAir* - This placeholder will be replaced by Air (50%), an
Empty ATM (40%), or a TFP ATM with loot (10%).

### Bathroom Cabinet Helpers
All of these helpers work the same way. There's a 65% chance of an open cabinet
being placed which will have no loot leaving a 35% chance for a closed cabinet.

The Helpers are:
* cbpBathroomCabinetRedBottomHelper
* cbpBathroomCabinetRedTopHelper
* cbpBathroomCabinetOldBottomHelper
* cbpBathroomCabinetOldTopHelper

### Clothing Racks, Stacks, and Shelves
A variety of Random Helpers can place clothing racks or air. They will place
air roughly 60% of the time.
* cbpClothesRackRoundPantsRandomLootHelper
* cbpClothesRackRoundTopsRandomLootHelper
* cbpClothesRackRectanglePantsRandomLootHelper
* cbpClothesRackRectangleShirtsRandomLootHelper
* cbpClothesRackWallPantsRandomLootHelper
* cbpClothesRackWallTopRandomLootHelper
* cbpClothesShelfHalfJeansRandomLootHelper
* cbpClothesShelfHalfTopsRandomLootHelper
* cbpClothesShelfStackJeansRandomLootHelper
* cbpClothesShelfStackTopsRandomLootHelper
* cbpClothesPileFloorRandomLootHelper
* cbpRackRoundMilitaryPantsRandomLootHelper
* cbpClothesRackRoundMilitaryShirtsRandomLootHelper
* cbpRackRackRectangleMilitaryPantsRandomLootHelper
* cbpClothesRackRectangleMilitaryShirtsRandomLootHelper
* cbpClothesRackWallMilitaryPantsRandomLootHelper
* cbpClothesRackWallMilitaryTopsRandomLootHelper
* cbpStoreShelfDoubleBottomShoesRandomLootHelper
* cbpStoreShelfDoubleTopShoesRandomLootHelper
* cbpStoreShelfSingleBottomShoesRandomLootHelper
* cbpStoreShelfSingleTopShoesRandomLootHelper

### Cooking Pot Helper
*cbpCookingPotHelper* - This can be air (40%), a cooking pot (50%), or a bomb
(10%). It exists to both randomize minor loot (a cooking pot) and to keep
survivors on their toes (the bomb).

### Corpse Helpers
*cbpCorpseHumanHelper* - This can be any of the 4 TFP corpses (20% each), with
smaller chances of getting bones or a skull (10% each).

*cbpCorpseHumanHelperAir* - This is air 50% of the time, the 4 TFP corpses (10%
each), bones (5%), or a skull (5%).

### Farming Helpers
*cbpPlantedMushroomHarvestRandomHelper* - This fills a gap in TFP's helper
blocks. TFP doesn't have a help block for mushroom. This helper is defined
exactly like the other TFP helpers.

### Freezer Helpers
Freezer helpers all have a chance to be air, about 30% of the time. Note the
difference between Grocery and Beverage Freezers.

* cbpFreezerGroceriesMiddleRandomLootHelper
* cbpFreezerBeveragesMiddleRandomLootHelper
* cbpFreezerBeveragesStandaloneRandomLootHelper

### Garbage Helper
These helpers can randomize the minor debris found around the world. These will
lead to garbage, broken glass, various minor broken objects, and even a scrap
metal piles. The air version has a 20% chance of being air.

* cbpGroundDecoRandomHelper
* cbpGroundDecoRandomHelperAir

### Land Mine Helpers
There are a number of variations of these helpers, some that only give out a
specific kind of landmine, such as the Candy Tin variety. You will sometimes
see a plain old hubcap placed too. These helpers come with a number in them
that indicate the chance of getting an Air block. For example:

*cbpLandMine50RandomHelper* - The number indicates the chance the placeholder
will be air. So, 50 means there's a 50% chance of it actually being a landmine.

*cbpLandMine10RandomHelper* - This is just like the cbpLandMine50RandomHelper,
except there's a 10% chance of it actually being a landmine, so 90% of the time
it is an Air block.

Here's a complete list of landmine helpers:

* cbpLandMine50RandomHelper
* cbpLandMine10RandomHelper
* cbpLandMineCandyTin50RandomHelper
* cbpLandMineCandyTin10RandomHelper
* cbpLandMineHubcap50RandomHelper
* cbpLandMineHubcap10RandomHelper
* cbpLandMineAirFilter50RandomHelper
* cbpLandMineAirFilter10RandomHelper

### Movie Poster Helpers
*cbpMoviePosterRandomHelper* - Shows one of the TFP movie posters with an equal
chance for any poster.

*cbpMoviePosterTheaterRandomHelper* - Shows one of the TFP movie posters, but
this is the theater version of the posters.

### Shipping Crate Helpers
*cbpShamwayShippingCrateHelper* - This is a series of helpers, where the
underlined can be any of the TFP shipping containers. The purpose of these
helpers is to let a POI Designer scatter a lot of shipping containers (crates)
around a POI without giving out a lot of loot. There is only a 1 in 100 chance
of one of these turning out to be a real crate with loot.

*cbpShamwayShippingCrateHelperAir* - This is the "Air" version of the
cbpShamwayShippingCrateHelper. This is defined as a 50 in 100 chance (50%) that
the helper will be replaced with an Air block. Otherwise, 1 in 100 is a real
crate with loot.

Here's a complete list of shipping crate helpers:

* cbpShippingCrateShamwayHelper
* cbpShippingCrateShamwayHelperAir
* cbpShippingCrateLabEquipmentHelper
* cbpShippingCrateLabEquipmentHelperAir
* cbpShippingCrateBookstoreHelper
* cbpShippingCrateBookstoreHelperAir
* cbpShippingCrateCarPartsHelper
* cbpShippingCrateCarPartsHelperAir
* cbpShippingCrateShotgunMessiahHelper
* cbpShippingCrateShotgunMessiahHelperAir
* cbpShippingCrateWorkingStiffsHelper
* cbpShippingCrateWorkingStiffsHelperAir
* cbpShippingCrateSavageCountryHelper
* cbpShippingCrateSavageCountryHelperAir
* cbpShippingCrateMoPowerElectronicsHelper
* cbpShippingCrateMoPowerElectronicsHelperAir

### Shopping Cart Helper
*cbpShoppingCartRandomHelperAir* - There can become Air (50%), an empty shopping
cart (30%), or a lootable shopping cart (20%).

### Store Shelves
Store shelves were added to satisfy a desire by some prefabbers to have POIs
that are not entirely full of empty shelves, but yet didn't give out a lot of
loot. They can all end up placing air roughly 30 to 60% of the time depending
on the block.

* cbpStoreShelfSingleBottomFoodRandomLootHelper
* cbpStoreShelfSingleTopFoodRandomLootHelper
* cbpStoreShelfDoubleBottomFoodRandomLootHelper
* cbpStoreShelfDoubleTopFoodRandomLootHelper
* cbpStoreShelfSingleBottomHardwareRandomLootHelper
* cbpStoreShelfSingleTopHardwareRandomLootHelper
* cbpStoreShelfDoubleBottomHardwareRandomLootHelper
* cbpStoreShelfDoubleTopHardwareRandomLootHelper
* cbpStoreShelfSingleBottomPharmaRandomLootHelper
* cbpStoreShelfSingleBottomTrashRandomLootHelper
* cbpStoreShelfSingleTopTrashRandomLootHelper
* cbpStoreShelfDoubleBottomTrashRandomLootHelper
* cbpStoreShelfDoubleTopTrashRandomLootHelper
* cbpStoreShelfDoubleBottomTrashRandomLootHelper
* cbpShelvesWoodRandomLootHelper
* cbpShelvesFreeStandingRandomLootHelper
* cbpShelvesMetalRandomLootHelper
* cbpMilitaryMetalShelvesRandomLootHelper

### Tractors
The Tractor helper mimics the game's automobile helpers for the non-air version
of the helper all tractors have an equal chance of being placd. For the air
version there's a 60% chance of placing an air block.

* cbpTractorRandomHelper
* cbpTractorRandomHelperAir

### Tree Stump POI
This helper either places 

### Vending Machines
*cbpVendingMachineRandomHelper* - This can be a broken vending machine (50%), an
empty vending machine (40%), or a working vending machine (10%).

*cbpVendingMachineRandomHelperAir* - This can be Air (30%), a broken vending
machine (30%), an empty vending machine (30%), or a working vending machine (10%)

### Weapon Racks and Displays
This series of helpers focus on randomizing loot blocks for weapons racks and
displays.

* cbpGunRackLargeRandomLootHelper
* cbpGunRackSmallArmorRandomLootHelper
* cbpGunRackSmallMagazineRandomLootHelper
* cbpDisplayCaseAmmoLeftRandomLootHelper
* cbpDisplayCaseAmmoMiddleRandomLootHelper
* cbpDisplayCaseAmmoRightRandomLootHelper

### Water Cooler Helpers
There are two lines of Water Cooler blocks -- those that are centered and those
that are offset. Within each line you can either get a full or empty block.
The air version of the helpers has a 50% chance of placing an air block.

* cbpWaterCoolerRandomHelper
* cbpWaterCoolerRandomHelperAir
* cbpWaterCoolerFullSideCenteredRandomHelper
* bpWaterCoolerFullSideCenteredRandomHelperAir

## Contributors
The following persons contributed to this modlet:

**Pille** - Contributed the Super Brush tool/item.

**MP Logue** - Contributed a number of interesting blocks with special effects
and blocks that assist with structural integrity.

**Stallionsden** - Collaborated on various loot settings, inspired Landmine,
Vending Machine and ATM blocks, contributed the Mushroom Helper. Then added
a truly massive number of blocks and placeholders.

**ZZTong** - Contributed various shipping crate blocks and helpers,
contributed empty and low-loot block variations, contributed the Delos (West
World) blocks, worked on a variety of offset block variations.
