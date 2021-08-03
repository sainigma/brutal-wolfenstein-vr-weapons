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