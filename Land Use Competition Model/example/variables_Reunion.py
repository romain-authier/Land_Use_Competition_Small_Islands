# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
from LUC_model import parcel_indices_lists as p

# We have the following notations:
# Crop c1: Rice
# Crop c2: Vegetables
# Crop c3: Fruits
# The index u_pot refers to the potential for urban development
# Major crop for export: Sugarcane


def define_variables(model, T):

    # Definition of surface variables for crop c3
    model.s_c3_on_export_crop_with_c3_pot = pyo.Var(T, p.P_export_crop_with_c2_pot, initialize=0)
    model.s_c3_on_c3_pot = pyo.Var(T, p.P_with_c2_pot, initialize=0)
    model.s_c3_on_c3_and_PV_pot = pyo.Var(T, p.P_with_c2_and_PV_pot, initialize=0)
    model.s_c3_on_c3_and_PV_and_c1_pot = pyo.Var(T, p.P_with_PV_and_c1_and_c2_pot, initialize=0)
    model.s_crop_c3 = pyo.Var(T)

    # Definition of production variable for crop c3
    model.production_crop_c3 = pyo.Var(T)

    # Definition of SSR for Reunion
    model.ssr_best_Reunion = pyo.Var(T)
    model.ssr_worst_Reunion = pyo.Var(T)

    # Definition of additional variables according to scenarios (new variables only related to the introduction of
    # various dietary behaviors)
    model.ssr_mediterranean_best_Reunion = pyo.Var(T)
    model.ssr_mediterranean_worst_Reunion = pyo.Var(T)
    model.ssr_traditional_best_Reunion = pyo.Var(T)
    model.ssr_traditional_worst_Reunion = pyo.Var(T)
