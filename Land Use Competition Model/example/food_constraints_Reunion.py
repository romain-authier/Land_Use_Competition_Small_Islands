# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
from LUC_model import parcel_indices_lists as p
import projections_data as proj_data
import pre_processing as geo
import parameters_Reunion as para_reunion
from LUC_model import parameters as para

# We have the following notations:
# Crop c1: Rice
# Crop c2: Vegetables
# Crop c3: Fruits
# The index u_pot refers to the potential for urban development
# Major crop for export: Sugarcane

# Best case: lowest population projections
# Worst case: highest population projections

# For rice crop, we consider no existing production on the island and therefore a theoretical yield across the island.
# Similarly, we assume a constant theoretical yield across the island for fruits.
# The main crop for exports in Reunion is sugarcane.

# The total surface area of parcels with a potential for production of crop c2 (s_c2_pot) is calculated
s_c2_pot = sum(geo.S_export_crop_with_c2_pot[k][1] for k in p.P_export_crop_with_c2_pot) + \
           sum(geo.S_export_crop_with_c1_and_c2_pot[k][1] for k in p.P_export_crop_with_c1_and_c2_pot) + \
           sum(geo.S_export_crop_with_c2_and_PV_pot[k][1] for k in p.P_export_crop_with_c2_and_PV_pot) + \
           sum(geo.S_export_crop_with_PV_and_c1_and_c2_pot[k][1] for k in p.P_export_crop_with_PV_and_c1_and_c2_pot) + \
           sum(geo.S_with_c2_pot[k][1] for k in p.P_with_c2_pot) + \
           sum(geo.S_with_c1_and_c2_pot[k][1] for k in p.P_with_c1_and_c2_pot) + \
           sum(geo.S_with_c2_and_PV_pot[k][1] for k in p.P_with_c2_and_PV_pot) + \
           sum(geo.S_with_PV_and_c1_and_c2_pot[k][1] for k in p.P_with_PV_and_c1_and_c2_pot) + \
           sum(geo.S_with_u_and_c2_pot[k][1] for k in p.P_with_u_and_c2_pot) + \
           sum(geo.S_export_crop_with_u_and_c2_pot[k][1] for k in p.P_export_crop_with_u_and_c2_pot) + \
           sum(geo.S_with_u_and_c2_and_PV_pot[k][1] for k in p.P_with_u_and_c2_and_PV_pot) + \
           sum(geo.S_export_crop_with_u_and_c2_and_PV_pot[k][1] for k in p.P_export_crop_with_u_and_c2_and_PV_pot) + \
           sum(geo.S_with_u_and_c2_and_c1_pot[k][1] for k in p.P_with_u_and_c2_and_c1_pot) + \
           sum(geo.S_export_crop_with_u_and_c2_and_c1_pot[k][1] for k in p.P_export_crop_with_u_and_c2_and_c1_pot) + \
           sum(geo.S_with_u_and_c2_and_PV_and_c1_pot[k][1] for k in p.P_with_u_and_c2_and_PV_and_c1_pot) + \
           sum(geo.S_export_crop_with_u_and_c2_and_PV_and_c1_pot[k][1]
               for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot)

# The total surface area of parcels with a potential for production of crop c3 (s_c3_pot) is calculated.
s_c3_pot = sum(geo.S_export_crop_with_c2_pot[k10][1] for k10 in p.P_export_crop_with_c2_pot) + \
           sum(geo.S_with_c2_pot[k][1] for k in p.P_with_c2_pot) + \
           sum(geo.S_with_PV_and_c1_and_c2_pot[k][1] for k in p.P_with_PV_and_c1_and_c2_pot) + \
           sum(geo.S_with_c2_and_PV_pot[k][1] for k in p.P_with_c2_and_PV_pot)


# Addition of crop c3 in the calculation of the food SSR for the best case
def SSR_best_Reunion_constraint(mdl, t):
    return mdl.ssr_best_Reunion[t] == 100 * (para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 *
                                             para.kcal_crop_c1 + mdl.production_crop_c2[t] * para.kcal_crop_c2 +
                                             mdl.production_crop_c3[t] * para_reunion.kcal_crop_c3) / \
           ((para.demand_crop_c1 * para.kcal_crop_c1 + para.demand_crop_c2 * para.kcal_crop_c2 +
             para_reunion.demand_crop_c3 * para_reunion.kcal_crop_c3) * proj_data.household_projections_best[t])


# Addition of crop c3 in the calcul of the food SSR for the worst case
def SSR_worst_Reunion_constraint(mdl, t):
    return mdl.ssr_worst_Reunion[t] == 100 * (para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 *
                                              para.kcal_crop_c1 + mdl.production_crop_c2[t] * para.kcal_crop_c2 +
                                              mdl.production_crop_c3[t] * para_reunion.kcal_crop_c3) / \
           ((para.demand_crop_c1 * para.kcal_crop_c1 + para.demand_crop_c2 * para.kcal_crop_c2 +
             para_reunion.demand_crop_c3 * para_reunion.kcal_crop_c3) * proj_data.household_projections_worst[t])


# This constraint ensures that not all the potential areas for the production of crop c1 are converted into
# producing parcels at the beginning of the simulation.
def surfaces_crop_c1_limit(mdl, t):
    if t == 0:
        return mdl.s_crop_c1[t] == para_reunion.crop_c1_surface_limit[0]
    if t == 1:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[1]
    if t == 2:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[2]
    if t == 3:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[3]
    if t == 4:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[4]
    if t == 5:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[5]
    if t == 6:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[6]
    if t == 7:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[7]
    if t == 8:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[8]
    if t > 8:
        return mdl.s_crop_c1[t] <= para_reunion.crop_c1_surface_limit[9]


# This constraint ensures that not all the potential areas for the production of crop c2 are converted into
# producing parcels at the beginning of the simulation.
def surfaces_crop_c2_limit(mdl, t):
    if t == 0:
        return mdl.s_crop_c2[t] == para.initial_surface_area_crop_c2
    if t == 1:
        return mdl.s_crop_c2[t] <= para.initial_surface_area_crop_c2 + 0.1 * s_c2_pot
    if t == 2:
        return mdl.s_crop_c2[t] <= para.initial_surface_area_crop_c2 + 0.5 * s_c2_pot
    if t >= 3:
        return mdl.s_crop_c2[t] <= para.initial_surface_area_crop_c2 + s_c2_pot


# This constraint ensures that the total surface area associated to crop c3 is not decreasing
# from one time step to an other.
def surfaces_crop_c3_increasing(mdl, t):
    if t == 0:
        return mdl.s_crop_c3[t] == para_reunion.initial_surface_area_crop_c3
    else:
        return mdl.s_crop_c3[t] >= mdl.s_crop_c3[t - 1]


def surfaces_crop_c3(mdl, t):
    return mdl.s_crop_c3[t] == para_reunion.initial_surface_area_crop_c3 + \
           sum(mdl.s_c3_on_export_crop_with_c3_pot[t, k] for k in p.P_export_crop_with_c2_pot) + \
           sum(mdl.s_c3_on_c3_pot[t, k] for k in p.P_with_c2_pot) + \
           sum(mdl.s_c3_on_c3_and_PV_and_c1_pot[t, k] for k in p.P_with_PV_and_c1_and_c2_pot) + \
           sum(mdl.s_c3_on_c3_and_PV_pot[t, k] for k in p.P_with_c2_and_PV_pot)


def production_crop_c3_constraint(mdl, t):
    return mdl.production_crop_c3[t] == para_reunion.initial_production_crop_c3 + \
           (sum(mdl.s_c3_on_export_crop_with_c3_pot[t, k] for k in p.P_export_crop_with_c2_pot) +
            sum(mdl.s_c3_on_c3_pot[t, k] for k in p.P_with_c2_pot) +
            sum(mdl.s_c3_on_c3_and_PV_and_c1_pot[t, k] for k in p.P_with_PV_and_c1_and_c2_pot) +
            sum(mdl.s_c3_on_c3_and_PV_pot[t, k] for k in p.P_with_c2_and_PV_pot)) * para_reunion.yield_crop_c3 * 0.0001


def balance_production_demand_crop_c3_best(mdl, t):
    return mdl.production_crop_c3[t] <= para_reunion.demand_crop_c3 * proj_data.household_projections_best[t]


def balance_production_demand_crop_c3_worst(mdl, t):
    return mdl.production_crop_c3[t] <= para_reunion.demand_crop_c3 * proj_data.household_projections_worst[t]


# This constraint ensures that not all the potential areas for the production of crop c3 are converted into
# producing parcels at the beginning of the simulation.
def surfaces_crop_c3_limit(mdl, t):
    if t == 0:
        return mdl.s_crop_c3[t] == para_reunion.initial_surface_area_crop_c3
    if t == 1:
        return mdl.s_crop_c3[t] <= para_reunion.initial_surface_area_crop_c3 + 0.1 * s_c3_pot
    if t == 2:
        return mdl.s_crop_c3[t] <= para_reunion.initial_surface_area_crop_c3 + 0.5 * s_c3_pot
    if t >= 3:
        return mdl.s_crop_c3[t] <= para_reunion.initial_surface_area_crop_c3 + s_c3_pot


# Constraints definition related to the function listed above
def define_constraints(model, T):
    model.ssr_best_Reunion_constraint = pyo.Constraint(T, rule=SSR_best_Reunion_constraint)
    model.ssr_worst_Reunion_constraint = pyo.Constraint(T, rule=SSR_worst_Reunion_constraint)
    model.production_crop_c3_constraint = pyo.Constraint(T, rule=production_crop_c3_constraint)
    model.balance_production_demand_crop_c3_best = pyo.Constraint(T, rule=balance_production_demand_crop_c3_best)
    model.balance_production_demand_crop_c3_worst = pyo.Constraint(T, rule=balance_production_demand_crop_c3_worst)
    model.surfaces_crop_c3_increasing = pyo.Constraint(T, rule=surfaces_crop_c3_increasing)
    model.surfaces_crop_c3 = pyo.Constraint(T, rule=surfaces_crop_c3)
    model.surfaces_crop_c1_limit = pyo.Constraint(T, rule=surfaces_crop_c1_limit)
    model.surfaces_crop_c2_limit = pyo.Constraint(T, rule=surfaces_crop_c2_limit)
    model.surfaces_crop_c3_limit = pyo.Constraint(T, rule=surfaces_crop_c3_limit)
