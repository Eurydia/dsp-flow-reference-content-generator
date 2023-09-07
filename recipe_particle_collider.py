from recipe import ItemEnum, Recipe


RECIPE_PARTICLE_COLLIDER: list[Recipe] = [
    Recipe(
        "Strange Matter",
        8,
        [
            (ItemEnum.PARTICLE_CONTAINER, 2, "2/2"),
            (ItemEnum.IRON_INGOT, 2, "2/2"),
            (ItemEnum.DEUTERIUM, 5, "5/10"),
            (ItemEnum.DEUTERIUM, 5, "5/10"),
        ],
        [
            (ItemEnum.STRANGE_MATTER, 1, "1/1"),
        ],
    ),
    Recipe(
        "Deuterium",
        2.5,
        [
            (ItemEnum.HYDROGEN, 5, "5/10"),
            (ItemEnum.HYDROGEN, 5, "5/10"),
        ],
        [
            (ItemEnum.DEUTERIUM, 5, "5/5"),
        ],
        True,
    ),
    Recipe(
        "Antimatter",
        2,
        [
            (ItemEnum.CRITICAL_PHOTON, 2, "2/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 2, "2/2"),
            (ItemEnum.ANTIMATTER, 2, "2/2"),
        ],
        True,
    ),
    Recipe(
        "Hydrogen (Critical Photon)",
        2,
        [
            (ItemEnum.CRITICAL_PHOTON, 2, "2/2"),
        ],
        [
            (ItemEnum.HYDROGEN, 2, "2/2"),
            (ItemEnum.ANTIMATTER, 2, "2/2"),
        ],
        True,
    ),
]
