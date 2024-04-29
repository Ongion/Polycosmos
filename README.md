# Polycosmos
Polycosmos is a mod for the game Hades, which gives it integration with Archipelago Multiworld. Right now Polycosmos is in version: 
0.10.0 and up to this version it possesses the feature detailed below:

Modes for heat:
- Reverse Heat: Start the game with high pacts of punishments. Pact of punishment reductions are items in the item pool.
- Minimal Heat: Start the game with high pacts of punishments. Pact of punishments can never be set below the initial settings. Made for the brave.
- Vanilla: Same as the standard game.

Items:
- Pact of Punishment down: an item that turns down the level of pact of punishment. Note the game may load this effect
on the next room, biome or run.

- Keys, Darkness, Gemstones, Diamonds, Titan Blood, Nectar and Ambrosia as filler items.

- Weaponsanity: weapons can be randomized as items in the multiworld. Buying them counts as a location check.

- Hidden Aspects: hidden aspects can be randomized as items in the multiworld, needing to get those before being able to buy them on Hades. Helps make them more balanced.

- Keepsakesanity: keepsakes can randomized as items in the multiworld. Getting them count as a location check.

- Storesanity: all important items from the store can be randomized in the multiworld. Buying them from the store counts as a location check.

- FateSanity: The majority of the fated list can be used as a location for the multiworld. Completing them and cashing them grants the reward behind them.

Location Modes: Cleaning rooms will give location checks. Two modes can be chosen for how this works: 
- Location based: Beating any room with a certain depth on the run counts as a location for the AP. Beating the same room twice won't give another item.
- Score based: Beating a room with a certain depth on a run gives score according to its depth. So beating the fifth room on the run gives 5 points. The twenty-th gives 20 points and so on.  Beating your high score level counts as an item, and then it subtracts that amount of score. So if your highest score is 19, you have 17 points and beat room 6: this will give location "ScoreClear020" and leave you with 17+6-20=3 points. You can adjust how many locations are behind the score system, with the limit being 1000. Note this will give a REALLY
long game.
- Location based for weapon: Beating any room with a certain depth on the run, which each weapon, counts as a location for the AP. Beating the same room twice with the same weapon wont give another item.


Settings:
- Number of Pact of Punishments: tweak how high each pact of punishment starts, and so how many of these items are in the pool.
- Value of filler items: tweak how much currency each filler item gives you. Can be used to turn off filler items
- Number of locations behind the scoring system in the score-based mode.
- Keepsakesanity: Keepsakes are shuffled into the item pool, and giving the first nectar to each NPC becomes a location. Excludes Hades and Persephone. NPCs can be befriended after obtaining their corresponding item and location check as normal.
- Storesanity: Important store items are shuffled into the item pool, and buying them from the store becomes location instead. The store slots have logic to them, you can see below the details.
- Weaponsanity: Weapons can be shuffled into the item pool, buying them from the store becomes a location.
- FateSanity: Fated lists are location for the AP world.

Victory conditions tweaks:
- Minimum number of victories against Hades before finishing a run counts as victory.
- Mininum number of victories with different weapons before finishing a run counts as a victory.
- Minimum number of keepsakes before finishing a run counts as a victory.
- Minimum number of fated lists completed before finishing a run counts as a victory.

Traps:
-Add some traps into the item pool to keep you on your toes.
  
Quality of Life:
- Contractor has some extra upgrades available to buy from the start. Fated list is available from the start. The lounge is available from the start. Brooker is available from the start. Demeter can appear from the second run.
- The order in which Extreme Measures affect bosses can be reversed. So the first level affects Hades (instead of the Furies), the second one the heroes and so on. Can be toggled from the .yaml, but it is recommended for a more balanced experience.
- To avoid deaths in Greece counting for deathlink.
- The ability to choose the initial weapon for Zagreyus. Also allows randomized option.
- Weapons now getting bought from the house contractor, not from the weapon storage. Needed for getting weaponsanity working.
- All aspects of weapons can be bought once you unlock the weapon (except for the hidden ones if those are in the item pool).

# Requirements
- Have Hades installed (duh!). Download what version you need of [ModImporter](https://github.com/SGG-Modding/ModImporter/releases/tag/1.5.2) and put modimporter.exe in your Hades/Content folder.
- Have [ModUtils](https://github.com/SGG-Modding/ModUtil/releases) installed. For this download the latest version from the Github link, unzip that folder on Hades/Content/Mods and then Open modimporter.exe in you Hades/Content folder. Note you might need to create the Mods folder.
- Have [StyxScribe without the REPL](https://github.com/NaixGames/StyxScribeWithoutREPL) installed, without the REPL part. For this download the mod from the link and put StyxScribe.py and SubsumeHades.py in your Hades folder, put the folders StyxScribe and StyxScribeShared in Hades/Content/Mods folder. Run modimporter.exe. If you have Python installed you can check everything is working fine here by executing SubsumeHades.py in Hades folder. That should open Hades.
- Now you can use the modimporter.exe to install the Polycosmos mod folder in this repository. That is, put the Polycosmos folder in Hades/Content/Mods folder and open modimporter.exe. At this point, your Mods folder should look like this:

![](https://github.com/NaixGames/Polycosmos/blob/main/FolderStructure.png?raw=true)
- Copy hades.apworld into your lib/worlds folder inside your Archipelago install.
- After doing this you should be able to generate and play multiword with Hades! (Note that generating Hades games on the website is still not supported. You need to generate locally. Ask in Discord if you need help
for this step. To start you can use the Template.yaml, which also includes some explanation of the settings.)

NOTE: up to the time of writing this mod does not guarantee any type of compatibility with other Hades mods. You have been warned!

# How to use Polycosmos

- To use Polycosmos launch the client from the Archipelago Launcher. If everything is working correctly this should open a window to search for your StyxScribe.py file, in your Hades folder (the standard steam path being C:\Program Files\Steam\steamapps\common\Hades ). Select that file and this should open Hades and the Archipelago client. Note the Archipelago client is a different window that looks like this:
  ![](https://github.com/NaixGames/Polycosmos/blob/main/ArchipelagoClient.png?raw=true)
- Before starting a file, connect to your Archipelago server using the client as you would do with any other AP game. Play the game and have fun ;).

# Credits

Everyone at the Hades modding discord. They have been a massive help. Especially Magic_Gonads and PonyWarrior for answering my pestering questions. Also, the credit of StyxScribe is theirs and only theirs.

DoesBoKnow for proposing the multiworld and providing tons of resources and testing. Also for being a contributor since 0.4.0, contributing in some capacity to almost all the features from that point forward.

The AP discord and all the people in the Hades subthread have pitched in with ideas and helped keep me motivated. That includes but is not limited to, Flore for proposing the “reversed heat” idea (which was simple enough to start implementing almost right away, which made this much more bearable) and Sylvris for helping add proper APWorld support. Also thanks to all the testers for providing information about the bugs they encountered. I could 
have not made this without you.

Also, thanks to RobinLSL for having the patience to report a large number of typos.

# Bugs 

A known issue is that some changes in heat level only take effect when starting the next room, biome or run starts. That is how Hades works and not much we can do about that.

You see some weird debug messages while playing with keyboard and mouse. To avoid this go to your main Hades folder, and in there open StyxScribe.py. Go to line 26 and in there change "DebugDraw=true" to "DebugDraw=false". In a future version, this will be disabled permanently.

Any other bug is not expected and reporting helps a ton :).

# StoreSanity logic

In StoreSanity the "spots" in the store are tied to a location in the original game. You can see the logic for each location below. Note that when obtaining items that have multiple levels, which are managed progressively (so if you get InfernalTrove3Item first that will appear as InternalTrove1Item in your game and be managed as such). 

- FountainUpgrade1Location: Requires FountainTartarusItem

- FountainUpgrade2Location: Requires FountainUpgrade1Item

- FountainAsphodelLocation: Requires FountainTartarusItem, Arriving to Asphodel, KeepsakeRack.

- FountainElysiumLocation: Requires FountainAsphodelItem, Arriving to Elysium, KeepsakeRack.

- UrnsOfWealth1Location: Requires FountainTartarusItem

- UrnsOfWealth2Location: Requires UrnsOfWealth1Item

- UrnsOfWealth3Location: Requires UrnsOfWealth2Item

- InfernalTrove1Location: Requires FountainElysiumItem, InfernalTrove1Item, KeepsakeRack.

- InfernalTrove2Location: Requires FountainElysiumItem, InfernalTrove2Item, KeepsakeRack, DeluxeContractorDeskItem.

- DeluxeContractorDeskLocation: Requires ElysiumFountainItem, CourtMusicianSentenceItem

- VanishersKeepLocation: Requires DeluxeContractorDeskItem

- FishingRodLocation: Requires getting to Temple of Styx, FountainTartarusItem.

- CourtMusicianSentenceLocation: Requires getting to Asphodel, FountainTartarusItem.

- CourtMusicianStandLocation: Requires CourtMusicianSentenceItem and the Scrying Pool (which is not an AP item).

- PitchBlackDarknessLocation, FatedKeysLocation, BrilliantGemstonesLocation, VintageNectarLocation, DarkerThirstLocation: all require DeluxeContractorDeskItem

# Other logic facts

- You get access to the second side of the mirror after getting 300 Darkness and talking to Nyx

- In keepsakesanity the multiworld expects you to have the keepsake item before getting the keepsake location for each Olympian god.

- You need to talk to Achilles a couple of times to get the Codex. Speak to him after each run and you should get it between runs 3 and 5.

- The Codex tells you which NPCs still have a check behind giving them nectar.

# How this mod works

There might be a case in which you want to collaborate to improve this multiworld or want to adapt this to bring other games to Archipelago.
If that is the case; great! You can always put in contact with me at my discord. In any case, here is a broad overview of how this mod is set up.

First, there are 3 ingredients; Polycosmos mod, StyxScribe and the ArchipelagoClient. Broadly; the Polycosmos
mod is what can directly influence the game (give Zag items, record when locations have been reached, etc.). The Archipelago Client
is what Communicate with the AP Server, and can communicate messages to other clients (for example "HadesPlayer reached a location" or "HadesPlayer have received an item").
The StyxScribe is what can communicate the Polycosmos mod with the ArchipleagoCLient.

- Polycosmos mod works like a standard Hades mod. It is written in .lua with some stripped-down capabilities (in particular no access to
"require" or related commands). Up to the time of 0.5.0 compromised a bunch of modules, which we explain a few here:

PolycosmosEvents: reacts to certain important events in the game (location reached, game loaded) by notifying other modules.
PolycosmosHeatManager: manages the current Heat level according to the settings and items it receives
PolycosmosItemManager: manages the reception of filler items
PolycosmosMessages: It is the module that prints messages to the player.
PolycosmosUtils: Contains functions that are useful to manage or parse data, but are agnostic to the mod structure, so do not fit in any other library.

Note that while some modules could be mashed together, these different functionalities have been split to be able to grow this in the most modular way possible.

- StyxScribe is a Hades mod that allows communication between .lua and .py modules. It uses a Hook system with strings;
ie, Allows the execution of certain functions in the modules each time a message with a certain prefix has been sent in the console.
Is that by using these hooks that can communicate between Polycosmos and the Archipelago Client.

As a side note, you might be considering why we even use StyxScribe and not import a .dll to use for the APClient (which already
exists for game running in .lua). The reason is simple: Hades runs on a Lua compiler that does not allow the manual import of external files.
It is why we use StyxScribe; to bypass this limitation as painlessly as possible. If other ways are found to also
overcome this, another implementation of this mod might be possible which directly implements the client or other functionality inside Hades
itself.

- Archipelago Client is a .py app that can communicate with an Archipelago server to send and receive items. This server also
deals with game randomization (ie, what item corresponds to which other player item).
