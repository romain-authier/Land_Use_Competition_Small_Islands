# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
from LUC_model import parameters as para
from LUC_model import parcel_indices_lists as p

# Best case: lowest population projections
# Worst case: highest population projections


def define_variables(model, T):
    # Variables depicting the food SSR
    model.ssr_best = pyo.Var(T)
    model.ssr_worst = pyo.Var(T)

    # Surface variables
    # Surfaces related to the cultivation of crop c1 and c2
    model.s_crop_c1 = pyo.Var(T)
    model.s_crop_c2 = pyo.Var(T)

    # Agricultural surfaces generating biomass (agricultural residues)
    model.s_biomass = pyo.Var(T)

    # Urban development surfaces
    model.s_urban_development = pyo.Var(T, initialize=0)

    # Urban surfaces for solar self-consumption (through the installation of PV panels on the roofs)
    model.s_urban_for_solar_self_consumption = pyo.Var(T, p.P_urb_solar_self_consumption, initialize=0)

    # Agricultural surfaces (related to the export crop) with a single potential land use
    model.s_u_on_export_crop_with_u_pot = pyo.Var(T, p.P_export_crop_with_u_pot, initialize=0)
    model.s_PV_on_export_crop_with_PV_pot = pyo.Var(T, p.P_export_crop_with_PV_pot, initialize=0)
    model.s_c1_on_export_crop_with_c1_pot = pyo.Var(T, p.P_export_crop_with_c1_pot, initialize=0)
    model.s_c2_on_export_crop_with_c2_pot = pyo.Var(T, p.P_export_crop_with_c2_pot, initialize=0)

    # Non-agricultural surfaces with a single potential land use
    model.s_c1_on_c1_pot = pyo.Var(T, p.P_with_c1_pot, initialize=0)
    model.s_c2_on_c2_pot = pyo.Var(T, p.P_with_c2_pot, initialize=0)
    model.s_u_on_u_pot = pyo.Var(T, p.P_with_u_pot, initialize=0)
    model.s_PV_on_PV_pot = pyo.Var(T, p.P_with_PV_pot, initialize=0)

    # Agricultural surfaces (related to the export crop) with 2 potential land uses
    model.s_c1_on_export_crop_with_c1_and_PV_pot = pyo.Var(T, p.P_export_crop_with_c1_and_PV_pot, initialize=0)
    model.s_PV_on_export_crop_with_c1_and_PV_pot = pyo.Var(T, p.P_export_crop_with_c1_and_PV_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_PV_pot = pyo.Var(T, p.P_export_crop_with_u_and_PV_pot, initialize=0)
    model.s_PV_on_export_crop_with_u_and_PV_pot = pyo.Var(T, p.P_export_crop_with_u_and_PV_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_c1_pot = pyo.Var(T, p.P_export_crop_with_u_and_c1_pot, initialize=0)
    model.s_c1_on_export_crop_with_u_and_c1_pot = pyo.Var(T, p.P_export_crop_with_u_and_c1_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_c2_pot = pyo.Var(T, p.P_export_crop_with_u_and_c2_pot, initialize=0)
    model.s_c2_on_export_crop_with_u_and_c2_pot = pyo.Var(T, p.P_export_crop_with_u_and_c2_pot, initialize=0)
    model.s_c2_on_export_crop_with_c2_and_PV_pot = pyo.Var(T, p.P_export_crop_with_c2_and_PV_pot, initialize=0)
    model.s_PV_on_export_crop_with_c2_and_PV_pot = pyo.Var(T, p.P_export_crop_with_c2_and_PV_pot, initialize=0)
    model.s_c1_on_export_crop_with_c1_and_c2_pot = pyo.Var(T, p.P_export_crop_with_c1_and_c2_pot, initialize=0)
    model.s_c2_on_export_crop_with_c1_and_c2_pot = pyo.Var(T, p.P_export_crop_with_c1_and_c2_pot, initialize=0)

    # Non-agricultural surfaces with 2 potential land uses
    model.s_c1_on_c1_and_PV_pot = pyo.Var(T, p.P_with_c1_and_PV_pot, initialize=0)
    model.s_PV_on_c1_and_PV_pot = pyo.Var(T, p.P_with_c1_and_PV_pot, initialize=0)
    model.s_c2_on_c2_and_PV_pot = pyo.Var(T, p.P_with_c2_and_PV_pot, initialize=0)
    model.s_PV_on_c2_and_PV_pot = pyo.Var(T, p.P_with_c2_and_PV_pot, initialize=0)
    model.s_c1_on_c1_and_c2_pot = pyo.Var(T, p.P_with_c1_and_c2_pot, initialize=0)
    model.s_c2_on_c1_and_c2_pot = pyo.Var(T, p.P_with_c1_and_c2_pot, initialize=0)
    model.s_u_on_u_and_PV_pot = pyo.Var(T, p.P_with_u_and_PV_pot, initialize=0)
    model.s_PV_on_u_and_PV_pot = pyo.Var(T, p.P_with_u_and_PV_pot, initialize=0)
    model.s_u_on_u_and_c1_pot = pyo.Var(T, p.P_with_u_and_c1_pot, initialize=0)
    model.s_c1_on_u_and_c1_pot = pyo.Var(T, p.P_with_u_and_c1_pot, initialize=0)
    model.s_u_on_u_and_c2_pot = pyo.Var(T, p.P_with_u_and_c2_pot, initialize=0)
    model.s_c2_on_u_and_c2_pot = pyo.Var(T, p.P_with_u_and_c2_pot, initialize=0)

    # Agricultural surfaces (related to the export crop) with 3 potential land uses
    model.s_PV_on_export_crop_with_PV_and_c1_and_c2_pot = \
        pyo.Var(T, p.P_export_crop_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot = \
        pyo.Var(T, p.P_export_crop_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot = \
        pyo.Var(T, p.P_export_crop_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_PV_on_export_crop_with_u_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_c1_on_export_crop_with_u_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_c2_and_PV_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_PV_on_export_crop_with_u_and_c2_and_PV_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_c2_on_export_crop_with_u_and_c2_and_PV_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_u_on_export_crop_with_u_and_c2_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_c1_pot, initialize=0)
    model.s_c2_on_export_crop_with_u_and_c2_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_c1_pot, initialize=0)
    model.s_c1_on_export_crop_with_u_and_c2_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_c1_pot, initialize=0)

    # Non-agricultural surfaces with 3 potential land uses
    model.s_PV_on_PV_and_c1_and_c2_pot = pyo.Var(T, p.P_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_c1_on_PV_and_c1_and_c2_pot = pyo.Var(T, p.P_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_c2_on_PV_and_c1_and_c2_pot = pyo.Var(T, p.P_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_u_on_u_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_PV_on_u_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_c1_on_u_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_PV_and_c1_pot, initialize=0)
    model.s_u_on_u_and_c2_and_PV_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_PV_on_u_and_c2_and_PV_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_c2_on_u_and_c2_and_PV_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_pot, initialize=0)
    model.s_u_on_u_and_c2_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_c1_pot, initialize=0)
    model.s_c2_on_u_and_c2_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_c1_pot, initialize=0)
    model.s_c1_on_u_and_c2_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_c1_pot, initialize=0)

    # Agricultural surfaces (related to the export crop) with 4 potential land uses
    model.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_PV_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = \
        pyo.Var(T, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot, initialize=0)

    # Non-agricultural surfaces with 4 potential land uses
    model.s_u_on_u_and_c2_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_c2_on_u_and_c2_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_c1_on_u_and_c2_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_and_c1_pot, initialize=0)
    model.s_PV_on_u_and_c2_and_PV_and_c1_pot = pyo.Var(T, p.P_with_u_and_c2_and_PV_and_c1_pot, initialize=0)

    # Production variables
    # Electricity production variables
    model.p_elec = pyo.Var(T)
    model.p_coal = pyo.Var(T, initialize=para.p_coal_year_basis, bounds=(0, para.p_coal_year_basis))
    model.p_oil = pyo.Var(T, initialize=para.p_oil_year_basis, bounds=(0, para.p_oil_year_basis))
    model.p_hydro = pyo.Var(T, initialize=para.p_hydro_year_basis)
    model.p_biomass = pyo.Var(T)
    model.p_ground_mounted_PV = pyo.Var(T, initialize=para.p_ground_mounted_PV_year_basis)
    model.p_wind = pyo.Var(T, initialize=para.p_wind_year_basis)
    model.p_imported_biomass = pyo.Var(T, initialize=para.p_imported_biomass_year_basis)
    model.p_solar_self_consumption = pyo.Var(T, initialize=para.p_solar_self_consumption_year_basis)

    # Food production variables related to crops c1 and c2
    model.production_crop_c1 = pyo.Var(T)
    model.production_crop_c2 = pyo.Var(T)


