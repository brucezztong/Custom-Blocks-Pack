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
* cbpOffsetStainedGlassPlate
* cbpSmokeCapOffset
* cbpSaleSaleSaleSign
* cbpMetalCatwalkBridge
* cbpCubeTeeBridge
* cbpShippingContainerSideStable
* cbpSemiFlatbedMiddleA
* cbpSemiFlatbedMiddleB
* cbpSemiFlatbedFrontA
* cbpSemiFlatbedFrontB

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

**Offset Hazard Pipes** - TFP hazard Pipes offsetted so you can hide the pipes inside walls and just show the flames.

* cbpPipeSmallRed3mOffset
* cbpPipeFireHazardBlack2mOffset
* cbpPipeFireHazardBlack3mOffset
* cbpPipeFireHazardBlack4mOffset
* cbpPipeFireHazardRed2mOffset
* cbpPipeFireHazardRed3mOffset
* cbpPipeFireHazardRed4mOffset
* cbpPipeFireHazardYellow2mOffset
* cbpPipeFireHazardYellow3mOffset
* cbpPipeFireHazardYellow4mOffset
* cbpPipeFireHazardGreen2mOffset
* cbpPipeFireHazardGreen3mOffset
* cbpPipeFireHazardGreen4mOffset
* cbpPipeFireHazardBlue2mOffset
* cbpPipeFireHazardBlue3mOffset
* cbpPipeFireHazardBlue4mOffset
* cbpPipeFireHazardGrey2mOffset
* cbpPipeFireHazardGrey3mOffset
* cbpPipeFireHazardGrey4mOffset
* cbpPipeFireHazardWallBlack2mOffset
* cbpPipeFireHazardWallBlack3mOffset
* cbpPipeFireHazardWallBlack4mOffset
* cbpPipeFireHazardWallRed2mOffset
* cbpPipeFireHazardWallRed3mOffset
* cbpPipeFireHazardWallRed4mOffset
* cbpPipeFireHazardWallYellow2mOffset
* cbpPipeFireHazardWallYellow3mOffset
* cbpPipeFireHazardWallYellow4mOffset
* cbpPipeFireHazardWallGreen2mOffset
* cbpPipeFireHazardWallGreen3mOffset
* cbpPipeFireHazardWallGreen4mOffset
* cbpPipeFireHazardWallBlue2mOffset
* cbpPipeFireHazardWallBlue3mOffset
* cbpPipeFireHazardWallBlue4mOffset
* cbpPipeFireHazardWallGrey2mOffset
* cbpPipeFireHazardWallGrey3mOffset
* cbpPipeFireHazardWallGrey4mOffset

**Hazard Rocks** - Used to hide actual block in small spaces.
 
* cbpFireHazardRock2M
* cbpFireHazardRock3M
* cbpFireHazardRock4M

**Hazard Pipe No Model Offset** - A pipe that is 1x1x1 so you can add stuff on top of it where the flame is. 

* cbpFireHazardBlackNomodeloffset

**Drone Hazards** - A right and left pipe used to make the Drone deco look like it is operating. 

* cbpDroneright
* cbpDroneLeft

**Server Racks** - TFP Server racks tinted a different colour.

* cbpServerRackBlack

**TFP Bundle Storage** - Utilises the TFP storage crates not yet in game as lootable blocks in game.

[DECO]
* cbpWoodboxCube
* cbpIronboxCube
* cbpSteelboxCube
[LOOTABLE]
* cbpWoodbox
* cbpIronbox
* cbpSteelbox

**Store Shelves Deco** - Shelves filled with said shelf name but not lootable.

* cbpStoreShelfSingleBottomFood01
* cbpStoreShelfSingleBottomFood02
* cbpStoreShelfSingleTopFood01
* cbpStoreShelfDoubleBottomFood01
* cbpStoreShelfDoubleBottomFood02
* cbpStoreShelfDoubleTopFood01
* cbpStoreShelfSingleBottomHardware01
* cbpStoreShelfSingleBottomHardware02
* cbpStoreShelfSingleTopHardware01
* cbpStoreShelfSingleTopHardware02
* cbpStoreShelfDoubleBottomHardware01
* cbpStoreShelfDoubleBottomHardware02
* cbpStoreShelfDoubleBottomHardware03Rags
* cbpStoreShelfDoubleTopHardware01
* cbpStoreShelfDoubleTopHardware02Rags
* cbpStoreShelfSingleBottomPharmaGoods01
* cbpStoreShelfSingleBottomPharmaGoods02
* cbpStoreShelfDoubleBottomPharmaGoods01
* cbpStoreShelfDoubleBottomPharmaGoods02
* cbpStoreShelfSingleBottomTrash01
* cbpStoreShelfSingleBottomTrash02
* cbpStoreShelfSingleTopTrash01
* cbpStoreShelfSingleTopTrash02
* cbpStoreShelfDoubleBottomTrash01
* cbpStoreShelfDoubleBottomTrash02
* cbpStoreShelfDoubleTopTrash01
* cbpStoreShelfElectronicsSingleBottomPC
* cbpStoreShelfElectronicsSingleBottomElectronicsMonitor
* cbpStoreShelfElectronicsSingleBottomGoodsMisc
* cbpStoreShelfElectronicsSingleBottomHeadphones
* cbpStoreShelfElectronicsSingleBottomKeyboard
* cbpStoreShelfElectronicsSingleBottomLaptopClosed
* cbpStoreShelfElectronicsSingleBottomLaptopOpen
* cbpStoreShelfElectronicsSingleBottomSpeaker
* cbpStoreShelfElectronicsDoubleBottomGoods01
* cbpStoreShelfElectronicsDoubleBottomGoods02
* cbpStoreShelfElectronicsDoubleBottomGoods03
* cbpStoreShelfElectronicsDoubleBottomGoods04
* cbpShelvesWoodFullA
* cbpShelvesFreeStandingFullA
* cbpShelvesMetalFullA
* cbpMilitaryMetalShelvesFull

**Store Shelves Lootable** - Shelves filled with said shelf name but not lootable.

* cbpStoreShelfSingleBottomFoodA
* cbpStoreShelfSingleBottomFoodB
* cbpStoreShelfSingleTopFoodA
* cbpStoreShelfDoubleBottomFoodA
* cbpStoreShelfDoubleBottomFoodB
* cbpStoreShelfDoubleTopFoodA
* cbpStoreShelfSingleBottomHardwareA
* cbpStoreShelfSingleBottomHardwareB
* cbpStoreShelfSingleTopHardwareA
* cbpStoreShelfSingleTopHardwareB
* cbpStoreShelfDoubleBottomHardwareA
* cbpStoreShelfDoubleBottomHardwareB
* cbpStoreShelfDoubleBottomHardwareCRags
* cbpStoreShelfDoubleTopHardwareA
* cbpStoreShelfDoubleTopHardwareBRags
* cbpStoreShelfSingleBottomPharmacyGoodsA
* cbpStoreShelfSingleBottomPharmacyGoodsB
* cbpStoreShelfDoubleBottomPharmacyGoodsA
* cbpStoreShelfDoubleBottomPharmacyGoodsB
* cbpStoreShelfSingleBottomTrashA
* cbpStoreShelfSingleBottomTrashB
* cbpStoreShelfSingleTopTrashA
* cbpStoreShelfSingleTopTrashB
* cbpStoreShelfDoubleBottomTrashA
* cbpStoreShelfDoubleBottomTrashB
* cbpStoreShelfDoubleTopTrashA
* cbpStoreShelfElectricsSingleBottomPCA
* cbpStoreShelfElectricsSingleBottomElectronicsMonitorA
* cbpStoreShelfElectricsSingleBottomGoodsMiscA
* cbpStoreShelfElectricsSingleBottomHeadphonesA
* cbpStoreShelfElectricsSingleBottomKeyboardA
* cbpStoreShelfElectricsSingleBottomLaptopClosedA
* cbpStoreShelfElectricsSingleBottomLaptopOpenA
* cbpStoreShelfElectricsSingleBottomSpeakerA
* cbpStoreShelfElectricsDoubleBottomGoodsA
* cbpStoreShelfElectricsDoubleBottomGoodsB
* cbpStoreShelfElectricsDoubleBottomGoodsC
* cbpStoreShelfElectricsDoubleBottomGoodsD
* cbpShelvesWoodFull
* cbpShelvesFreeStandingFull
* cbpShelvesMetalFull
* cbpMilitaryMetalShelvesFullA

**Clothes/Wall Racks Deco** - Racks that are just deco and not lootable. Also have seperated the racks to one having pants the other shirts ETC.

* cbpClothesRackRoundPants
* cbpClothesRackRoundShirts
* cbpClothesRackRectanglePants
* cbpClothesRackRectangleShirts
* cbpClothesRackWallPants
* cbpClothesRackWallLongSleeve
* cbpClothesRackWallSweater
* cbpClothesRackWallTShirts
* cbpClothesShelfHalfJeans01
* cbpClothesShelfHalfJeans02
* cbpClothesShelfHalfShirts01
* cbpClothesShelfHalfShirts02
* cbpClothesShelfHalfSweaters01
* cbpClothesShelfStackJeans01
* cbpClothesShelfStackJeans02
* cbpClothesShelfStackShirts01
* cbpClothesShelfStackShirts02
* cbpClothesRackRoundPantsMilitary
* cbpClothesRackRoundShirtsMilitary
* cbpClothesRackRectanglePantsMilitary
* cbpClothesRackRectangleShirtsMilitary
* cbpClothesRackWallPantsMilitary
* cbpClothesRackWallLongSleeveMilitary
* cbpClothesRackWallSweaterMilitary
* cbpClothesRackWallTShirtsMilitary
* cbpStoreShelfDoubleBottomShoesFull
* cbpStoreShelfDoubleTopShoesFull
* cbpStoreShelfSingleBottomShoesFull
* cbpStoreShelfSingleTopShoesFull

**Clothes/Wall Racks Lootable** - Racks that are just deco and lootable. Also have seperated the racks to one having pants the other shirts ETC.

* cbpClothesRackRoundPantsLoot
* cbpClothesRackRoundShirtsLoot
* cbpClothesRackRectanglePantsLoot
* cbpClothesRackRectangleShirtsLoot
* cbpClothesRackWallPantsLoot
* cbpClothesRackWallLongSleeveLoot
* cbpClothesRackWallSweaterLoot
* cbpClothesRackWallTShirtsLoot
* cbpClothesShelfHalfJeansA
* cbpClothesShelfHalfJeansB
* cbpClothesShelfHalfShirtsA
* cbpClothesShelfHalfShirtsB
* cbpClothesShelfHalfSweatersA
* cbpClothesShelfStackJeansA
* cbpClothesShelfStackJeansB
* cbpClothesShelfStackShirtsA
* cbpClothesShelfStackShirtsB
* cbpClothesPileFloorA
* cbpClothesRackRoundPantsMilitaryLoot
* cbpClothesRackRoundShirtsMilitaryLoot
* cbpClothesRackRectanglePantsMilitaryLoot
* cbpClothesRackRectangleShirtsMilitaryLoot
* cbpClothesRackWallPantsMilitaryLoot
* cbpClothesRackWallLongSleeveMilitaryLoot
* cbpClothesRackWallSweaterMilitaryLoot
* cbpClothesRackWallTShirtsMilitaryLoot
* cbpStoreShelfDoubleBottomShoesFullA
* cbpStoreShelfDoubleTopShoesFullA
* cbpStoreShelfSingleBottomShoesFullA
* cbpStoreShelfSingleTopShoesFullA

**Floor Pile** -  a lootable block and the randomHelper version also has a chance for a landmine to spawn.

* cbpClothesPileFloor

**Display Cases Deco** - Display cases that look like display cases but are non lootable.

* cbpDisplayCaseAmmoLeftBroken
* cbpDisplayCaseAmmoMiddleBroken01
* cbpDisplayCaseAmmoMiddleBroken02
* cbpDisplayCaseAmmoRightBroken

**Display Cases Lootable** - Display cases that look like display cases and are lootable But heavily reduced Loot returns.

* cbpDisplayCaseAmmoLeftBrokenA
* cbpDisplayCaseAmmoMiddleBrokenA
* cbpDisplayCaseAmmoMiddleBrokenB
* cbpDisplayCaseAmmoRightBrokenA

**Gun Rack Deco** - Gun racks that are just displays and not lootable. Also each rack is now personalised so the magazine rack only shows magazines and the armor rack only shows armor.

* cbpGunRackSmallMagazines
* cbpGunRackSmallArmor
* cbpGunRackLargeGuns01
* cbpGunRackLargeGuns02

**Gun Rack Lootable** - Gun racks that are lootable. Also each rack is now personalised so the magazine rack only shows magazines and the armor rack only shows armor.

* cbpGunRackSmallMagazinesA
* cbpGunRackSmallArmorA
* cbpGunRackLargeGunsA
* cbpGunRackLargeGunsB

**Vehicle Deco** - Player made vehicles can now be a display in your poi/s. No more having to go to the trader Hughs to get them. 

* cbpBicycleStatic [fixed the model offset that vanillas sinks into the ground]
* cbpMinibikeStatic
* cbpMotorcycleStatic
* cbp4x4Static
* cbpGyrocopterStatic
* cbpHelipad

**Traps and Turrets** - As the player made ones should never be used in a poi. These have had all the elctrical references removed and are just displays.

* cbpAutoTurret
* cbpShotgunTurret
* cbpBladeTrap
* cbpDartTrap
* cbpSwitch

**Benches** - A special request for all rotations added to the vanilla park benches. 

* cbpParkBenchA
* cbpParkBenchB

**Zombie/Animal Displays** - They Look like zombies, they twitch like zombies but are just deco blocks. A good use for them is in a lab in a containment field. [Credits to Valmar the Legend]

* cbpZombieArlene
* cbpZombieArleneFeral
* cbpZombieArleneRadiated
* cbpZombieMarlene
* cbpZombieMarleneFeral
* cbpZombieMarleneRadiated
* cbpZombiePartyGirl
* cbpZombiePartyGirlFeral
* cbpZombiePartyGirlRadiated
* cbpZombieNurse
* cbpZombieNurseFeral
* cbpZombieNurseRadiated
* cbpZombieJoe
* cbpZombieJoeFeral
* cbpZombieJoeRadiated
* cbpZombieSteve
* cbpZombieSteveFeral
* cbpZombieSteveRadiated
* cbpZombieTomClark
* cbpZombieTomClarkFeral
* cbpZombieTomClarkRadiated
* cbpZombieBusinessMan
* cbpZombieBusinessManFeral
* cbpZombieBusinessManRadiated
* cbpZombieBurnt
* cbpZombieBurntFeral
* cbpZombieBurntRadiated
* cbpZombieSpider
* cbpZombieSpiderFeral
* cbpZombieSpiderRadiated
* cbpZombieBoe
* cbpZombieBoeFeral
* cbpZombieBoeRadiated
* cbpZombieJanitor
* cbpZombieJanitorFeral
* cbpZombieJanitorRadiated
* cbpZombieMoe
* cbpZombieMoeFeral
* cbpZombieMoeRadiated
* cbpZombieLab
* cbpZombieLabFeral
* cbpZombieLabRadiated
* cbpZombieDarlene
* cbpZombieDarleneFeral
* cbpZombieDarleneRadiated
* cbpZombieYo
* cbpZombieYoFeral
* cbpZombieYoRadiated
* cbpZombieUtilityWorker
* cbpZombieUtilityWorkerFeral
* cbpZombieUtilityWorkerRadiated
* cbpZombieBiker
* cbpZombieBikerFeral
* cbpZombieBikerRadiated
* cbpZombieLumberjack
* cbpZombieLumberjackFeral
* cbpZombieLumberjackRadiated
* cbpZombieFemaleFat
* cbpZombieFemaleFatFeral
* cbpZombieFemaleFatRadiated
* cbpZombieFatHawaiian
* cbpZombieFatHawaiianFeral
* cbpZombieFatHawaiianRadiated
* cbpZombieMaleHazmat
* cbpZombieFatCop
* cbpZombieFatCopFeral
* cbpZombieFatCopRadiated
* cbpZombieSkateboarder
* cbpZombieSkateboarderFeral
* cbpZombieSkateboarderRadiated
* cbpZombieSoldier
* cbpZombieSoldierFeral
* cbpZombieSoldierRadiated
* cbpZombieWightFeral
* cbpZombieWightRadiated
* cbpZombieScreamer
* cbpZombieScreamerFeral
* cbpZombieScreamerRadiated
* cbpZombieMutated
* cbpZombieMutatedFeral
* cbpZombieMutatedRadiated
* cbpZombieDemolition
* cbpZombieSteveCrawler
* cbpZombieSteveCrawlerFeral
* cbpTimidAnimalStag
* cbpTimidAnimalDoe
* cbpTimidAnimalRabbit
* cbpTimidAnimalChicken
* cbpHostileAnimalBear
* cbpHostileAnimalZombieBear
* cbpHostileAnimalWolf
* cbpHostileAnimalCoyote
* cbpHostileAnimalDireWolf
* cbpHostileAnimalMountainLion
* cbpHostileAnimalZombieVulture
* cbpHostileAnimalZombieVultureRadiated
* cbpHostileAnimalZombieDog
* cbpHostileAnimalSnake
* cbpHostileAnimalBoar
* cbpHostileAnimalBossGrace

**Support/Radiation Blocks** - Blocks used for support (invisible) to radiate areas etc. 

* cbpRadiationWater 
* cbpHardAir
* cbpHardAirLadder
* cbpHardAirTallx20
* cbpHardAir3x9
* cbpFastCollapseSheet
* cbpBurnAir
* cbpHealthWaterPOI_BC01
* cbpPlateSwitchTrap
* cbpSlowAir
* cbpSlowAir2
* cbpTripWire
* cbpShockAir
* cbpHardAirTripWire
* cbpHardAirShock
* cbpHardAirHeal
* cbpHardAirVomitSplash

**Visual Effects Blocks** - Blocks that give visual effects but and player damage and others no player damage.

* cbpHardAirDark 
* cbpHardAirBlur
* cbpHardAirHot
* cbpHardAirHot2
* cbpHardAirCold
* cbpHardAirCold2
* cbpHardAirDistorted
* cbpHardAirGrey
* cbpHardAirRadiation
* cbpHardAirInfected
* cbpHardAirDrunk
* cbpHardAirShockLight

**Custom Boulder** - Can be used as a building block.

* cbpBoulderBuildingBlock

**Weapon/Tools/Vehicles/Drone Deco Blocks** - Weapon displays you can hang on your wall or around your poi. A tool wall in a hardware store to a weapon wall in a gun shop, to Drones in a drone factory and everything in between
 
* cbpSteelSpearPropWall
* cbpSteelSpearPropCtr
* cbpSteelSpearPropCtr_Wonky
* cbpCompoundCrossbowProp
* cbpCompoundCrossbowPropCtr
* cbpCompoundCrossbowPropCtr_Wonky
* cbpCompoundBowProp
* cbpCompoundBowPropCtr
* cbpCompoundBowPropCtr_Wonky
* cbpAxeSteelPropWall
* cbpAxeSteelPropCtr
* cbpAxeSteelPropCtr_Wonky
* cbpGunRifleT3SniperRiflePropWall
* cbpGunRifleT3SniperRiflePropCtr
* cbpGunRifleT3SniperRiflePropCtrOffset
* cbpGunRifleT3SniperRiflePropCtr_Wonky
* cbpM60PropWall
* cbpM60PropCtr
* cbpM60PropCtr_Wonky
* cbpAutoShotgunPropWall
* cbpAutoShotgunPropCtr
* cbpAutoShotgunPropCtr_Wonky
* cbpRocketLauncherPropWall
* cbpRocketLauncherPropCtr
* cbpRocketLauncherPropCtr_Wonky
* cbpTacticalARPropWall
* cbpTacticalARPropCtr
* cbpTacticalARPropCtr_Wonky
* cbpHuntingKnifePropWall
* cbpHuntingKnifePropCenter
* cbpHuntingKnifePropCtr_Wonky
* cbpMachettePropWall
* cbpMachettePropCenter
* cbpMachettePropCtr_Wonky
* cbpJunkDroneProp
* cbpJunkDroneGroundProp
* cbpJunkDroneOffsetProp
* cbpWoodenBowPropWall
* cbpWoodenBowPropCenter
* cbpWoodenBowPropCtr_Wonky
* cbpClawHammerPropWall
* cbpClawHammerPropCenter
* cbpClawHammerPropCtr_Wonky
* cbpNailgunPropWall
* cbpNailgunPropCenter
* cbpNailgunPropCtr_Wonky
* cbpFireaxePropWall
* cbpFireaxePropCenter
* cbpFireaxePropCtr_Wonky
* cbpIronPickaxePropWall
* cbpIronPickaxePropCenter
* cbpIronPickaxePropCtr_Wonky
* cbpSteelPickaxePropWall
* cbpSteelPickaxePropCenter
* cbpSteelPickaxePropCtr_Wonky
* cbpSteelShovelPropWall
* cbpSteelShovelPropCenter
* cbpSteelShovelPropCtr_Wonky
* cbpChainsawPropWall
* cbpChainsawPropCenter
* cbpChainsawPropCtr_Wonky
* cbpAugerPropWall
* cbpAugerPropCenter
* cbpAugerPropCtr_Wonky
* cbpWrenchPropWall
* cbpWrenchPropCenter
* cbpWrenchPropCtr_Wonky
* cbpRatchetPropWall
* cbpRatchetPropCenter
* cbpRatchetPropCtr_Wonky
* cbpImpactDriverPropWall
* cbpImpactDriverPropCenter
* cbpImpactDriverPropCtr_Wonky
* cbpBaseballBatPropWall
* cbpBaseballBatPropCenter
* cbpBaseballBatPropCtr_Wonky
* cbpSteelClubPropWall
* cbpSteelClubPropCenter
* cbpSteelClubPropCtr_Wonky
* cbpSteelSledgehammerPropWall
* cbpSteelSledgehammerPropCenter
* cbpSteelSledgehammerPropCtr_Wonky
* cbpWireToolPropWall
* cbpWireToolPropCenter
* cbpWireToolPropCtr_Wonky
* cbpSMG5PropWall
* cbpSMG5PropCenter
* cbpSMG5PropCtr_Wonky
* cbpMagnum44PropWall
* cbpMagnum44PropCenter
* cbpMagnum44PropCtr_Wonky
* cbpDesertVulturePropWall
* cbpDesertVulturePropCenter
* cbpDesertVulturePropCtr_Wonky
* cbpPistolPropWall
* cbpPistolPropCenter
* cbpPistolPropCtr_Wonky
* cbpDoubleBarrelPropWall
* cbpDoubleBarrelPropCenter
* cbpDoubleBarrelPropCtr_Wonky
* cbpPumpShotgunPropWall
* cbpPumpShotgunPropCenter
* cbpPumpShotgunPropCtr_Wonky
* cbpHuntingRiflePropWall
* cbpHuntingRiflePropCenter
* cbpHuntingRiflePropCtr_Wonky
* cbpLeverActionRiflePropWall
* cbpLeverActionRiflePropCenter
* cbpLeverActionRiflePropCtr_Wonky
* cbpAK47PropWall
* cbpAK47PropCenter
* cbpAK47PropCtr_Wonky
* cbpIronCrossbowPropWall
* cbpIronCrossbowPropCenter
* cbpIronCrossbowPropCtr_Wonky
* cbpPaintBrushPropWall
* cbpPaintBrushPropWallPropCenter
* cbpPaintBrushPropWallPropCtr_Wonky
* cbpPaintBrushPropWalloffsetCtr_Corner
* cbpFlameThrowerProp
* cbpJunkSledgeProp
* cbpJunkTurretProp
* cbpJunkTurret2Prop
* cbpStunBattonPropWall
* cbpStunBattonPropCenter
* cbpStunBattonPropCtr_Wonky
* cbpMotorCycleProp [No Hoist]
* cbp4x4Prop [No Hoist]

**Sparkly Stuff** - as the name suggest special effect blocks. 

* cbpSparklyBlockLarge
* cbpSparklyBlockZomLeft
* cbpSparklyBlockZomRight
* cbpSparklyBlockDroneBeamAttack
* cbpSparklyBlockDroneBeam
* cbpSparklyBlockDroneBeamOffset
* cbpSparklyBlockDroneHealPlayer
* cbpSparklyBlockDroneHealBeam
* cbpSparklyBlockSmall
* cbpVomitBulbProp
* cbpRadBulbProp
* cbp_SparklySmallFlame
* cbp_SparklySmallFlameOffset
* cbpdecoMannequinFemaleGold
* cbpHardAirClaymore
* cbpHologramZombieRadiatedCop
* cbpRadiatedCopClaymore
* cbpHardAirVomitClaymoreHelper
* cbpHardAirVomitClaymore
* cbp_SparklyBlockLargeOff

**Mid Century Bathroom Objects** - Go back to the 50s with these coloured variation of bath sets. 

* cbpAvacadoToiletOpen
* cbpSalmonToiletOpen
* cbpRoseToiletOpen
* cbpTurquoiseToiletOpen
* cbpAvacadoToiletClosed
* cbpSalmonToiletClosed
* cbpRoseToiletClosed
* cbpTurquoiseToiletClosed
* cbpAvacadoToiletClosedIndustrial
* cbpSalmonToiletClosedIndustrial
* cbpRoseToiletClosedIndustrial
* cbpTurquoiseToiletClosedIndustrial
* cbpAvacadoUrinal
* cbpSalmonUrinal
* cbpRoseUrinal
* cbpTurquoiseUrinal
* cbpAvacadoSinkWallMounted
* cbpSalmonSinkWallMounted
* cbpRoseSinkWallMounted
* cbpTurquoiseSinkWallMounted
* cbpAvacadoSinkCounterMounted
* cbpSalmonSinkCounterMounted
* cbpRoseSinkCounterMounted
* cbpTurquoiseSinkCounterMounted
* cbpAvacadoSinkCounterMountedOffset
* cbpSalmonSinkCounterMountedOffset
* cbpRoseSinkCounterMountedOffset
* cbpTurquoiseSinkCounterMountedOffset
* cbpAvacadoSinkPedestal
* cbpSalmonSinkPedestal
* cbpRoseSinkPedestal
* cbpTurquoiseSinkPedestal
* cbpAvacadoBathtubEmpty
* cbpSalmonBathtubEmpty
* cbpRoseBathtubEmpty
* cbpTurquoiseBathtubEmpty
* cbpAvacadoBathtubGore
* cbpSalmonBathtubGore
* cbpRoseBathtubGore
* cbpTurquoiseBathtubGore
* cbpAvacadoBathtubClawFoot
* cbpSalmonBathtubClawFoot
* cbpRoseBathtubClawFoot
* cbpTurquoiseBathtubClawFoot

**Custom Trees with Advanced rotation** - Trees that can be placed laying down. 

* cbpTreeFallenMountainPine19m
* cbpTreeFallenWinterPine6m
* cbpTreeFallenBurntMed
* cbpTreeFallenDry21m
* cbpTreeFallenDeadTree01
* cbpTreeFallenPlainsTree2
* cbpTreeFallenMountainPine27m
* cbpTreeFallenMountainPine48m
* cbpTreeFallenPineBurntLrg
* cbpTreeFallenBurntFullMed
* cbpTreeFallenOakMed01
* cbpTreeFallenSpookyLarge
* cbpTreeFallenSpookySmall
* cbpTreeFallenSpookyMed

**Wonky Trees** - Trees that align with ground slope. 

* cbpTreeFallenMountainPine19m_Wonky 
* cbpTreeFallenWinterPine6m_Wonky
* cbpTreeFallenBurntMed_Wonky
* cbpTreeFallenDry21m_Wonky
* cbpTreeFallenDeadTree01_Wonky
* cbpTreeFallenPlainsTree2_Wonky
* cbpTreeFallenMountainPine27m_Wonky
* cbpTreeFallenMountainPine48m_Wonky
* cbpTreeFallenPineBurntLrg_Wonky
* cbpTreeFallenBurntFullMed_Wonky
* cbpTreeFallenOakMed01_Wonky
* cbpTreeFallenSpookyLarge_Wonky
* cbpTreeFallenSpookySmall_Wonky
* cbpTreeFallenSpookyMed_Wonky

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

**MP Logue** - Contributed a number of interesting blocks with special effects
and blocks that assist with structural integrity.

**Pille** - Contributed the Super Brush tool/item.

**Robfly** - Contributed game events.

**Stallionsden** - Collaborated on various loot settings, inspired Landmine,
Vending Machine and ATM blocks, contributed the Mushroom Helper. Then added
a truly massive number of blocks and placeholders.

**ZZTong** - Contributed various shipping crate blocks and helpers,
contributed empty and low-loot block variations, contributed the Delos (West
World) blocks, worked on a variety of offset block variations.
