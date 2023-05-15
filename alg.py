def get_male_bodyshape(chest, waist, hip):
    chest = int(chest)
    waist = int(waist)
    hip = int(hip)

    # # Chest is at least 5 percent bigger than Hip measurement.
    # # oval shape is also known as apple
    # if float(chest) * float(1.05) > hip:
    #     return 'Oval/Apple'
    #
    # # Chest is at least 5 percent smaller than Hip measurement.
    # # trapezoid shape is also known as inverted triangle
    # elif float(chest) * float(1.05) < hip:
    #     return 'Trapezoid/Inverted Triangle'
    #
    # # Chest and Hip measurements are within 5 percent of each other.
    # # rectangle shape is also known as straight
    # elif float(chest) * float(1.05) == hip:
    #     return 'Rectangle/Straight'


def get_female_bodyshape(bust, waist, hip):
    bust = int(bust)
    waist = int(waist)
    hip = int(hip)

    # Waist is at least 25 percent smaller than Hip AND Bust measurement.
    # hour glass is also known as curvy shape
    if float(waist) * float(1.25) <= bust & hip:
        return 'Hourglass'

    # Hip measurement is more than 5 percent bigger than Bust measurement.
    # pear shape is also known as triangle
    elif float(hip) * float(1.05) > bust:
        return 'Pear/Triangle'

    # Hip measurement is more than 5 percent smaller than Bust measurement.
    # apple shape is also known as inverted triangle
    elif float(hip) * float(1.05) < bust:
        return 'Apple/Inverted Triangle'

    # Hip and Bust measurements are within 5 percent of each other.
    # rectangle shape is also known as straight
    elif float(hip) * float(1.05) == bust:
        return 'Rectangle/Straight'


bust = 34
waist = 24
hip = 36
output = get_female_bodyshape(bust, waist, hip)
print(output)
if output == 'Hourglass':
    # Form-fitting jersey knits
    # Wrap tops
    # Peplum blouses
    # Tailored tops with ample room in the chest
    # Anything with a V-neck, round neck or boat neck
    # Dresses
    pass
elif output == 'Pear/Triangle':
    # Plunging V - necks in any silhouette
    # Cowl necks
    # Bell-sleeves
    # Scoop neck
    pass
elif output == 'Apple/Inverted Triangle':
    # Breezy A-line silhouettes
    # Flowy tunics
    # Relaxed, boyfriend button-ups
    # V-neck anything
    pass

elif output == 'Rectangle/Straight':
    pass
