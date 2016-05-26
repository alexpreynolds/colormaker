# colormaker
Starting with a seed color and desired number of colors, returns an array of colors which are roughly divided through the HSV color space.

To use, specify an RGB triplet as a braced list, where red, green and blue values are between 0 and 255, as well as the desired number of colors. The result is returned to standard output as hexadecimal values of the original starting color and additional calculated colors:

```
$ ./colormaker.py --seed="[222,127,5]" --number=5
#de7f05
#4005de
#09de05
#de0548
#0587de
```

To get RGB triplets or RGBA quartets as standard output, add the `--asRGB` or `--asRGBA` option:

```
$ ./colormaker.py --seed="[222,127,5]" --number=5 --asRGB
rgb(222,127,5)
rgb(64,5,222)
rgb(9,222,5)
rgb(222,5,72)
rgb(5,135,222)
```