The branch `blender2.9` is now loading in  blender 2.9.
The main workflow to create and export robot models
should work. However, there are still a few todos left:

- [possibly done] search for all matrix multiplications:
  vector*vector
  quaternion*vector
  matrix*matrix
  ...
  ->
  vector@vector
  quaternion@vector
  matrix@matrix
  ...
- rewrite lod handling
- how to handle ambient and emission colors?
- update texture handling
- collect all issues
- update add motor and controller operator to not create new objects
- fully integrate cli-phobos starting with io
- [done] replace layer handling by collections
- [done] drawing into 3d_view via opengl
- [done] autmatic installation of python dependencies in blender
- [done] make compatible with blender3
