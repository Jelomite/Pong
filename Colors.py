# RGB format
pomegranate = (192, 57, 43)
alizarin = (231, 76, 60)
pumpkin = (211, 84, 0)
carrot = (230, 126, 34)
orange = (243, 156, 18)
sun_flower = (241, 196, 15)
emerald = (46, 204, 113)
nephritis = (39, 174, 96)
turquoise = (26, 188, 156)
green_sea = (22, 160, 133)
peter_river = (52, 152, 219)
belize_hole = (41, 128, 185)
amethyst = (155, 89, 182)
wisteria = (142, 68, 173)
wet_asphalt = (52, 73, 94)
midnight_blue = (44, 62, 80)
concrete = (149, 165, 166)
asbestos = (127, 140, 141)
silver = (189, 195, 199)
clouds = (236, 240, 241)
pure_white = (255, 255, 255)
pure_black = (0, 0, 0)


def mix(color1, color2):
    r = (color1[0] + color2[0]) / 2
    g = (color1[1] + color2[1]) / 2
    b = (color1[2] + color2[2]) / 2
    return r, g, b


def negative(color):
    r = color[0]
    g = color[1]
    b = color[2]
    return 255 - r, 255 - g, 255 - b
