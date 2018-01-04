PRESET_COLORS = {'gold':'#ffd700', 'spring_green':'#00ff7f', 'floral_white':'#fffaf0', 'light_gray':'#d3d3d3'}

def parse_color(color):
    if color.lower() in PRESET_COLORS:
        color = PRESET_COLORS[color.lower()]
    color_value = color[1:] if len(color) == 7 else ''.join(i * 2 for i in color[1:])
    try:
        result = {'r' : int(color_value[:2], 16), 'g' : int(color_value[2:4], 16), 'b' : int(color_value[4:], 16)}
        return result
    except ValueError:
        return {}

if __name__ == '__main__':
    print(parse_color('light_gray'))
    print(parse_color('#445520'))
    print(parse_color('light_gray'))

#---------------------------

def diamond(n):
    if n % 2 == 0 or n < 1:
        return None

    result = []
    middle = n // 2 + 1
    print(middle)
    for i in range(0, middle):
        star_count = n - (i * 2)
        length = star_count + i
        line = ("*" * star_count).rjust(length)
        result.append(line)
        if i > 0:
            result.insert(0, line)

    return "\n".join(result) + "\n"

if __name__ == "__main__":
	print(diamond(5))
	print(diamond(7))
	print(diamond(13))