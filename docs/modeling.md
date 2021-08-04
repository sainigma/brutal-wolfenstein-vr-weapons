WORK IN PROGRESS

- modeling
  - md3 format
  - model origin is the origin of the player viewport -> put the weapon at a distance (grip at ~30cm from origin)
  - blender X+ is forward
  - barrel should coincide with X+
  - it's easier to model with unit scale turned to metric. use unit scale of 0.01
- animating
  - vertex animations
  - use either shapekeys or bones to animate
- export
  - modern blender has no support for md3 export
  - requires an ancient version of blender (2.79)
  - 2.79 is required only for export, use append to import your model and armature
  - the texture has to be set in ancient blender before export
  - triangulate the model before exporting
- scripting
  - map keyframes to sprite id's with modeldef

## Workflow

- find the [DECORATE](https://zdoom.org/wiki/DECORATE) script file for the weapon you want to model. the decorate scripts are listed in DECORATE.txt -file. a single script can contain logic for many actors, so finding the correct file might take some work if the project is oddly organized.

The actor is defined like:

    Actor ActornameHere:ActorType {
      //actor properties are defined here
      ...
      States {
        Function:
          ABCD A 0 A_Example

        NextFunction:
          TNT1 A 0 A_Example
          Goto Function
      }
    } 

The actor is basically a state machine, and in an optimal case, you only have to find out which sprites are used in each state function.

Using STG44's DECORATE as an example, here are the states that define a reload:

    Reload:
    
    	//Checks if the inventory still has ammo, if not, the conditional jump removes rest of the actions from execution and moves to the function pointed to
    	TNT1 A 0 A_Takeinventory("Reloading",1)
    	TNT1 A 0 A_JumpIfInventory("STGAmmo",30,"InsertBullets")
    	TNT1 A 0 A_JumpIfInventory("KARClip",1,3)
    	Goto NoAmmo
    	
      //Weapon moves to reload position
    	TNT1 AAA 0
    	ZSTR ABCDEF 1

      //Magazine ejection
    	ZSR2 ABC 1
    	ZSR2 D 2
    	TNT1 a 0 A_FireCustomMissile("MP44EmptyClip",-5,0,8,-4)
    	TNT1 a 0 a_playsound("mp441")

      //Magazine insertation
    	ZSR3 ABCDEFGHI 2
    	TNT1 a 0 a_playsound("mp442")
    	TNT1 A 0 A_TakeInventory("STGMAGCOUNT",30)
    	
      //If the magazine wasn't empty, the charging handle animation is skipped
    	TNT1 A 0 A_JumpIfInventory("STGAmmo",1,"TacticalReload")
    	
      //Charging handle animation
    	ZSR4 ABC 1
    	ZSR4 D 3
    	TNT1 A 0 A_PlayWeaponSound("STEND1")
    	ZSR4 EFGHI 1
    	
    	Goto FinishReload
    	
    TacticalReload:
    	Goto FinishReload
    	
    FinishReload:
      //Weapon animation to reload position is played on reverse
    	ZSTR FEDCBA 1

Each action consists of a four letter ID, frame index, hold time and an optional function. For example, ZSTR A 1 would change the current sprite to a file named ZSTRA, and hold it for a single frame. ZSTR ABCDEF 1 on the other hand, would animate from sprites ZSTRA to ZSTRF and hold each sprite for a single frame. 

TNT1 is a null sprite reference, so it doesn't change the active sprite. It's used for timing, and triggering special actions, like conditional jumps, inventory management, sound effects and so on.

Once you have reviewed the decorate script for the weapon, you should end up with an outline and a plan on how to animate the weapon:

    stg44:

    ZSTG A(default state) B(fire) CDEF(recoil)
    ZSTS ABCDEFGHIJKL (weapon intro)

    ZSTR ABCDEF (reload intro)
    
    ZSR2 ABCD (magazine ejection)
    ZSR3 ABCDEFGHI (magazine insertation)
    ZSR4 ABCD (charging handle pull) EFGHI (charging handle release)
    
    ZSTS 12fr
    ZSTG 6fr
    ZSTR 6fr
    ZSR2 9fr
    
You can now animate the weapon in blender, using the sprite outline as a reference for strip lengths.

- NLA strips are great
- Animating is pretty freeform due to it being baked as a vertex animation (think crash bandicoot)
- Due to previous, high-poly models and long animations will produce a HUGE file
- Also due to point preceding previous, you can also bake shapekeys to animations! (think crash/roger rabbit/looney toons etc.)
- First frame should be the default state, since rest of the frames are computed based on it. Having the model at a really odd position and an angle at the start will produce floating point rounding errors in rest of the frames.
- The model is tied to the spritesheet using modeldef: define your model and how each frame ties to a specific sprite
- This whole process can be done in reverse order if you're willing to modify the decorate script for the weapon: modeldef doesn't care if the ID you're referencing to exists or not, as long as it's unique/unused. A safe bet is to repurpouse the sprite id's used by the weapon you're modding.