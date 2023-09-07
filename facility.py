from dataclasses import dataclass


@dataclass
class Facility:
    name: str
    production_speed: float


FACILITIY_SMELTING: list[Facility] = [
    Facility("Arc Smelter", 1),
    Facility("Plane Smelter", 2),
]

FACILITIY_ASSEMBLER: list[Facility] = [
    Facility("Assembling Machine Mk.I", 0.75),
    Facility("Assembling Machine Mk.II", 1),
    Facility("Assembling Machine Mk.III", 1.5),
]

FACILITIY_REFINING: list[Facility] = [
    Facility("Oil Refinery", 1),
]

FACILITIY_CHEMICAL: list[Facility] = [
    Facility("Chemical Plant", 1),
    Facility("Quantum Chemical Plant", 2),
]

FACILITIY_PARTICLE_COLLIDER: list[Facility] = [
    Facility("Miniature Particle Collider", 1),
]

FACILITIY_RESEARCH: list[Facility] = [
    Facility("Matrix Lab", 1),
]
