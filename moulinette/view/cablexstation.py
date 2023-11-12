"""Default, empty instance visualization tool."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from model import *

IMPORT_DICT = {
    # 'NOM_DE_LA_CLASSE' : Classe correspondante
    'land_substation_cable_types'           : "Q0",
    'wind_turbines'                         : "Turbines",
    'wind_scenarios'                        : "Scenarios",
    'substation_locations'                  : "LieuStation",
    'substation_types'                      : "S_types",
    'general_parameters'                    : "Param",
    'substation_substation_cable_types'     : "QS",
}


def view(instance: Instance):
    """Do nothing."""
    ## TODO TODO vue par défaut
    # for scenario in instance.wind_scenarios:
    #     print(f"id={scenario.id: >4} ; power_generation =")

    lll = []
    for station_type in instance.substation_types:
        for cable_type in instance.land_substation_cable_types:
            lll.append(StationXCableType(station_type, cable_type))

    l_proba = [sxc.probability_of_failure for sxc in lll]
    l_rating = [sxc.rating for sxc in lll]
    l_id = [str(divmod(sxc.id, 1000)) for sxc in lll]
    l_cost = [sxc.fixed_cost for sxc in lll]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(l_proba, l_rating, l_cost)
    ax.set_xlabel("proba")
    ax.set_ylabel("rating")
    ax.set_zlabel("fixed_cost")

    for x, y, z, txt in zip(l_proba, l_rating, l_cost, l_id):
        ax.text(x, y, z, txt)

    fig.suptitle("Types d'ensemble Câbles terre <-> Station x Stations")

    plt.show()


