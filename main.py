MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
def pair_number_to_colors(pair_number):
    if not 1 <= pair_number <= len(MAJOR_COLORS) * len(MINOR_COLORS):
        raise Exception('Pair number out of range')
    major_index, minor_index = divmod(pair_number - 1, len(MINOR_COLORS))
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
def colors_to_pair_number(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Color not found')
    return major_index * len(MINOR_COLORS) + minor_index + 1
if __name__ == '__main__':
    assert pair_number_to_colors(4) == ('White', 'Brown')
    assert pair_number_to_colors(5) == ('White', 'Slate')
    assert colors_to_pair_number('Black', 'Orange') == 12
    assert colors_to_pair_number('Violet', 'Slate') == 25
    assert colors_to_pair_number('Red', 'Orange') == 7
    print('Done :)')
