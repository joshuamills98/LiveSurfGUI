from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib import cm


def get_temp_colour(temp):
    """Get the colour of a temperature in the form of rgba"""
    norm = Normalize(vmin=0, vmax=30)
    map = ScalarMappable(norm=norm, cmap=cm.cool)
    rgba = map.to_rgba(temp)
    return rgba_to_hex(rgba)


def rgba_to_hex(rgb_color):
    [r, g, b, a] = rgb_color
    r = round(r*255)
    g = round(g*255)
    b = round(b*255)
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255

    r = hex(r).lstrip('0x')
    g = hex(g).lstrip('0x')
    b = hex(b).lstrip('0x')
    # re-write '7' to '07'
    r = (2 - len(r)) * '0' + r
    g = (2 - len(g)) * '0' + g
    b = (2 - len(b)) * '0' + b

    hex_color = '#' + r + g + b
    return hex_color


if __name__ == '__main__':
    rgb_input = (0.7893886966551327,
                 0.2768166089965398,
                 0.2549019607843137,
                 1.0)
    hex_output = rgba_to_hex(rgb_input)
    print(hex_output)
