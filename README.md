# Brutal Wolfenstein VR Weapons mod

![GitHub Logo](/docs/titlecard.png)

## Table of Contents

- [Description](#description)
  - [Supported weapons](#supported-weapons)
- [Installation and Usage](#installation-and-usage)
- [Documentation](#documentation)

## Description

This is a mod for ZioMcCall's [Brutal Wolfenstein 3D mod](https://forum.zdoom.org/viewtopic.php?f=19&t=48035) that replaces the weapon sprites with animated 3d models. It also modifies the weapon scripts for general VR comfort and compatibility with [GZDoomVR](https://github.com/hh79/gzdoomvr) project.

So basically it's a mod for a mod and a specific gzdoom fork, what a wild intersection.

### Supported weapons:

 - [x] P08 Luger
 - [x] Colt 1911A1
 - [x] MP40
 - [x] Thompson M1A1
 - [x] Kar98k
 - [x] M1 Garand
 - [x] STG 44
 - [x] Winchester M12 Trench Gun
 - [x] MG-42
 - [x] Flammenwerfer 41
 - [ ] Panzershreck (Grenades as placeholder)
 - [ ] Laser rifle (FmW 41 as placeholder)
 - [ ] Browning BAR (Garand as placeholder)
 - [ ] Chaingun (MG42 as placeholder)
 - [ ] PPSh-41 (Thompson M1A1 as placeholder)

While some weapons are still missing, the game is fully playable, as the missing guns function as pickups for existing weapons. Akimbo and melee weapons were not ported (although melee weapons are still available as sprites), as they don't really work in VR imo.

## Installation and Usage

  Downloads:
  - GZDoomVR https://github.com/hh79/gzdoomvr/releases/
  - ZMC-BWFinal.zip https://www.moddb.com/mods/brutal-wolfenstein-3d/downloads/zmc-bwfinal
  - BW-VR-Weapons.zip https://github.com/sainigma/brutal-wolfenstein-vr-weapons/releases
  - brutal-wolfenstein-vr-weapons.bat https://github.com/sainigma/brutal-wolfenstein-vr-weapons/blob/master/brutal-wolfenstein-vr-weapons.bat

  1. Extract GZDoomVR to a folder
  2. Extract ZMC-BWFinal.**pk3** to the GZDoomVR folder
  3. Move BW-VR-Weapons.zip and brutal-wolfenstein-vr-weapons.bat to the GZDoomVR folder
  4. Add original Doom2 wad to the GZDoomVR folder

  Your game folder should now look like:

    GZDoomVR
    ├── gzdoom.exe
    ├── ZMC-BWFinal.pk3
    ├── BW-VR-Weapons.zip
    ├── brutal-wolfenstein-vr-weapons.bat
    ├── DOOM2.WAD
    └── ...

  5. Run brutal-wolfenstein-vr-weapons.bat, start the game from launcher with Doom2 selected, modify reload and grenade keybinds in in-game settings, play

  Note. Autoreload is disabled by default. To enable it, edit brutal-wolfenstein-vr-weapons.bat and set sv_autoreload to 1.

## Documentation

If anyone else is interested in porting 3d weapons to old gzdoom-mods, [here are some pointers](./docs/tutorial.md) I wrote based on this project.

## Credits

GZDoomVR by a lot of people, latest release by hh79

Original Brutal Wolfenstein 3D mod and weapon scripts by ZMC

Script modifications for VR, weapon models, textures and animations by me.

## Links

[Brutal Doom VR Weapons](https://github.com/ajantaju/br_vr) by ajantaju, a similar project that supports Brutal Doom, Brutal Doom 64 and Heretic

[Showcase for the german weapons]() at Artstation

[Showcase for the US weapons]() at Artstation