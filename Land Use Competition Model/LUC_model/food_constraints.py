# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
from LUC_model import parameters as para
from example import projections_data as proj, pre_processing as geo
from LUC_model import parcel_indices_lists as p

# We assume here that the production of crop c2 is calculated thanks to spatialized yields while the
# production of crop c1 is calculated using a theoretical yield across the island.
# However, we can work with spatialized yields for all the crops considered.

# Best case: lowest population projections
# Worst case: highest population projections


# Calculation of the food SSR for the best case
def SSR_best_constraint(mdl, t):
    return mdl.ssr_best[t] == 100 * (para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 *
                                     para.kcal_crop_c1 + mdl.production_crop_c2[t] * para.kcal_crop_c2) / \
           ((para.demand_crop_c1 * para.kcal_crop_c1 + para.demand_crop_c2 * para.kcal_crop_c2) *
            proj.household_projections_best[t])


# Calculation of the food SSR for the worst case
def SSR_worst_constraint(mdl, t):
    return mdl.ssr_worst[t] == 100 * (para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 *
                                      para.kcal_crop_c1 + mdl.production_crop_c2[t] * para.kcal_crop_c2) / \
           ((para.demand_crop_c1 * para.kcal_crop_c1 + para.demand_crop_c2 * para.kcal_crop_c2) *
            proj.household_projections_worst[t])


def production_crop_c2_constraint(mdl, t):
    return mdl.production_crop_c2[t] == para.initial_production_crop_c2 + \
           (sum(geo.yield_c2_on_export_crop_with_c2_pot[k] * mdl.s_c2_on_export_crop_with_c2_pot[t, k]
                for k in p.P_export_crop_with_c2_pot)
            + sum(geo.yield_c2_on_export_crop_with_c1_and_c2_pot[k] * mdl.s_c2_on_export_crop_with_c1_and_c2_pot[t, k]
                  for k in p.P_export_crop_with_c1_and_c2_pot)
            + sum(geo.yield_c2_on_export_crop_with_c2_and_PV_pot[k] * mdl.s_c2_on_export_crop_with_c2_and_PV_pot[t, k]
                  for k in p.P_export_crop_with_c2_and_PV_pot)
            + sum(geo.yield_c2_on_export_crop_with_PV_and_c1_and_c2_pot[k] *
                  mdl.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot[t, k]
                  for k in p.P_export_crop_with_PV_and_c1_and_c2_pot)
            + sum(geo.yield_c2_on_export_crop_with_u_and_c2_pot[k] * mdl.s_u_on_export_crop_with_u_and_c2_pot[t, k]
                  for k in p.P_export_crop_with_u_and_c2_pot) +
            sum(geo.yield_c2_on_export_crop_with_u_and_c2_and_PV_pot[k] *
                mdl.s_u_on_export_crop_with_u_and_c2_and_PV_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_pot) +
            sum(geo.yield_c2_on_export_crop_with_u_and_c2_and_c1_pot[k] *
                mdl.s_u_on_export_crop_with_u_and_c2_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_c1_pot) +
            sum(geo.yield_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[k] *
                mdl.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) +
            sum(geo.yield_c2_on_c2_pot[k] * mdl.s_c2_on_c2_pot[t, k] for k in p.P_with_c2_pot) +
            sum(geo.yield_c2_on_c1_and_c2_pot[k] * mdl.s_c2_on_c1_and_c2_pot[t, k] for k in p.P_with_c1_and_c2_pot) +
            sum(geo.yield_c2_on_c2_and_PV_pot[k] * mdl.s_c2_on_c2_and_PV_pot[t, k] for k in p.P_with_c2_and_PV_pot) +
            sum(geo.yield_c2_on_PV_and_c1_and_c2_pot[k] * mdl.s_c2_on_PV_and_c1_and_c2_pot[t, k] for k in
                p.P_with_PV_and_c1_and_c2_pot) +
            sum(geo.yield_c2_on_u_and_c2_pot[k] * mdl.s_u_on_u_and_c2_pot[t, k] for k in p.P_with_u_and_c2_pot) +
            sum(geo.yield_c2_on_u_and_c2_and_PV_pot[k] * mdl.s_u_on_u_and_c2_and_PV_pot[t, k] for k in
                p.P_with_u_and_c2_and_PV_pot) +
            sum(geo.yield_c2_on_u_and_c2_and_c1_pot[k] * mdl.s_u_on_u_and_c2_and_c1_pot[t, k] for k in
                p.P_with_u_and_c2_and_c1_pot) +
            sum(geo.yield_c2_on_u_and_c2_and_PV_and_c1_pot[k] * mdl.s_u_on_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_with_u_and_c2_and_PV_and_c1_pot)) * 0.0001


def balance_production_demand_crop_c1_best(mdl, t):
    return para.yield_crop_c1_best * mdl.s_crop_c1[t] * 0.0001 <= para.demand_crop_c1 * \
           proj.household_projections_best[t]


def balance_production_demand_crop_c1_worst(mdl, t):
    return para.yield_crop_c1_worst * mdl.s_crop_c1[t] * 0.0001 <= para.demand_crop_c1 * \
           proj.household_projections_worst[t]


def balance_production_demand_crop_c2_best(mdl, t):
    return mdl.production_crop_c2[t] <= para.demand_crop_c2 * proj.household_projections_best[t]


def balance_production_demand_crop_c2_worst(mdl, t):
    return mdl.production_crop_c2[t] <= para.demand_crop_c2 * proj.household_projections_worst[t]


# This constraint ensures that the total surface area associated to crop c1 is not decreasing
# from one time step to an other.
def surfaces_crop_c1_increasing(mdl, t):
    if t == 0:
        return mdl.s_crop_c1[t] == 0
    else:
        return mdl.s_crop_c1[t] >= mdl.s_crop_c1[t - 1]


# This constraint ensures that the total surface area associated to crop c2 is not decreasing
# from one time step to an other.
def surfaces_crop_c2_increasing(mdl, t):
    if t == 0:
        return mdl.s_crop_c2[t] == para.initial_surface_area_crop_c2
    else:
        return mdl.s_crop_c2[t] >= mdl.s_crop_c2[t - 1]


def surfaces_crop_c1(mdl, t):
    return mdl.s_crop_c1[t] == para.initial_surface_area_crop_c1 + \
           sum(mdl.s_c1_on_export_crop_with_c1_and_PV_pot[t, k] for k in p.P_export_crop_with_c1_and_PV_pot) + \
           sum(mdl.s_c1_on_c1_and_PV_pot[t, k] for k in p.P_with_c1_and_PV_pot) + \
           sum(mdl.s_c1_on_PV_and_c1_and_c2_pot[t, k] for k in p.P_with_PV_and_c1_and_c2_pot) + \
           sum(mdl.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] for k in
               p.P_export_crop_with_PV_and_c1_and_c2_pot) + \
           sum(mdl.s_c1_on_export_crop_with_c1_pot[t, k] for k in p.P_export_crop_with_c1_pot) + \
           sum(mdl.s_c1_on_export_crop_with_c1_and_c2_pot[t, k] for k in p.P_export_crop_with_c1_and_c2_pot) + \
           sum(mdl.s_c1_on_c1_pot[t, k] for k in p.P_with_c1_pot) + \
           sum(mdl.s_c1_on_c1_and_c2_pot[t, k] for k in p.P_with_c1_and_c2_pot) + \
           sum(mdl.s_c1_on_u_and_c1_pot[t, k] for k in p.P_with_u_and_c1_pot) + \
           sum(mdl.s_c1_on_export_crop_with_u_and_c1_pot[t, k] for k in p.P_export_crop_with_u_and_c1_pot) + \
           sum(mdl.s_c1_on_u_and_PV_and_c1_pot[t, k] for k in p.P_with_u_and_PV_and_c1_pot) + \
           sum(mdl.s_c1_on_export_crop_with_u_and_PV_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_PV_and_c1_pot) + \
           sum(mdl.s_c1_on_u_and_c2_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_c1_on_export_crop_with_u_and_c2_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_c1_on_u_and_c2_and_PV_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_PV_and_c1_pot) + \
           sum(mdl.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot)


def surfaces_crop_c2(mdl, t):
    return mdl.s_crop_c2[t] == para.initial_surface_area_crop_c2 + \
           sum(mdl.s_c2_on_export_crop_with_c2_pot[t, k] for k in p.P_export_crop_with_c2_pot) + \
           sum(mdl.s_c2_on_export_crop_with_c1_and_c2_pot[t, k] for k in p.P_export_crop_with_c1_and_c2_pot) + \
           sum(mdl.s_c2_on_export_crop_with_c2_and_PV_pot[t, k] for k in p.P_export_crop_with_c2_and_PV_pot) + \
           sum(mdl.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] for k in
               p.P_export_crop_with_PV_and_c1_and_c2_pot) + \
           sum(mdl.s_c2_on_c2_pot[t, k] for k in p.P_with_c2_pot) + \
           sum(mdl.s_c2_on_c1_and_c2_pot[t, k] for k in p.P_with_c1_and_c2_pot) + \
           sum(mdl.s_c2_on_c2_and_PV_pot[t, k] for k in p.P_with_c2_and_PV_pot) + \
           sum(mdl.s_c2_on_PV_and_c1_and_c2_pot[t, k] for k in p.P_with_PV_and_c1_and_c2_pot) + \
           sum(mdl.s_c2_on_u_and_c2_pot[t, k] for k in p.P_with_u_and_c2_pot) + \
           sum(mdl.s_c2_on_export_crop_with_u_and_c2_pot[t, k] for k in p.P_export_crop_with_u_and_c2_pot) + \
           sum(mdl.s_c2_on_u_and_c2_and_PV_pot[t, k] for k in p.P_with_u_and_c2_and_PV_pot) + \
           sum(mdl.s_c2_on_export_crop_with_u_and_c2_and_PV_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_PV_pot) + \
           sum(mdl.s_c2_on_u_and_c2_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_c2_on_export_crop_with_u_and_c2_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_c1_pot) + \
           sum(mdl.s_c2_on_u_and_c2_and_PV_and_c1_pot[t, k] for k in p.P_with_u_and_c2_and_PV_and_c1_pot) + \
           sum(mdl.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] for k in
               p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot)


# Constraints definition related to the function listed above
def define_constraints(model, T):
    model.SSR_best_constraint = pyo.Constraint(T, rule=SSR_best_constraint)
    model.SSR_worst_constraint = pyo.Constraint(T, rule=SSR_worst_constraint)
    model.production_crop_c2_constraint = pyo.Constraint(T, rule=production_crop_c2_constraint)
    model.balance_production_demand_crop_c1_best = pyo.Constraint(T, rule=balance_production_demand_crop_c1_best)
    model.balance_production_demand_crop_c1_worst = pyo.Constraint(T, rule=balance_production_demand_crop_c1_worst)
    model.balance_production_demand_crop_c2_best = pyo.Constraint(T, rule=balance_production_demand_crop_c2_best)
    model.balance_production_demand_crop_c2_worst = pyo.Constraint(T, rule=balance_production_demand_crop_c2_worst)
    model.surfaces_crop_c2_increasing = pyo.Constraint(T, rule=surfaces_crop_c2_increasing)
    model.surfaces_crop_c1 = pyo.Constraint(T, rule=surfaces_crop_c1)
    model.surfaces_crop_c2 = pyo.Constraint(T, rule=surfaces_crop_c2)
    model.surfaces_crop_c1_increasing = pyo.Constraint(T, rule=surfaces_crop_c1_increasing)
