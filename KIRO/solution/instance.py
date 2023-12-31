from dataclasses import dataclass

from KIRO.structures import (
    LandSubstationCableType, 
    WindTurbine, 
    WindScenario, 
    SubstationLocation, 
    SubstationType, 
    Parameters, 
    SubstationSubstationCableType
)

@dataclass
class Instance:
    land_substation_cable_types: list[LandSubstationCableType]
    wind_turbines: list[WindTurbine]
    wind_scenarios: list[WindScenario]
    substation_locations: list[SubstationLocation]
    substation_types: list[SubstationType]
    general_parameters: Parameters
    substation_substation_cable_types: list[SubstationSubstationCableType]
