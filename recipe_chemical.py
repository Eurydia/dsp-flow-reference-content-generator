from recipe import ItemEnum, Recipe


RECIPE_CHEMICAL: list[Recipe] = [
    Recipe(
        "Plastic",
        3,
        [
            (ItemEnum.GRAPHENE, 1, "1/1"),
            (ItemEnum.REFINED_OIL, 1, "1/2"),
            (ItemEnum.REFINED_OIL, 1, "1/2"),
        ],
        [(ItemEnum.PLASTIC, 1, "1/1")],
    ),
    Recipe(
        "Graphene",
        3,
        [
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/3"),
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/3"),
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/3"),
            (ItemEnum.SULFURIC_ACID, 1, "1/1"),
        ],
        [(ItemEnum.GRAPHENE, 2, "2/2")],
    ),
    Recipe(
        "Organic Crystal",
        6,
        [
            (ItemEnum.WATER, 1, "1/3"),
            (ItemEnum.REFINED_OIL, 1, "1/1"),
            (ItemEnum.PLASTIC, 1, "1/2"),
            (ItemEnum.PLASTIC, 1, "1/2"),
        ],
        [(ItemEnum.ORGANIC_CRYSTAL, 1, "1/1")],
    ),
    Recipe(
        "Graphene (advanced)",
        2,
        [
            (ItemEnum.FIRE_ICE, 2, "2/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 1, "1/1"),
            (ItemEnum.GRAPHENE, 2, "2/2"),
        ],
    ),
    Recipe(
        "Hydrogen (Graphene (advanced))",
        2,
        [
            (ItemEnum.FIRE_ICE, 1, "1/2"),
            (ItemEnum.FIRE_ICE, 1, "1/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 1, "1/1"),
            (ItemEnum.GRAPHENE, 1, "1/2"),
            (ItemEnum.GRAPHENE, 1, "1/2"),
        ],
    ),
    Recipe(
        "Sulfuric Acid",
        6,
        [
            (ItemEnum.WATER, 4, "4/4"),
            (ItemEnum.REFINED_OIL, 3, "3/6"),
            (ItemEnum.REFINED_OIL, 3, "3/6"),
            (ItemEnum.STONE, 4, "4/8"),
            (ItemEnum.STONE, 4, "4/8"),
        ],
        [
            (ItemEnum.SULFURIC_ACID, 4, "4/4"),
        ],
    ),
    Recipe(
        "Carbon Nanotube",
        4,
        [
            (ItemEnum.TITANIUM_INGOT, 1, "1/1"),
            (ItemEnum.GRAPHENE, 1, "1/3"),
            (ItemEnum.GRAPHENE, 1, "1/3"),
            (ItemEnum.GRAPHENE, 1, "1/3"),
        ],
        [
            (ItemEnum.CARBON_NANOTUBE, 2, "2/2"),
        ],
    ),
    Recipe(
        "Carbon Nanotube (advanced)",
        4,
        [
            (ItemEnum.SPINIFORM_STALAGMITE_CRYSTAL, 2, "2/6"),
            (ItemEnum.SPINIFORM_STALAGMITE_CRYSTAL, 2, "2/6"),
            (ItemEnum.SPINIFORM_STALAGMITE_CRYSTAL, 2, "2/6"),
        ],
        [
            (ItemEnum.CARBON_NANOTUBE, 2, "2/2"),
        ],
    ),
]
