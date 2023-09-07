from dataclasses import dataclass
from math import floor
from recipe import Recipe
from os import mkdir, path

from recipe_assembler import RECIPE_ASSEMBLER
from recipe_refining import RECIPE_REFINING
from recipes_smelting import RECIPE_SMELTING
from recipe_chemical import RECIPE_CHEMICAL
from recipe_particle_collider import RECIPE_PARTICLE_COLLIDER
from recipe_research import RECIPE_RESEARCH
from content_generator.facility import (
    Facility,
    FACILITIY_SMELTING,
    FACILITIY_ASSEMBLER,
    FACILITIY_REFINING,
    FACILITIY_CHEMICAL,
    FACILITIY_PARTICLE_COLLIDER,
    FACILITIY_RESEARCH,
)


@dataclass
class Proliferator:
    name: str
    extra_product: float
    production_speedup: float


@dataclass
class Job:
    recipes: list[Recipe]
    facilities: list[Facility]
    recipe_group: str


def compute_production_per_facility(
    r: Recipe, f: Facility, p: Proliferator
) -> float:
    cycles_per_minute: float = (
        (60 / r.cycle_speed)
        * f.production_speed
        * p.production_speedup
    )

    return float(
        cycles_per_minute
        * max(v for _, v, _ in r.product)
        * p.extra_product
    )


def compute_facilities_required(
    production_target: int,
    r: Recipe,
    f: Facility,
    p: Proliferator,
) -> float:
    return float(
        production_target
        / compute_production_per_facility(r, f, p)
    )


def compute_facilities_per_array(
    transport_speed: float,
    r: Recipe,
    f: Facility,
    p: Proliferator,
) -> float:
    return float(transport_speed) / (
        (60 / r.cycle_speed)
        * (f.production_speed * p.production_speedup)
        * max(
            max(v for _, v, _ in r.product) * p.extra_product,
            max(v for _, v, _ in r.material),
        )
    )


def write_blueprint_section(
    j: Job,
    r: Recipe,
    blueprint_base_path: str = "content/Standard Set/Blueprints",
) -> str:
    blueprint_path: str = rf"{blueprint_base_path}/{j.recipe_group}/{r.recommended_standard_blueprint}.txt|{r.recommended_standard_blueprint}"

    content: str = rf"""
## Blueprint

**Recommended standard blueprints**: [[{blueprint_path}]]

**Item transportation table**

| Conveyor Belt # | Direction | Item | Ratio |
| - | - | - | - |"""

    belt_counter: int = 1
    for item_name, _, ratio in r.material:
        content = f"""{content}
|{belt_counter}| Input | [[{item_name}]] | {ratio} |"""
        belt_counter += 1

    for item_name, _, ratio in r.product:
        content = f"""{content}
|{belt_counter}| Output | [[{item_name}]] | {ratio} |"""
        belt_counter += 1

    return content


def write_reference(
    r: Recipe,
    f: Facility,
    ps: list[Proliferator],
    targets: list[int],
) -> str:
    content: str = f"""
### {f.name}

The number of **{f.name}** required to satisfy different production targets (items per minute).

The square brackets represents the greatest production capacity without going over.

|Proliferation|360|720|1800|
|-|-|-|-|"""

    for p in ps:
        if r.production_speedup_only and p.name.startswith(
            "Extra Products"
        ):
            continue

        row: str = f"|{p.name}|"
        for target in targets:
            total_facilities: float = compute_facilities_required(
                target, r, f, p
            )

            per_array: int = floor(
                compute_facilities_per_array(target, r, f, p)
            )

            row = f"{row}`"

            if int(total_facilities) > per_array:
                if int(total_facilities) % per_array != 0:
                    row = f"{row}({int(total_facilities/per_array)}*{per_array})+{round(int(total_facilities) % per_array,2)}"
                else:
                    row = f"{row}{int(total_facilities/per_array)}*{per_array}"
                row = f"{row}="

            row = f"{row}{int(total_facilities)}"

            if int(total_facilities) < total_facilities:
                row = f"{row} [{round(int(total_facilities) * compute_production_per_facility(r,f,p),2)}]"
            row = f"{row}`|"

        content = f"""{content}
{row}"""

    return content


def main() -> None:
    ps: list[Proliferator] = [
        Proliferator("None", 1, 1),
        Proliferator("Extra Products +12.5%", 1.125, 1),
        Proliferator("Extra Products +20%", 1.2, 1),
        Proliferator("Extra Products +25%", 1.25, 1),
        Proliferator("Production Speedup +25%", 1, 1.25),
        Proliferator("Production Speedup +50%", 1, 1.5),
        Proliferator("Production Speedup +100%", 1, 2),
    ]

    jobs: list[Job] = [
        Job(
            recipes=RECIPE_ASSEMBLER,
            facilities=FACILITIY_ASSEMBLER,
            recipe_group="Assembler",
        ),
        Job(
            recipes=RECIPE_SMELTING,
            facilities=FACILITIY_SMELTING,
            recipe_group="Smelting",
        ),
        Job(
            recipes=RECIPE_REFINING,
            facilities=FACILITIY_REFINING,
            recipe_group="Refining",
        ),
        Job(
            recipes=RECIPE_CHEMICAL,
            facilities=FACILITIY_CHEMICAL,
            recipe_group="Chemical",
        ),
        Job(
            recipes=RECIPE_PARTICLE_COLLIDER,
            facilities=FACILITIY_PARTICLE_COLLIDER,
            recipe_group="Particle Collider",
        ),
        Job(
            recipes=RECIPE_RESEARCH,
            facilities=FACILITIY_RESEARCH,
            recipe_group="Research",
        ),
    ]

    for j in jobs:
        for r in j.recipes:
            if not path.exists(f"content/{j.recipe_group}"):
                mkdir(f"content/{j.recipe_group}")

            with open(
                f"content/{j.recipe_group}/{r.name}.md",
                mode="w+",
                encoding="utf-8",
            ) as file:
                print(f"# {r.name}", file=file)
                print(
                    write_blueprint_section(j, r),
                    file=file,
                )

                for f in j.facilities:
                    print(
                        write_reference(
                            r, f, ps, [360, 720, 1800]
                        ),
                        file=file,
                    )


if __name__ == "__main__":
    main()
