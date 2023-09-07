from recipe import ItemEnum, Recipe


RECIPE_SMELTING: list[Recipe] = [
    Recipe(
        "Iron Ingot",
        1,
        [(ItemEnum.IRON_ORE, 1, "1/1")],
        [(ItemEnum.IRON_INGOT, 1, "1/1")],
    ),
    Recipe(
        "Copper Ingot",
        1,
        [(ItemEnum.COPPER_ORE, 1, "1/1")],
        [(ItemEnum.COPPER_INGOT, 1, "1/1")],
    ),
    Recipe(
        "High-Purity Silicon",
        2,
        [
            (ItemEnum.SILICON_ORE, 1, "1/2"),
            (ItemEnum.SILICON_ORE, 1, "1/2"),
        ],
        [(ItemEnum.HIGH_PURITY_SILICON, 1, "1/1")],
    ),
    Recipe(
        "Titanium Ingot",
        2,
        [
            (ItemEnum.TITANIUM_ORE, 1, "1/2"),
            (ItemEnum.TITANIUM_ORE, 1, "1/2"),
        ],
        [(ItemEnum.TITANIUM_INGOT, 1, "1/1")],
    ),
    Recipe(
        "Stone Brick",
        1,
        [(ItemEnum.STONE, 1, "1/1")],
        [(ItemEnum.STONE_BRICK, 1, "1/1")],
    ),
    Recipe(
        "Energetic Graphite",
        2,
        [
            (ItemEnum.COAL, 1, "1/2"),
            (ItemEnum.COAL, 1, "1/2"),
        ],
        [(ItemEnum.ENERGETIC_GRAPHITE, 1, "1/1")],
    ),
    Recipe(
        "Magnet",
        1.5,
        [(ItemEnum.IRON_ORE, 1, "1/1")],
        [(ItemEnum.MAGNET, 1, "1/1")],
    ),
    Recipe(
        "Titanium Alloy",
        12,
        [
            (ItemEnum.TITANIUM_INGOT, 4, "4/4"),
            (ItemEnum.STEEL, 4, "4/4"),
            (ItemEnum.SULFURIC_ACID, 4, "4/8"),
            (ItemEnum.SULFURIC_ACID, 4, "4/8"),
        ],
        [(ItemEnum.TITANIUM_ALLOY, 4, "4/4")],
    ),
    Recipe(
        "Glass",
        2,
        [
            (ItemEnum.STONE, 1, "1/2"),
            (ItemEnum.STONE, 1, "1/2"),
        ],
        [(ItemEnum.GLASS, 1, "1/1")],
    ),
    Recipe(
        "Diamond",
        2,
        [
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/1"),
        ],
        [(ItemEnum.DIAMOND, 1, "1/1")],
    ),
    Recipe(
        "Crystal Silicon",
        2,
        [
            (ItemEnum.HIGH_PURITY_SILICON, 1, "1/1"),
        ],
        [(ItemEnum.CRYSTAL_SILICON, 1, "1/1")],
    ),
    Recipe(
        "Steel",
        3,
        [
            (ItemEnum.IRON_INGOT, 3, "1/3"),
            (ItemEnum.IRON_INGOT, 3, "1/3"),
            (ItemEnum.IRON_INGOT, 3, "1/3"),
        ],
        [(ItemEnum.STEEL, 1, "1/1")],
    ),
    Recipe(
        "Diamond (advanced)",
        1.5,
        [(ItemEnum.KIMBERLITE_ORE, 1, "1/1")],
        [(ItemEnum.DIAMOND, 2, "2/2")],
    ),
    # Recipe(
    #     "Silicon Ore",
    #     10,
    #     [ItemEnum.STONE] 10,
    #     [ItemEnum.SILICON_ORE] 1,
    # ),
]
