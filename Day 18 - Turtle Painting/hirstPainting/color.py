import colorgram
colors = colorgram.extract("colors.jpg",20)
color_list = []
for color in colors:
    x = color.rgb
    a = x.r
    b = x.g
    c = x.b
    color_list.append((a,b,c))
print(color_list)