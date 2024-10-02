# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
import parameters_Reunion as para_reunion
from LUC_model import parameters as para
import projections_data as proj_data

# We have the following notations:
# Crop c1: Rice
# Crop c2: Vegetables
# Crop c3: Fruits
# The index u_pot refers to the potential for urban development
# Major crop for export: Sugarcane

# Best case: lowest population projections
# Worst case: highest population projections

# The following constraints described below are to activate or deactivate depending on a specific case the user wants to
# study (defined as scenarios). The scenarios involve (1) dietary behaviors, (2) urban development dynamics, and (3)
# electricity production from various energy sources.


# Constraint to activate for a scenario that considers no biomass imports throughout the simulation process and to
# deactivate if we consider biomass imports during the planning horizon.
def no_biomass_imports(model, t):
    if t == 0:
        return model.p_imported_biomass[t] == para.p_imported_biomass_year_basis
    else:
        return model.p_imported_biomass[t] == 0


# Constraint to activate for a scenario that considers biomass imports from a certain time period (for example from t=4
# here) and to deactivate if we consider no biomass imports during the planning horizon.
def biomass_imports(model, t):
    if t == 0:
        return model.p_imported_biomass[t] == para.p_imported_biomass_year_basis
    if 1 <= t <= 3:
        return model.p_imported_biomass[t] == 0
    if t >= 4:
        return model.p_imported_biomass[t] >= 0


# Constraint related to the disconnection threshold due to high share of intermittent RE in the electricity mix in
# islands systems. It has to be activated for a scenario that considers high electricity production from
# ground-mounted PV during the planning horizon and deactivated otherwise.
def share_intermittent_RE_high(model, t):
    return model.p_ground_mounted_PV[t] + model.p_wind[t] <= \
           para.disconnection_threshold_intermittent_RE_high * model.p_elec[t]


# Constraint to activate for a scenario that considers low electricity production from ground-mounted PV during the
# planning horizon and deactivated otherwise.
def share_intermittent_RE_low(model, t):
    return model.p_ground_mounted_PV[t] + model.p_wind[t] <= \
           para.disconnection_threshold_intermittent_RE_low * model.p_elec[t]


# Calculation of a food SSR (expressed in %) for a dietary behavior directed towards a mediterranean profile for the
# best case. Function to maximize for assessing the impact of mediterranean diet on food SSR and other objective
# functions to deactivate in both folders.
def SSR_mediterranean_diet_best(mdl, t):
    return 100 * (para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 * para.kcal_crop_c1 +
                  mdl.production_crop_c2[t] * para.kcal_crop_c2 + mdl.production_crop_c3[t] *
                  para_reunion.kcal_crop_c3) / ((para_reunion.demand_crop_c1_med * para.kcal_crop_c1 +
                                                 para_reunion.demand_crop_c2_med * para.kcal_crop_c2 +
                                                 para_reunion.demand_crop_c3_med * para_reunion.kcal_crop_c3) *
                                                proj_data.household_projections_best[t]) == \
           mdl.ssr_mediterranean_best_Reunion[t]


# For the worst case:
def SSR_mediterranean_diet_worst(mdl, t):
    return 100 * (para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 * para.kcal_crop_c1 +
                  mdl.production_crop_c2[t] * para.kcal_crop_c2 + mdl.production_crop_c3[t] *
                  para_reunion.kcal_crop_c3) / ((para_reunion.demand_crop_c1_med * para.kcal_crop_c1 +
                                                 para_reunion.demand_crop_c2_med * para.kcal_crop_c2 +
                                                 para_reunion.demand_crop_c3_med * para_reunion.kcal_crop_c3) *
                                                proj_data.household_projections_worst[t]) == \
           mdl.ssr_mediterranean_worst_Reunion[t]


# Calculation of a food SSR (expressed in %) for a dietary behavior directed towards a traditional profile for the
# best case. Function to maximize for assessing the impact of traditional diet on food SSR and other objective functions
# to deactivate in both folders.
def SSR_traditional_diet_best(mdl, t):
    return 100 * (para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 * para.kcal_crop_c1 +
                  mdl.production_crop_c2[t] * para.kcal_crop_c2 + mdl.production_crop_c3[t] *
                  para_reunion.kcal_crop_c3) / ((para_reunion.demand_crop_c1_trad * para.kcal_crop_c1 +
                                                 para_reunion.demand_crop_c2_trad * para.kcal_crop_c2 +
                                                 para_reunion.demand_crop_c3_trad * para_reunion.kcal_crop_c3) *
                                                proj_data.household_projections_best[t]) == \
           mdl.ssr_traditional_best_Reunion[t]


# For the worst case:
def SSR_traditional_diet_worst(mdl, t):
    return 100 * (para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 * para.kcal_crop_c1 +
                  mdl.production_crop_c2[t] * para.kcal_crop_c2 + mdl.production_crop_c3[t] *
                  para_reunion.kcal_crop_c3) / ((para_reunion.demand_crop_c1_trad * para.kcal_crop_c1 +
                                                 para_reunion.demand_crop_c2_trad * para.kcal_crop_c2 +
                                                 para_reunion.demand_crop_c3_trad * para_reunion.kcal_crop_c3) *
                                                proj_data.household_projections_worst[t]) == \
           mdl.ssr_traditional_worst_Reunion[t]


# Constraint to activate when considering mediterranean food profile for the best case and deactivate the other
# constraints related to the balance between food production and demand for non-mediterranean diet in both folders.
def balance_production_demand_crop_c1_mediterranean_diet_best(mdl, t):
    return para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 <= para_reunion.demand_crop_c1_med * \
           proj_data.household_projections_best[t]


# For the worst case:
def balance_production_demand_crop_c1_mediterranean_diet_worst(mdl, t):
    return para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 <= para_reunion.demand_crop_c1_med * \
           proj_data.household_projections_worst[t]


# Constraint to activate when considering mediterranean food profile for the best case and deactivate the other
# constraints related to the balance between food production and demand for non-mediterranean diet in both folders.
def balance_production_demand_crop_c2_mediterranean_diet_best(mdl, t):
    return mdl.production_crop_c2[t] <= para_reunion.demand_crop_c2_med * proj_data.household_projections_best[t]


# For the worst case:
def balance_production_demand_crop_c2_mediterranean_diet_worst(mdl, t):
    return mdl.production_crop_c2[t] <= para_reunion.demand_crop_c2_med * proj_data.household_projections_worst[t]


# Constraint to activate when considering mediterranean food profile for the best case and deactivate the other
# constraints related to the balance between food production and demand for non-mediterranean diet in both folders.
def balance_production_demand_crop_c3_mediterranean_diet_best(mdl, t):
    return mdl.production_crop_c3[t] <= para_reunion.demand_crop_c3_med * proj_data.household_projections_best[t]


# For the worst case:
def balance_production_demand_crop_c3_mediterranean_diet_worst(mdl, t):
    return mdl.production_crop_c3[t] <= para_reunion.demand_crop_c3_med * proj_data.household_projections_worst[t]

# The 6 constraints above can be formulated similarly for the traditional diet.


# Constraint to activate when considering high urban planning for the best case and
# deactivate the other constraints related to urban development dynamics in both folders.
def urban_development_surfaces_high_planning_best_case(mdl, t):
    return mdl.s_urban_development[t] >= para_reunion.urban_extension_area_per_household_high_planning * \
           (proj_data.household_projections_best[t] - proj_data.household_projections_best[0]) + \
           para_reunion.urban_extension_surfaces_non_residential_high_planning


# For the worst case:
def urban_development_surfaces_high_planning_worst_case(mdl, t):
    return mdl.s_urban_development[t] >= para_reunion.urban_extension_area_per_household_high_planning * \
           (proj_data.household_projections_worst[t] - proj_data.household_projections_worst[0]) + \
           para_reunion.urban_extension_surfaces_non_residential_high_planning


# Constraint to activate when considering low urban planning for the best case and
# deactivate the other constraints related to urban development dynamics in both folders.
def urban_development_surfaces_low_planning_best_case(mdl, t):
    return mdl.s_urban_development[t] >= para_reunion.urban_extension_area_per_household_low_planning * (
            proj_data.household_projections_best[t] - proj_data.household_projections_best[0]) + \
           para_reunion.urban_extension_surfaces_non_residential_low_planning


# For the worst case:
def urban_development_surfaces_low_planning_worst_case(mdl, t):
    return mdl.s_urban_development[t] >= para_reunion.urban_extension_area_per_household_low_planning * (
            proj_data.household_projections_worst[t] - proj_data.household_projections_worst[0]) + \
           para_reunion.urban_extension_surfaces_non_residential_low_planning


# Constraints definition related to the functions listed above
def define_constraints(model, T):
    model.biomass_imports = pyo.Constraint(T, rule=biomass_imports)
    model.no_biomass_imports = pyo.Constraint(T, rule=no_biomass_imports)
    model.share_intermittent_RE_high = pyo.Constraint(T, rule=share_intermittent_RE_high)
    model.share_intermittent_RE_low = pyo.Constraint(T, rule=share_intermittent_RE_low)
    model.SSR_mediterranean_diet_best = pyo.Constraint(T, rule=SSR_mediterranean_diet_best)
    model.SSR_mediterranean_diet_worst = pyo.Constraint(T, rule=SSR_mediterranean_diet_worst)
    model.SSR_traditional_diet_worst = pyo.Constraint(T, rule=SSR_traditional_diet_worst)
    model.SSR_traditional_diet_best = pyo.Constraint(T, rule=SSR_traditional_diet_best)
    model.balance_production_demand_crop_c3_mediterranean_diet_worst = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c3_mediterranean_diet_worst)
    model.balance_production_demand_crop_c3_mediterranean_diet_best = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c3_mediterranean_diet_best)
    model.balance_production_demand_crop_c2_mediterranean_diet_worst = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c2_mediterranean_diet_worst)
    model.balance_production_demand_crop_c2_mediterranean_diet_best = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c2_mediterranean_diet_best)
    model.balance_production_demand_crop_c1_mediterranean_diet_worst = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c1_mediterranean_diet_worst)
    model.balance_production_demand_crop_c1_mediterranean_diet_best = \
        pyo.Constraint(T, rule=balance_production_demand_crop_c1_mediterranean_diet_best)
    model.urban_development_surfaces_low_planning_best_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_low_planning_best_case)
    model.urban_development_surfaces_low_planning_worst_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_low_planning_worst_case)
    model.urban_development_surfaces_high_planning_best_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_high_planning_best_case)
    model.urban_development_surfaces_high_planning_worst_case = \
        pyo.Constraint(T, rule=urban_development_surfaces_high_planning_worst_case)
