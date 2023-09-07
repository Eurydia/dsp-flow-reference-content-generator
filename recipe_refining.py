from recipe import ItemEnum, Recipe

RECIPE_REFINING: list[Recipe] = [
    Recipe(
        "Hydrogen (Plasma Refining)",
        4,
        [
            (ItemEnum.CRUDE_OIL, 1, "1/2"),
            (ItemEnum.CRUDE_OIL, 1, "1/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 1, "1/2"),
            (ItemEnum.REFINED_OIL, 1, "1/2"),
        ],
    ),
    Recipe(
        "Refined Oil (Plasma Refining)",
        4,
        [
            (ItemEnum.CRUDE_OIL, 2, "2/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 2, "2/2"),
        ],
    ),
    Recipe(
        "Hydrogen (X-Ray Cracking)",
        4,
        [
            (ItemEnum.REFINED_OIL, 1, "1/1"),
            (ItemEnum.HYDROGEN, 2, "2/2"),
        ],
        [
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 3, "3/3"),
        ],
        True,
    ),
    Recipe(
        "Energetic Graphite (X-Ray Cracking)",
        4,
        [
            (ItemEnum.REFINED_OIL, 1, "1/1"),
            (ItemEnum.HYDROGEN, 2, "2/2"),
        ],
        [
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 1, "1/3"),
            (ItemEnum.REFINED_OIL, 1, "1/3"),
            (ItemEnum.REFINED_OIL, 1, "1/3"),
        ],
        True,
    ),
    Recipe(
        "Refined Oil (Reforming Refine)",
        4,
        [
            (ItemEnum.HYDROGEN, 1, "1/1"),
            (ItemEnum.COAL, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 2, "2/2"),
        ],
        [
            (ItemEnum.REFINED_OIL, 3, "3/3"),
        ],
        True,
    ),
]
