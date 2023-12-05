from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("jersey2.jpg")
# print(ct.get_color(quality=5))

dominant_color = ct.get_color(quality=1)

# plt.imshow([[dominant_color]])
# plt.show()
number_color = int(input("number of dominant color need to be shown:"))

palette = ct.get_palette(color_count=number_color)
plt.imshow([[palette[i] for i in range(number_color)]])
plt.show()

for color in palette:
    #
    print(f"RGB color: {color}")
    print(f"hex color: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(f"HSV color: {colorsys.rgb_to_hsv(*color)}")
    print(f"HLS color: {colorsys.rgb_to_hls(*color)}")

