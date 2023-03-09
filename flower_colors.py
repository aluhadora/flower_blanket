import random

def main():

    all_colors = [
        'Admiral',
        'Ivory',
        'Himalayan',
        'Canyon',
        'Bee Pollen',
        'Dijon',
        'Tourmaline',
        'Caper',
        'Peacock',
        'Stonewash',
        'Amethyst',
        'Raisin',
        'Satellite',
        'Bone',
        'Nutmeg',
        'Moonbeam',
        'Provence',
        'Thunder',
        'Badlands',
        'Channel Islands',
        'Wolf Trap',
        'Indiana Dunes'
    ]

    allowable_colors, color_counts = build_allowable_colors(all_colors)
    print_colors_dictionary(allowable_colors)
    print_counts_dictionary(color_counts)

def build_allowable_colors(all_colors):
    eligible_colors = all_colors.copy()

    # Define a dictionary of allowable middle colors for each petal color
    allowable_colors = {}
    color_counts = {}
        
    for petal_color in all_colors:
        color_counts[petal_color] = 0

    shuffled = all_colors.copy()
    random.shuffle(shuffled)

    for petal_color in shuffled:
        eligible_colors_except_current = eligible_colors.copy()
        if (petal_color in eligible_colors):
            eligible_colors_except_current.remove(petal_color)

        random_color = random.sample(eligible_colors_except_current, 6)
        for middle in random_color:
            color_counts[middle] += 1
            if (color_counts[middle] > 6):
                eligible_colors.remove(middle)

        allowable_colors[petal_color] = random_color

    return allowable_colors, color_counts

def print_colors_dictionary(dict):
    for petals, middle in dict.items():
        print("{:<20} {}".format(petals, middle))

def print_counts_dictionary(dict):
    for color, count in dict.items():
        print("{:<20} {}".format(color, count))


if __name__ == "__main__":
    main()
    


    # for petal_color in all_colors:
    #     # how many times does this color show up in all of the middle items
    #     color_counts[petal_color] = 0
    #     # loop through all of the "middle colors" and add 1 each time we see the petal color
    #     for primary, middle_colors in allowable_colors.items():
    #         for middle_color in middle_colors:
    #             if (middle_color == petal_color):
    #                 color_counts[petal_color] += 1
    #             if (color_counts[petal_color] > 8):
    #                 allowable_colors[primary]