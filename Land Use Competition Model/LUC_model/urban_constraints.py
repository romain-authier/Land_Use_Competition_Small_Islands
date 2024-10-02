# Import of the optimization package pyomo
import pyomo.environ as pyo

# Import of useful python files
from LUC_model import parcel_indices_lists as p
from example import projections_data as proj_data
from LUC_model import parameters as para

# Best case: lowest population projections
# Worst case: highest population projections


# Calculation of urban development surfaces according to potential areas for urban development
def urban_development_surfaces(mdl, t):
    return mdl.s_urban_development[t] == sum(mdl.s_u_on_u_pot[t, k] for k in p.P_with_u_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_pot[t, k] for k in p.P_export_crop_with_u_pot) + \
           sum(mdl.s_u_on_u_and_PV_pot[t, k] for k in p.P_with_u_and_PV_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_PV_pot[t, k] for k in p.P_export_crop_with_u_and_PV_pot) + \
           sum(mdl.s_u_on_u_and_c1_pot[t, k] for k in p.P_with_u_and_c1_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_c1_pot[t, k] for k in p.P_export_crop_with_u_and_c1_pot) + \
           sum(mdl.s_u_on_u_and_c2_pot[t, k] for k in p.P_with_u_and_c2_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_c2_pot[t, k] for k in p.P_export_crop_with_u_and_c2_pot) + \
           sum(mdl.s_u_on_u_and_PV_and_c1_pot[t, k] for k in p.P_with_u_and_PV_and_c1_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_PV_and_c1_pot[t, k]
               for k in p.P_export_crop_with_u_and_PV_and_c1_pot) + \
           sum(mdl.s_u_on_u_and_c2_and_PV_pot[t, k] for k in p.P_with_u_and_c2_and_PV_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_c2_and_PV_pot[t, k]
               for k in p.P_export_crop_with_u_and_c2_and_PV_pot) + \
           sum(mdl.s_u_on_u_and_c2_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_c2_and_c1_pot[t, k]
               for k in p.P_export_crop_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_u_on_u_and_c2_and_PV_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_PV_and_c1_pot) + \
           sum(mdl.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot)


# Constraint on the limitation of urban development within designated zones in case of medium urban planning
# for the best case
def urban_development_surfaces_medium_planning_best_case(mdl, t):
    return mdl.s_urban_development[t] >= para.urban_extension_area_per_household_medium_planning * \
           (proj_data.household_projections_best[t] - proj_data.household_projections_best[0]) + \
           para.urban_extension_surfaces_non_residential_medium_planning


# For the worst case:
def urban_development_surfaces_medium_planning_worst_case(mdl, t):
    return mdl.s_urban_development[t] >= para.urban_extension_area_per_household_medium_planning * \
           (proj_data.household_projections_worst[t] - proj_data.household_projections_worst[0]) + \
           para.urban_extension_surfaces_non_residential_medium_planning


# Constraints definition related to the functions listed above
def define_constraints(model, T):
    model.urban_development_surfaces = pyo.Constraint(T, rule=urban_development_surfaces)
    model.urban_development_surfaces_medium_planning_best_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_medium_planning_best_case)
    model.urban_development_surfaces_medium_planning_worst_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_medium_planning_worst_case)
