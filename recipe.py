from dataclasses import dataclass
from enum import StrEnum


class ItemEnum(StrEnum):
    PROLIFERATOR_MK_I = "Proliferator Mk.I"
    PROLIFERATOR_MK_II = "Proliferator Mk.II"
    PROLIFERATOR_MK_III = "Proliferator Mk.III"
    COAL = "Coal"
    DIAMOND = "Diamond"
    CARBON_NANOTUBE = "Carbon Nanotube"
    MAGNETIC_COIL = "Magnetic Coil"
    COPPER_INGOT = "Copper Ingot"
    IRON_INGOT = "Iron Ingot"
    HYDROGEN = "Hydrogen"
    TITANIUM_INGOT = "Titanium Ingot"
    SUPER_MAGNETIC_RING = "Super-magnetic Ring"
    DEUTERIUM = "Deuterium"
    TITANIUM_ALLOY = "Titanium Alloy"
    HYDORGEN_FUEL_ROD = "Hydrogen Fuel Rod"
    DEUTERON_FUEL_ROD = "Deuteron Fuel Rod"
    ANTIMATTER_FUEL_ROD = "Antimatter Fuel Rod"
    ANNIHILATION_CONSTRAINT_SPHERE = (
        "Annihilation Constraint Sphere"
    )
    ANTIMATTER = "Antimatter"
    GEAR = "Gear"
    FRACTAL_SILICON = "Fractal Silicon"
    CRYSTAL_SILICON = "Crystal Silicon"
    GLASS = "Glass"
    WATER = "Water"
    TITANIUM_GLASS = "Titanium Glass"
    PRISM = "Prism"
    ORGANIC_CRYSTAL = "Organic Crystal"
    TITANIUM_CRYSTAL = "Titanium Crystal"
    ELECTRIC_MOTOR = "Electric Motor"
    ELECTROMAGNETIC_TURBINE = "Electromagnetic Turbine"
    CIRCUIT_BOARD = "Circuit Board"
    GRAVITON_LENS = "Graviton Lens"
    STRANGE_MATTER = "Strange Matter"
    PLANE_FILTER = "Plane Filter"
    CASIMIR_CRYSTAL = "Casimir Crystal"
    DYSON_SPHERE_COMPONENT = "Dyson Sphere Component"
    SMALL_CARRIER_ROCKET = "Small Carrier Rocket"
    QUANTUM_CHIP = "Quantum Chip"
    PLASMA_EXCITER = "Plasma Exciter"
    ENERGETIC_GRAPHITE = "Energetic Graphite"
    MAGNET = "Magnet"
    PLASTIC = "Plastic"
    PARTICLE_BROADBAND = "Particle Broadband"
    PROCESSOR = "Processor"
    MICROCRYSTALLINE_COMPONENT = "Microcrystalline Component"
    GRAPHENE = "Graphene"
    PARTICLE_CONTAINER = "Particle Container"
    SOLAR_SAIL = "Solar Sail"
    PHOTON_COMBINER = "Photon Combiner"
    HIGH_PURITY_SILICON = "High-Purity Silicon"
    FRAME_MATERIAL = "Frame Material"
    OPTICAL_GRATING_CRYSTAL = "Optical Grating Crystal"
    UNIPOLAR_MAGNET = "Unipolar Magnet"
    SPACE_WARPER = "Space Warper"
    GRAVITY_MATRIX = "Gravity Matrix"
    FOUNDATION = "Foundation"
    STEEL = "Steel"
    STONE_BRICK = "Stone Brick"
    REFINED_OIL = "Refined Oil"
    SULFURIC_ACID = "Sulfuric Acid"
    FIRE_ICE = "Fire Ice"
    STONE = "Stone"
    SPINIFORM_STALAGMITE_CRYSTAL = "Spiniform Stalagmite Crystal"
    CRITICAL_PHOTON = "Critical Photon"
    CRUDE_OIL = "Crude Oil"
    ELECTROMAGNETIC_MATRIX = "Electromagnetic Matrix"
    ENERGY_MATRIX = "Energy Matrix"
    STRUCTURE_MATRIX = "Structure Matrix"
    INFORMATION_MATRIX = "Information Matrix"
    UNIVERSE_MATRIX = "Universe Matrix"
    IRON_ORE = "Iron Ore"
    COPPER_ORE = "Copper Ore"
    SILICON_ORE = "Silicon Ore"
    TITANIUM_ORE = "Titanium Ore"
    KIMBERLITE_ORE = "Kimberlite Ore"
    THRUSTER = "Thruster"
    REINFORCED_THRUSTER = "Reinforced Thruster"
    LOGISTICS_BOT = "Logistics Bot"
    LOGISTICS_DRONE = "Logistics Drone"
    LOGISTICS_VESSEL = "Logistics Vessel"

    TESLA_TOWER = "Tesla Tower"
    WIRELESS_POWER_TOWER = "Wireless Power Tower"
    SATELLITE_SUBSTATION = "Statellite Substation"
    WIND_TURBINE = "Wind Turbine"
    THERMAL_POWER_PLANT = "Thermal Power Plant"
    SOLAR_PANEL = "Solar Panel"
    GEOTHERMAL_POWER_STATION = "Geothermal Power Station"
    MINI_FUSION_POWER_PLANT = "Mini Fusion Power Plant"
    ENERGY_EXCHANGER = "Energy Exchanger"
    RAY_RECEIVER = "Ray Receiver"
    ARTIFICIAL_STAR = "Artificial Star"
    CONVEYOR_BELT_MK_I = "Conveyor Belt Mk.I"
    CONVEYOR_BELT_MK_II = "Conveyor Belt Mk.II"
    CONVEYOR_BELT_MK_III = "Conveyor Belt Mk.III"
    SPLITTER = "Splitter"
    AUTOMATIC_PILER = "Automatic Piler"
    STORAGE_MK_I = "Storage Mk. I"
    STORAGE_MK_II = "Storage Mk. II"
    STORAGE_TANK = "Storage TANK"
    LOGISTICS_DISTRIBUTOR = "Logistics Distributor"
    PLANETARY_LOGISTICS_SYSTEM = "Planetary Logistics System"
    INTERSTELLAR_LOGISTICS_SYSTEM = (
        "Interstellar Logistics System"
    )
    ORBITAL_COLLECTOR = "Orbital Collector"
    ACCUMULATOR_FULL = "Accumulator (Full)"
    ACCUMULATOR = "Accumulator"
    SORTER_MK_I = "Sorter Mk.I"
    SORTER_MK_II = "Sorter Mk.II"
    SORTER_MK_III = "Sorter Mk.III"
    TRAFFIC_MONITOR = "Traffic Monitor"
    MINING_MACHINE = "Mining Machine"
    ADVANCED_MINING_MACHINE = "Advanced Mining Machine"
    WATER_PUMP = "Water Pump"
    OIL_EXTRACTOR = "Oil Extractor"
    OIL_REFINERY = "Oil Refinery"
    MINIATURE_PARTICLE_COLLIDER = "Miniature Particle Collider"
    EM_RAIL_EJECTOR = "EM-Rail Ejector"
    VERTICAL_LAUNCHING_SILO = "Vertical Launching Silo"
    ASSEMBLING_MACHINE_MK_I = "Assembling Machine Mk.I"
    ASSEMBLING_MACHINE_MK_II = "Assembling Machine Mk.II"
    ASSEMBLING_MACHINE_MK_III = "Assembling Machine Mk.III"
    ARC_SMELTER = "Arc Smelter"
    PLANE_SMELTER = "Plane Smelter"
    MATRIX_LAB = "Matrix Lab"
    SPRAY_COATER = "Spray Coater"
    FRACTIONER = "Fractioner"
    CHEMICAL_PLANT = "Chemical Plant"
    QUANTUM_CHEMICAL_PLANT = "Quantum Chemical Plant"


@dataclass
class Recipe:
    name: str
    cycle_speed: float
    material: list[tuple[ItemEnum, int, str]]
    product: list[tuple[ItemEnum, int, str]]
    production_speedup_only: bool = False

    @property
    def recommended_standard_blueprint(self) -> str:
        return f"{len(self.material)}-{len(self.product)}"
