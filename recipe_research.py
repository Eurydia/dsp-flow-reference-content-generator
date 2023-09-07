from recipe import ItemEnum, Recipe


RECIPE_RESEARCH: list[Recipe] = [
    Recipe(
        "Electromagnetic Matrix",
        3,
        [
            (ItemEnum.CIRCUIT_BOARD, 1, "1/1"),
            (ItemEnum.MAGNETIC_COIL, 1, "1/1"),
        ],
        [
            (ItemEnum.ELECTROMAGNETIC_MATRIX, 1, "1/1"),
        ],
    ),
    Recipe(
        "Energy Matrix",
        6,
        [
            (ItemEnum.HYDROGEN, 1, "1/2"),
            (ItemEnum.HYDROGEN, 1, "1/2"),
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/2"),
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/2"),
        ],
        [
            (ItemEnum.ENERGY_MATRIX, 1, "1/1"),
        ],
    ),
    Recipe(
        "Structure Matrix",
        8,
        [
            (ItemEnum.DIAMOND, 1, "1/1"),
            (ItemEnum.TITANIUM_CRYSTAL, 1, "1/1"),
        ],
        [
            (ItemEnum.ENERGY_MATRIX, 1, "1/1"),
        ],
    ),
    Recipe(
        "Information Matrix",
        10,
        [
            (ItemEnum.PARTICLE_BROADBAND, 1, "1/1"),
            (ItemEnum.PROCESSOR, 1, "1/2"),
            (ItemEnum.PROCESSOR, 1, "1/2"),
        ],
        [
            (ItemEnum.INFORMATION_MATRIX, 1, "1/1"),
        ],
    ),
    Recipe(
        "Gravity Matrix",
        10,
        [
            (ItemEnum.GRAVITON_LENS, 1, "1/1"),
            (ItemEnum.QUANTUM_CHIP, 1, "1/1"),
        ],
        [
            (ItemEnum.GRAVITY_MATRIX, 2, "2/2"),
        ],
    ),
    Recipe(
        "Universe Matrix",
        15,
        [
            (ItemEnum.ELECTROMAGNETIC_MATRIX, 1, "1/1"),
            (ItemEnum.ENERGY_MATRIX, 1, "1/1"),
            (ItemEnum.STRUCTURE_MATRIX, 1, "1/1"),
            (ItemEnum.INFORMATION_MATRIX, 1, "1/1"),
            (ItemEnum.GRAVITON_LENS, 1, "1/1"),
            (ItemEnum.ANTIMATTER, 1, "1/1"),
        ],
        [
            (ItemEnum.UNIVERSE_MATRIX, 1, "1/1"),
        ],
    ),
]
