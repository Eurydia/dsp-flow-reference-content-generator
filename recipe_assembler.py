from recipe import ItemEnum, Recipe

RECIPE_ASSEMBLER: list[Recipe] = [
    Recipe(
        "Proliferator Mk.I",
        0.5,
        [(ItemEnum.COAL, 1, "1/1")],
        [(ItemEnum.PROLIFERATOR_MK_I, 1, "1/1")],
    ),
    Recipe(
        "Proliferator Mk.II",
        1,
        [
            (ItemEnum.DIAMOND, 1, "1/1"),
            (ItemEnum.PROLIFERATOR_MK_I, 1, "1/2"),
            (ItemEnum.PROLIFERATOR_MK_I, 1, "1/2"),
        ],
        [(ItemEnum.PROLIFERATOR_MK_II, 1, "1/1")],
    ),
    Recipe(
        "Proliferator Mk.III",
        2,
        [
            (ItemEnum.CARBON_NANOTUBE, 1, "1/1"),
            (ItemEnum.PROLIFERATOR_MK_I, 1, "1/2"),
            (ItemEnum.PROLIFERATOR_MK_I, 1, "1/2"),
        ],
        [(ItemEnum.PROLIFERATOR_MK_III, 1, "1/1")],
    ),
    Recipe(
        "Magnetic Coil",
        1,
        [
            (ItemEnum.COPPER_INGOT, 1, "1/1"),
            (ItemEnum.MAGNET, 1, "1/2"),
            (ItemEnum.MAGNET, 1, "1/2"),
        ],
        [(ItemEnum.MAGNETIC_COIL, 2, "2/2")],
    ),
    Recipe(
        "Hydrogen Fuel Rod",
        6,
        [
            (ItemEnum.TITANIUM_INGOT, 1, "1/1"),
            (ItemEnum.MAGNET, 5, "5/10"),
            (ItemEnum.MAGNET, 5, "5/10"),
        ],
        [(ItemEnum.HYDORGEN_FUEL_ROD, 2, "2/2")],
    ),
    Recipe(
        "Deuteron Fuel Rod",
        12,
        [
            (ItemEnum.TITANIUM_ALLOY, 1, "1/1"),
            (ItemEnum.SUPER_MAGNETIC_RING, 1, "1/1"),
            (ItemEnum.DEUTERIUM, 10, "10/20"),
            (ItemEnum.DEUTERIUM, 10, "10/20"),
        ],
        [(ItemEnum.DEUTERON_FUEL_ROD, 2, "2/2")],
    ),
    Recipe(
        "Antimatter Fuel Rod",
        24,
        [
            (ItemEnum.TITANIUM_ALLOY, 1, "1/1"),
            (ItemEnum.ANNIHILATION_CONSTRAINT_SPHERE, 1, "1/1"),
            (ItemEnum.HYDROGEN, 12, "12/12"),
            (ItemEnum.ANTIMATTER, 12, "12/12"),
        ],
        [(ItemEnum.DEUTERON_FUEL_ROD, 2, "2/2")],
        True,
    ),
    Recipe(
        "Electric Motor",
        2,
        [
            (ItemEnum.MAGNETIC_COIL, 1, "1/1"),
            (ItemEnum.GEAR, 1, "1/1"),
            (ItemEnum.IRON_INGOT, 1, "1/2"),
            (ItemEnum.IRON_INGOT, 1, "1/2"),
        ],
        [(ItemEnum.ELECTRIC_MOTOR, 1, "1/1")],
    ),
    Recipe(
        "Crystal Silicon (advanced)",
        1.5,
        [
            (ItemEnum.FRACTAL_SILICON, 1, "1/1"),
        ],
        [(ItemEnum.CRYSTAL_SILICON, 2, "2/2")],
    ),
    Recipe(
        "Titanium Glass",
        5,
        [
            (ItemEnum.GLASS, 2, "2/2"),
            (ItemEnum.TITANIUM_INGOT, 2, "2/2"),
            (ItemEnum.WATER, 2, "2/2"),
        ],
        [(ItemEnum.TITANIUM_GLASS, 2, "2/2")],
    ),
    Recipe(
        "Prism",
        2,
        [
            (ItemEnum.GLASS, 1, "1/3"),
            (ItemEnum.GLASS, 1, "1/3"),
            (ItemEnum.GLASS, 1, "1/3"),
        ],
        [(ItemEnum.PRISM, 2, "2/2")],
    ),
    Recipe(
        "Titanium Crystal",
        4,
        [
            (ItemEnum.TITANIUM_INGOT, 1, "1/3"),
            (ItemEnum.TITANIUM_INGOT, 1, "1/3"),
            (ItemEnum.TITANIUM_INGOT, 1, "1/3"),
            (ItemEnum.ORGANIC_CRYSTAL, 1, "1/1"),
        ],
        [(ItemEnum.TITANIUM_CRYSTAL, 1, "1/1")],
    ),
    Recipe(
        "Gear",
        1,
        [
            (ItemEnum.IRON_INGOT, 1, "1/1"),
        ],
        [(ItemEnum.GEAR, 1, "1/1")],
    ),
    Recipe(
        "Electromagnetic Turbine",
        2,
        [
            (ItemEnum.ELECTRIC_MOTOR, 1, "1/2"),
            (ItemEnum.ELECTRIC_MOTOR, 1, "1/2"),
            (ItemEnum.MAGNETIC_COIL, 1, "1/2"),
            (ItemEnum.MAGNETIC_COIL, 1, "1/2"),
        ],
        [(ItemEnum.ELECTROMAGNETIC_TURBINE, 1, "1/1")],
    ),
    Recipe(
        "Circuit Board",
        1,
        [
            (ItemEnum.COPPER_INGOT, 1, "1/1"),
            (ItemEnum.IRON_INGOT, 1, "1/2"),
            (ItemEnum.IRON_INGOT, 1, "1/2"),
        ],
        [(ItemEnum.CIRCUIT_BOARD, 2, "2/2")],
    ),
    Recipe(
        "Graviton Lens",
        6,
        [
            (ItemEnum.STRANGE_MATTER, 1, "1/1"),
            (ItemEnum.DIAMOND, 1, "1/4"),
            (ItemEnum.DIAMOND, 1, "1/4"),
            (ItemEnum.DIAMOND, 1, "1/4"),
            (ItemEnum.DIAMOND, 1, "1/4"),
        ],
        [(ItemEnum.GRAVITON_LENS, 1, "1/1")],
    ),
    Recipe(
        "Plane Filter",
        12,
        [
            (ItemEnum.CASIMIR_CRYSTAL, 1, "1/1"),
            (ItemEnum.TITANIUM_GLASS, 1, "1/2"),
            (ItemEnum.TITANIUM_GLASS, 1, "1/2"),
        ],
        [(ItemEnum.PLANE_FILTER, 1, "1/1")],
    ),
    Recipe(
        "Small Carrier Rocket",
        6,
        [
            (ItemEnum.DYSON_SPHERE_COMPONENT, 2, "2/2"),
            (ItemEnum.QUANTUM_CHIP, 2, "2/2"),
            (ItemEnum.DEUTERON_FUEL_ROD, 2, "2/4"),
            (ItemEnum.DEUTERON_FUEL_ROD, 2, "2/4"),
        ],
        [(ItemEnum.SMALL_CARRIER_ROCKET, 1, "1/1")],
    ),
    Recipe(
        "Plasma Exciter",
        2,
        [
            (ItemEnum.PRISM, 2, "2/2"),
            (ItemEnum.MAGNETIC_COIL, 2, "2/4"),
            (ItemEnum.MAGNETIC_COIL, 2, "2/4"),
        ],
        [(ItemEnum.PLASMA_EXCITER, 1, "1/1")],
    ),
    Recipe(
        "Super-magnetic Ring",
        3,
        [
            (ItemEnum.ENERGETIC_GRAPHITE, 1, "1/1"),
            (ItemEnum.ELECTROMAGNETIC_TURBINE, 2, "2/2"),
            (ItemEnum.MAGNET, 3, "3/3"),
        ],
        [(ItemEnum.SUPER_MAGNETIC_RING, 1, "1/1")],
    ),
    Recipe(
        "Particle Broadband",
        8,
        [
            (ItemEnum.PLASTIC, 1, "1/1"),
            (ItemEnum.CRYSTAL_SILICON, 1, "1/2"),
            (ItemEnum.CRYSTAL_SILICON, 1, "1/2"),
            (ItemEnum.CARBON_NANOTUBE, 1, "1/2"),
            (ItemEnum.CARBON_NANOTUBE, 1, "1/2"),
        ],
        [(ItemEnum.PARTICLE_BROADBAND, 1, "1/1")],
    ),
    Recipe(
        "Processor",
        3,
        [
            (ItemEnum.CIRCUIT_BOARD, 1, "1/2"),
            (ItemEnum.CIRCUIT_BOARD, 1, "1/2"),
            (ItemEnum.MICROCRYSTALLINE_COMPONENT, 1, "1/2"),
            (ItemEnum.MICROCRYSTALLINE_COMPONENT, 1, "1/2"),
        ],
        [(ItemEnum.PROCESSOR, 1, "1/1")],
    ),
    Recipe(
        "Casimir Crystal",
        4,
        [
            (ItemEnum.TITANIUM_CRYSTAL, 1, "1/1"),
            (ItemEnum.GRAPHENE, 2, "2/2"),
            (ItemEnum.HYDROGEN, 4, "4/12"),
            (ItemEnum.HYDROGEN, 4, "4/12"),
            (ItemEnum.HYDROGEN, 4, "4/12"),
        ],
        [(ItemEnum.CASIMIR_CRYSTAL, 1, "1/1")],
    ),
    Recipe(
        "Particle Container",
        4,
        [
            (ItemEnum.ELECTROMAGNETIC_TURBINE, 2, "2/2"),
            (ItemEnum.GRAPHENE, 2, "2/2"),
            (ItemEnum.COPPER_INGOT, 2, "2/2"),
        ],
        [(ItemEnum.PARTICLE_CONTAINER, 1, "1/1")],
    ),
    Recipe(
        "Annihilation Constraint Sphere",
        20,
        [
            (ItemEnum.PARTICLE_CONTAINER, 1, "1/1"),
            (ItemEnum.PROCESSOR, 1, "1/1"),
        ],
        [(ItemEnum.ANNIHILATION_CONSTRAINT_SPHERE, 1, "1/1")],
    ),
    Recipe(
        "Solar Sail",
        4,
        [
            (ItemEnum.GRAPHENE, 1, "1/1"),
            (ItemEnum.PHOTON_COMBINER, 1, "1/1"),
        ],
        [(ItemEnum.SOLAR_SAIL, 2, "2/2")],
    ),
    Recipe(
        "Frame Material",
        6,
        [
            (ItemEnum.HIGH_PURITY_SILICON, 1, "1/1"),
            (ItemEnum.TITANIUM_INGOT, 1, "1/1"),
            (ItemEnum.CARBON_NANOTUBE, 2, "2/4"),
            (ItemEnum.CARBON_NANOTUBE, 2, "2/4"),
        ],
        [(ItemEnum.FRAME_MATERIAL, 1, "1/1")],
    ),
    Recipe(
        "Dyson Sphere Component",
        8,
        [
            (ItemEnum.FRAME_MATERIAL, 3, "3/3"),
            (ItemEnum.PROCESSOR, 3, "3/3"),
            (ItemEnum.SOLAR_SAIL, 3, "3/3"),
        ],
        [(ItemEnum.DYSON_SPHERE_COMPONENT, 1, "1/1")],
    ),
    Recipe(
        "Photon Combiner",
        3,
        [
            (ItemEnum.CIRCUIT_BOARD, 1, "1/1"),
            (ItemEnum.PRISM, 1, "1/2"),
            (ItemEnum.PRISM, 1, "1/2"),
        ],
        [(ItemEnum.PHOTON_COMBINER, 1, "1/1")],
    ),
    Recipe(
        "Photon Combiner (advanced)",
        3,
        [
            (ItemEnum.CIRCUIT_BOARD, 1, "1/1"),
            (ItemEnum.OPTICAL_GRATING_CRYSTAL, 1, "1/1"),
        ],
        [(ItemEnum.PHOTON_COMBINER, 1, "1/1")],
    ),
    Recipe(
        "Microcrystalline Component",
        2,
        [
            (ItemEnum.COPPER_INGOT, 1, "1/1"),
            (ItemEnum.HIGH_PURITY_SILICON, 1, "1/2"),
            (ItemEnum.HIGH_PURITY_SILICON, 1, "1/2"),
        ],
        [(ItemEnum.MICROCRYSTALLINE_COMPONENT, 1, "1/1")],
    ),
    Recipe(
        "Quantum Chip",
        6,
        [
            (ItemEnum.PROCESSOR, 1, "1/2"),
            (ItemEnum.PROCESSOR, 1, "1/2"),
            (ItemEnum.PLANE_FILTER, 1, "1/2"),
            (ItemEnum.PLANE_FILTER, 1, "1/2"),
        ],
        [(ItemEnum.QUANTUM_CHIP, 1, "1/1")],
    ),
    Recipe(
        "Casimir Crystal (advanced)",
        4,
        [
            (ItemEnum.GRAPHENE, 2, "2/2"),
            (ItemEnum.OPTICAL_GRATING_CRYSTAL, 4, "4/8"),
            (ItemEnum.OPTICAL_GRATING_CRYSTAL, 4, "4/8"),
            (ItemEnum.HYDROGEN, 6, "6/12"),
            (ItemEnum.HYDROGEN, 6, "6/12"),
        ],
        [(ItemEnum.CASIMIR_CRYSTAL, 1, "1/1")],
    ),
    Recipe(
        "Particle Container (advanced)",
        4,
        [
            (ItemEnum.COPPER_INGOT, 2, "2/2"),
            (ItemEnum.UNIPOLAR_MAGNET, 5, "5/10"),
            (ItemEnum.UNIPOLAR_MAGNET, 5, "5/10"),
        ],
        [(ItemEnum.PARTICLE_CONTAINER, 1, "1/1")],
    ),
    Recipe(
        "Space Warper",
        10,
        [
            (ItemEnum.GRAVITON_LENS, 1, "1/1"),
        ],
        [(ItemEnum.SPACE_WARPER, 1, "1/1")],
    ),
    Recipe(
        "Space Warper (advanced)",
        10,
        [
            (ItemEnum.GRAVITY_MATRIX, 1, "1/1"),
        ],
        [(ItemEnum.SPACE_WARPER, 8, "8/8")],
    ),
    Recipe(
        "Foundation",
        1,
        [
            (ItemEnum.STEEL, 1, "1/1"),
            (ItemEnum.STONE_BRICK, 1, "1/3"),
            (ItemEnum.STONE_BRICK, 1, "1/3"),
            (ItemEnum.STONE_BRICK, 1, "1/3"),
        ],
        [(ItemEnum.FOUNDATION, 1, "1/1")],
    ),
    Recipe(
        "Thruster",
        4,
        [
            (ItemEnum.STEEL, 1, "1/2"),
            (ItemEnum.STEEL, 1, "1/2"),
            (ItemEnum.COPPER_INGOT, 1, "1/1"),
        ],
        [(ItemEnum.THRUSTER, 1, "1/1")],
    ),
    Recipe(
        "Reinforced Thruster",
        6,
        [
            (ItemEnum.TITANIUM_ALLOY, 5, "5/5"),
            (ItemEnum.ELECTROMAGNETIC_TURBINE, 5, "5/5"),
        ],
        [(ItemEnum.REINFORCED_THRUSTER, 1, "1/1")],
    ),
    Recipe(
        "Logistics Bot",
        2,
        [
            (ItemEnum.IRON_INGOT, 1, "1/2"),
            (ItemEnum.IRON_INGOT, 1, "1/2"),
            (ItemEnum.ELECTROMAGNETIC_TURBINE, 1, "1/1"),
            (ItemEnum.PROCESSOR, 1, "1/1"),
        ],
        [(ItemEnum.LOGISTICS_BOT, 1, "1/1")],
    ),
    Recipe(
        "Logistics Drone",
        4,
        [
            (ItemEnum.IRON_INGOT, 5, "5/5"),
            (ItemEnum.IRON_INGOT, 2, "2/2"),
            (ItemEnum.THRUSTER, 2, "2/2"),
        ],
        [(ItemEnum.LOGISTICS_DRONE, 1, "1/1")],
    ),
    Recipe(
        "Logistics Vessel",
        6,
        [
            (ItemEnum.TITANIUM_ALLOY, 5, "5/10"),
            (ItemEnum.TITANIUM_ALLOY, 5, "5/10"),
            (ItemEnum.PROCESSOR, 5, "5/10"),
            (ItemEnum.PROCESSOR, 5, "5/10"),
            (ItemEnum.REINFORCED_THRUSTER, 2, "2/2"),
        ],
        [(ItemEnum.LOGISTICS_VESSEL, 1, "1/1")],
    ),
    # Recipe(
    #     "Tesla Tower",
    #     1,
    #     {
    #         [ItemEnum.IRON_INGOT]: 2,
    #         [ItemEnum.MAGNETIC_COIL]: 1,
    #     },
    #     {
    #         [ItemEnum.TESLA_TOWER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Wireless Power Tower",
    #     3,
    #     {
    #         [ItemEnum.PLASMA_EXCITER]: 3,
    #         [ItemEnum.TESLA_TOWER]: 1,
    #     },
    #     {
    #         [ItemEnum.WIRELESS_POWER_TOWER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Satellite Substation",
    #     5,
    #     {
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 10,
    #         [ItemEnum.FRAME_MATERIAL]: 2,
    #         [ItemEnum.WIRELESS_POWER_TOWER]: 1,
    #     },
    #     {
    #         [ItemEnum.SATELLITE_SUBSTATION]: 1,
    #     },
    # ),
    # Recipe(
    #     "Wind Turbine",
    #     4,
    #     {
    #         [ItemEnum.IRON_INGOT]: 6,
    #         [ItemEnum.MAGNETIC_COIL]: 3,
    #         [ItemEnum.GEAR]: 1,
    #     },
    #     {
    #         [ItemEnum.WIND_TURBINE]: 1,
    #     },
    # ),
    # Recipe(
    #     "Thermal Power Plant",
    #     5,
    #     {
    #         [ItemEnum.IRON_INGOT]: 10,
    #         [ItemEnum.STONE_BRICK]: 4,
    #         [ItemEnum.GEAR]: 4,
    #         [ItemEnum.MAGNETIC_COIL]: 4,
    #     },
    #     {
    #         [ItemEnum.THERMAL_POWER_PLANT]: 1,
    #     },
    # ),
    # Recipe(
    #     "Geothermal Power Station",
    #     6,
    #     {
    #         [ItemEnum.COPPER_INGOT]: 20,
    #         [ItemEnum.STEEL]: 15,
    #         [ItemEnum.PHOTON_COMBINER]: 4,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 1,
    #     },
    #     {
    #         [ItemEnum.GEOTHERMAL_POWER_STATION]: 1,
    #     },
    # ),
    # Recipe(
    #     "Mini Fusion Power Plant",
    #     10,
    #     {
    #         [ItemEnum.TITANIUM_ALLOY]: 12,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 10,
    #         [ItemEnum.CARBON_NANOTUBE]: 8,
    #         [ItemEnum.PROCESSOR]: 4,
    #     },
    #     {
    #         [ItemEnum.MINI_FUSION_POWER_PLANT]: 1,
    #     },
    # ),
    # Recipe(
    #     "Energy Exchanger",
    #     15,
    #     {
    #         [ItemEnum.TITANIUM_ALLOY]: 40,
    #         [ItemEnum.STEEL]: 40,
    #         [ItemEnum.PROCESSOR]: 40,
    #         [ItemEnum.PARTICLE_CONTAINER]: 8,
    #     },
    #     {
    #         [ItemEnum.ENERGY_EXCHANGER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Ray Receiver",
    #     8,
    #     {
    #         [ItemEnum.STEEL]: 20,
    #         [ItemEnum.HIGH_PURITY_SILICON]: 20,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 20,
    #         [ItemEnum.PHOTON_COMBINER]: 10,
    #         [ItemEnum.PROCESSOR]: 5,
    #     },
    #     {
    #         [ItemEnum.RAY_RECEIVER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Artificial Star",
    #     30,
    #     {
    #         [ItemEnum.TITANIUM_ALLOY]: 20,
    #         [ItemEnum.FRAME_MATERIAL]: 20,
    #         [ItemEnum.ANNIHILATION_CONSTRAINT_SPHERE]: 10,
    #         [ItemEnum.QUANTUM_CHIP]: 10,
    #     },
    #     {
    #         [ItemEnum.ARTIFICIAL_STAR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Conveyor Belt MK.I",
    #     1,
    #     {
    #         [ItemEnum.IRON_INGOT]: 2,
    #         [ItemEnum.GEAR]: 1,
    #     },
    #     {
    #         [ItemEnum.CONVEYOR_BELT_MK_I]: 3,
    #     },
    # ),
    # Recipe(
    #     "Conveyor Belt MK.II",
    #     1,
    #     {
    #         [ItemEnum.CONVEYOR_BELT_MK_I]: 3,
    #         [ItemEnum.ELECTROMAGNETIC_TURBINE]: 1,
    #     },
    #     {
    #         [ItemEnum.CONVEYOR_BELT_MK_II]: 3,
    #     },
    # ),
    # Recipe(
    #     "Conveyor Belt MK.III",
    #     1,
    #     {
    #         [ItemEnum.CONVEYOR_BELT_MK_II]: 3,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 1,
    #         [ItemEnum.GRAPHENE]: 1,
    #     },
    #     {
    #         [ItemEnum.CONVEYOR_BELT_MK_III]: 3,
    #     },
    # ),
    # Recipe(
    #     "Splitter",
    #     2,
    #     {
    #         [ItemEnum.IRON_INGOT]: 3,
    #         [ItemEnum.GEAR]: 2,
    #         [ItemEnum.CIRCUIT_BOARD]: 1,
    #     },
    #     {
    #         [ItemEnum.SPLITTER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Automatic Piler",
    #     4,
    #     {
    #         [ItemEnum.GEAR]: 4,
    #         [ItemEnum.STEEL]: 3,
    #         [ItemEnum.PROCESSOR]: 2,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 1,
    #     },
    #     {
    #         [ItemEnum.AUTOMATIC_PILER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Storage Mk.I",
    #     2,
    #     {
    #         [ItemEnum.IRON_INGOT]: 4,
    #         [ItemEnum.STONE_BRICK]: 4,
    #     },
    #     {
    #         [ItemEnum.STORAGE_MK_I]: 1,
    #     },
    # ),
    # Recipe(
    #     "Storage Mk.II",
    #     4,
    #     {
    #         [ItemEnum.STEEL]: 8,
    #         [ItemEnum.STONE_BRICK]: 8,
    #     },
    #     {
    #         [ItemEnum.STORAGE_MK_II]: 1,
    #     },
    # ),
    # Recipe(
    #     "Storage Tank",
    #     2,
    #     {
    #         [ItemEnum.IRON_INGOT]: 8,
    #         [ItemEnum.STONE_BRICK]: 4,
    #         [ItemEnum.GLASS]: 4,
    #     },
    #     {
    #         [ItemEnum.STORAGE_TANK]: 1,
    #     },
    # ),
    # Recipe(
    #     "Logistics Distributor",
    #     8,
    #     {
    #         [ItemEnum.IRON_INGOT]: 8,
    #         [ItemEnum.PLASMA_EXCITER]: 4,
    #         [ItemEnum.PROCESSOR]: 4,
    #     },
    #     {
    #         [ItemEnum.LOGISTICS_DISTRIBUTOR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Planetary Logistics Station",
    #     20,
    #     {
    #         [ItemEnum.STEEL]: 40,
    #         [ItemEnum.TITANIUM_INGOT]: 40,
    #         [ItemEnum.PROCESSOR]: 40,
    #         [ItemEnum.PARTICLE_CONTAINER]: 20,
    #     },
    #     {
    #         [ItemEnum.PLANETARY_LOGISTICS_SYSTEM]: 1,
    #     },
    # ),
    # Recipe(
    #     "Interstellar Logistics Station",
    #     30,
    #     {
    #         [ItemEnum.TITANIUM_INGOT]: 40,
    #         [ItemEnum.PARTICLE_CONTAINER]: 20,
    #         [ItemEnum.PLANETARY_LOGISTICS_SYSTEM]: 1,
    #     },
    #     {
    #         [ItemEnum.INTERSTELLAR_LOGISTICS_SYSTEM]: 1,
    #     },
    # ),
    # Recipe(
    #     "Orbital Collector",
    #     30,
    #     {
    #         [ItemEnum.INTERSTELLAR_LOGISTICS_SYSTEM]: 1,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 50,
    #         [ItemEnum.REINFORCED_THRUSTER]: 20,
    #         [ItemEnum.ACCUMULATOR_FULL]: 20,
    #     },
    #     {
    #         [ItemEnum.ORBITAL_COLLECTOR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Sorter Mk.I",
    #     1,
    #     {
    #         [ItemEnum.IRON_INGOT]: 1,
    #         [ItemEnum.CIRCUIT_BOARD]: 1,
    #     },
    #     {
    #         [ItemEnum.SORTER_MK_I]: 1,
    #     },
    # ),
    # Recipe(
    #     "Sorter Mk.II",
    #     1,
    #     {
    #         [ItemEnum.SORTER_MK_I]: 2,
    #         [ItemEnum.ELECTRIC_MOTOR]: 1,
    #     },
    #     {
    #         [ItemEnum.SORTER_MK_II]: 2,
    #     },
    # ),
    # Recipe(
    #     "Sorter Mk.III",
    #     1,
    #     {
    #         [ItemEnum.SORTER_MK_II]: 2,
    #         [ItemEnum.ELECTROMAGNETIC_TURBINE]: 1,
    #     },
    #     {
    #         [ItemEnum.SORTER_MK_III]: 2,
    #     },
    # ),
    # Recipe(
    #     "Traffic Monitor",
    #     2,
    #     {
    #         [ItemEnum.IRON_INGOT]: 3,
    #         [ItemEnum.GEAR]: 2,
    #         [ItemEnum.CIRCUIT_BOARD]: 2,
    #         [ItemEnum.GLASS]: 1,
    #     },
    #     {
    #         [ItemEnum.TRAFFIC_MONITOR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Mining Machine",
    #     3,
    #     {
    #         [ItemEnum.IRON_INGOT]: 4,
    #         [ItemEnum.CIRCUIT_BOARD]: 2,
    #         [ItemEnum.GEAR]: 2,
    #         [ItemEnum.MAGNETIC_COIL]: 2,
    #     },
    #     {
    #         [ItemEnum.MINING_MACHINE]: 1,
    #     },
    # ),
    # Recipe(
    #     "Advanced Mining Machine",
    #     20,
    #     {
    #         [ItemEnum.OPTICAL_GRATING_CRYSTAL]: 40,
    #         [ItemEnum.TITANIUM_ALLOY]: 20,
    #         [ItemEnum.FRAME_MATERIAL]: 10,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 10,
    #         [ItemEnum.QUANTUM_CHIP]: 4,
    #     },
    #     {
    #         [ItemEnum.ADVANCED_MINING_MACHINE]: 1,
    #     },
    # ),
    # Recipe(
    #     "Water Pump",
    #     4,
    #     {
    #         [ItemEnum.IRON_INGOT]: 8,
    #         [ItemEnum.STONE_BRICK]: 4,
    #         [ItemEnum.ELECTRIC_MOTOR]: 4,
    #         [ItemEnum.CIRCUIT_BOARD]: 2,
    #     },
    #     {
    #         [ItemEnum.WATER_PUMP]: 1,
    #     },
    # ),
    # Recipe(
    #     "Oil Extractor",
    #     8,
    #     {
    #         [ItemEnum.STEEL]: 12,
    #         [ItemEnum.STONE_BRICK]: 12,
    #         [ItemEnum.CIRCUIT_BOARD]: 6,
    #         [ItemEnum.PLASMA_EXCITER]: 4,
    #     },
    #     {
    #         [ItemEnum.OIL_EXTRACTOR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Oil Refinery",
    #     6,
    #     {
    #         [ItemEnum.STEEL]: 10,
    #         [ItemEnum.STONE_BRICK]: 10,
    #         [ItemEnum.CIRCUIT_BOARD]: 6,
    #         [ItemEnum.PLASMA_EXCITER]: 6,
    #     },
    #     {
    #         [ItemEnum.OIL_REFINERY]: 1,
    #     },
    # ),
    # Recipe(
    #     "Miniature Particle Collider",
    #     15,
    #     {
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 25,
    #         [ItemEnum.TITANIUM_ALLOY]: 20,
    #         [ItemEnum.FRAME_MATERIAL]: 20,
    #         [ItemEnum.GRAPHENE]: 10,
    #         [ItemEnum.PROCESSOR]: 8,
    #     },
    #     {
    #         [ItemEnum.MINIATURE_PARTICLE_COLLIDER]: 1,
    #     },
    # ),
    # Recipe(
    #     "EM-Rail Ejector",
    #     6,
    #     {
    #         [ItemEnum.STEEL]: 20,
    #         [ItemEnum.GEAR]: 20,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 10,
    #         [ItemEnum.PROCESSOR]: 5,
    #     },
    #     {
    #         [ItemEnum.EM_RAIL_EJECTOR]: 1,
    #     },
    # ),
    # Recipe(
    #     "Vertical Launching Silo",
    #     30,
    #     {
    #         [ItemEnum.TITANIUM_ALLOY]: 80,
    #         [ItemEnum.FRAME_MATERIAL]: 30,
    #         [ItemEnum.GRAVITON_LENS]: 20,
    #         [ItemEnum.QUANTUM_CHIP]: 10,
    #     },
    #     {
    #         [ItemEnum.VERTICAL_LAUNCHING_SILO]: 1,
    #     },
    # ),
    # Recipe(
    #     "Assembling Machine Mk.I",
    #     2,
    #     {
    #         [ItemEnum.GEAR]: 8,
    #         [ItemEnum.IRON_INGOT]: 4,
    #         [ItemEnum.CIRCUIT_BOARD]: 4,
    #     },
    #     {
    #         [ItemEnum.ASSEMBLING_MACHINE_MK_I]: 1,
    #     },
    # ),
    # Recipe(
    #     "Assembling Machine Mk.II",
    #     3,
    #     {
    #         [ItemEnum.GRAPHENE]: 8,
    #         [ItemEnum.PROCESSOR]: 4,
    #         [ItemEnum.ASSEMBLING_MACHINE_MK_I]: 1,
    #     },
    #     {
    #         [ItemEnum.ASSEMBLING_MACHINE_MK_II]: 1,
    #     },
    # ),
    # Recipe(
    #     "Assembling Machine Mk.III",
    #     4,
    #     {
    #         [ItemEnum.PARTICLE_BROADBAND]: 8,
    #         [ItemEnum.QUANTUM_CHIP]: 2,
    #         [ItemEnum.ASSEMBLING_MACHINE_MK_II]: 1,
    #     },
    #     {
    #         [ItemEnum.ASSEMBLING_MACHINE_MK_III]: 1,
    #     },
    # ),
    # Recipe(
    #     "Arc Smelter",
    #     3,
    #     {
    #         [ItemEnum.IRON_INGOT]: 4,
    #         [ItemEnum.CIRCUIT_BOARD]: 4,
    #         [ItemEnum.STONE_BRICK]: 2,
    #         [ItemEnum.MAGNETIC_COIL]: 2,
    #     },
    #     {
    #         [ItemEnum.ARC_SMELTER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Plane Smelter",
    #     5,
    #     {
    #         [ItemEnum.UNIPOLAR_MAGNET]: 15,
    #         [ItemEnum.FRAME_MATERIAL]: 5,
    #         [ItemEnum.PLANE_FILTER]: 4,
    #         [ItemEnum.ARC_SMELTER]: 1,
    #     },
    #     {
    #         [ItemEnum.PLANE_SMELTER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Matrix Lab",
    #     3,
    #     {
    #         [ItemEnum.IRON_INGOT]: 8,
    #         [ItemEnum.GLASS]: 4,
    #         [ItemEnum.CIRCUIT_BOARD]: 4,
    #         [ItemEnum.MAGNETIC_COIL]: 4,
    #     },
    #     {
    #         [ItemEnum.MATRIX_LAB]: 1,
    #     },
    # ),
    # Recipe(
    #     "Spray Coater",
    #     3,
    #     {
    #         [ItemEnum.STEEL]: 4,
    #         [ItemEnum.MICROCRYSTALLINE_COMPONENT]: 4,
    #         [ItemEnum.PLASMA_EXCITER]: 2,
    #         [ItemEnum.CIRCUIT_BOARD]: 2,
    #     },
    #     {
    #         [ItemEnum.SPRAY_COATER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Fractioner",
    #     3,
    #     {
    #         [ItemEnum.STEEL]: 8,
    #         [ItemEnum.STONE_BRICK]: 4,
    #         [ItemEnum.GLASS]: 4,
    #         [ItemEnum.PROCESSOR]: 1,
    #     },
    #     {
    #         [ItemEnum.FRACTIONER]: 1,
    #     },
    # ),
    # Recipe(
    #     "Chemical Plant",
    #     5,
    #     {
    #         [ItemEnum.STEEL]: 8,
    #         [ItemEnum.STONE_BRICK]: 8,
    #         [ItemEnum.GLASS]: 8,
    #         [ItemEnum.CIRCUIT_BOARD]: 2,
    #     },
    #     {
    #         [ItemEnum.CHEMICAL_PLANT]: 1,
    #     },
    # ),
    # Recipe(
    #     "Quantum Chemical Plant",
    #     10,
    #     {
    #         [ItemEnum.TITANIUM_GLASS]: 10,
    #         [ItemEnum.QUANTUM_CHIP]: 3,
    #         [ItemEnum.STRANGE_MATTER]: 3,
    #         [ItemEnum.CHEMICAL_PLANT]: 1,
    #     },
    #     {
    #         [ItemEnum.QUANTUM_CHEMICAL_PLANT]: 1,
    #     },
    # ),
    # Recipe(
    #     "Accumulator",
    #     5,
    #     {
    #         [ItemEnum.IRON_INGOT]: 6,
    #         [ItemEnum.CRYSTAL_SILICON]: 6,
    #         [ItemEnum.SUPER_MAGNETIC_RING]: 1,
    #     },
    #     {
    #         [ItemEnum.ACCUMULATOR]: 1,
    #     },
    # ),
]
