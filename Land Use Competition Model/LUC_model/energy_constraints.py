# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files
from LUC_model import parameters as para
from example import projections_data as proj, pre_processing as geo
from LUC_model import parcel_indices_lists as p


# Electricity production from various energy sources
def electricity_production(model, t):
    return model.p_coal[t] + model.p_oil[t] + model.p_hydro[t] + model.p_biomass[t] + model.p_imported_biomass[t] + \
           model.p_wind[t] + model.p_solar_self_consumption[t] + model.p_ground_mounted_PV[t] == model.p_elec[t]


# Electricity production has to meet demand while considering electrical losses for the best case
# scenario (accounting for 10 % losses)
def balance_production_demand_lower_best(model, t):
    if t == 0:
        return model.p_elec[t] == model.p_coal[t] + model.p_oil[t] + model.p_hydro[t] + model.p_biomass[t] + \
               model.p_imported_biomass[t] + model.p_wind[t] + model.p_solar_self_consumption[t] + \
               model.p_ground_mounted_PV[t]
    else:
        return model.p_elec[t] >= 1.1 * (proj.electricity_demand_projections_best[t] +
                                         para.elec_consumption_year_basis - para.domestic_elec_consumption_year_basis)


# No excess production has to be considered (upper limit) for the best case
def balance_production_demand_upper_best(model, t):
    if t == 0:
        return model.p_elec[t] == model.p_coal[t] + model.p_oil[t] + model.p_hydro[t] + model.p_biomass[t] + \
               model.p_imported_biomass[t] + model.p_wind[t] + model.p_solar_self_consumption[t] + \
               model.p_ground_mounted_PV[t]
    else:
        return model.p_elec[t] <= 1.15 * (proj.electricity_demand_projections_best[t] +
                                          para.elec_consumption_year_basis - para.domestic_elec_consumption_year_basis)


# Electricity production has to meet demand while considering electrical losses for the worst case
# scenario (accounting for 10 % losses)
def balance_production_demand_lower_worst(model, t):
    if t == 0:
        return model.p_elec[t] == model.p_coal[t] + model.p_oil[t] + model.p_hydro[t] + model.p_biomass[t] + \
               model.p_imported_biomass[t] + model.p_wind[t] + model.p_solar_self_consumption[t] + \
               model.p_ground_mounted_PV[t]
    else:
        return model.p_elec[t] >= 1.1 * (proj.electricity_demand_projections_worst[t] +
                                         para.elec_consumption_year_basis - para.domestic_elec_consumption_year_basis)


# No excess production has to be considered (upper limit) for the worst case
def balance_production_demand_upper_worst(model, t):
    if t == 0:
        return model.p_elec[t] == model.p_coal[t] + model.p_oil[t] + model.p_hydro[t] + model.p_biomass[t] + \
               model.p_imported_biomass[t] + model.p_wind[t] + model.p_solar_self_consumption[t] + \
               model.p_ground_mounted_PV[t]
    else:
        return model.p_elec[t] <= 1.15 * (proj.electricity_demand_projections_worst[t] +
                                          para.elec_consumption_year_basis - para.domestic_elec_consumption_year_basis)


# We consider biomass from the residues of the major export crop.
def biomass_surfaces(model, t):
    return model.s_biomass[t] == geo.S_export_crop_initial - (
            sum(model.s_c1_on_export_crop_with_c1_pot[t, k] for k in p.P_export_crop_with_c1_pot) +
            sum(model.s_PV_on_export_crop_with_PV_pot[t, k] for k in p.P_export_crop_with_PV_pot) +
            sum(model.s_c2_on_export_crop_with_c2_pot[t, k] for k in p.P_export_crop_with_c2_pot) +
            sum(model.s_u_on_export_crop_with_u_pot[t, k] for k in p.P_export_crop_with_u_pot) +
            sum(model.s_PV_on_export_crop_with_c1_and_PV_pot[t, k] for k in p.P_export_crop_with_c1_and_PV_pot) +
            sum(model.s_u_on_export_crop_with_u_and_PV_pot[t, k] for k in p.P_export_crop_with_u_and_PV_pot) +
            sum(model.s_PV_on_export_crop_with_u_and_PV_pot[t, k] for k in p.P_export_crop_with_u_and_PV_pot) +
            sum(model.s_u_on_export_crop_with_u_and_c1_pot[t, k] for k in p.P_export_crop_with_u_and_c1_pot) +
            sum(model.s_c1_on_export_crop_with_u_and_c1_pot[t, k] for k in p.P_export_crop_with_u_and_c1_pot) +
            sum(model.s_u_on_export_crop_with_u_and_c2_pot[t, k] for k in p.P_export_crop_with_u_and_c2_pot) +
            sum(model.s_c2_on_export_crop_with_u_and_c2_pot[t, k] for k in p.P_export_crop_with_u_and_c2_pot) +
            sum(model.s_u_on_export_crop_with_u_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_PV_and_c1_pot) +
            sum(model.s_PV_on_export_crop_with_u_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_PV_and_c1_pot) +
            sum(model.s_c1_on_export_crop_with_u_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_PV_and_c1_pot) +
            sum(model.s_u_on_export_crop_with_u_and_c2_and_PV_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_pot) +
            sum(model.s_PV_on_export_crop_with_u_and_c2_and_PV_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_pot) +
            sum(model.s_c2_on_export_crop_with_u_and_c2_and_PV_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_pot) +
            sum(model.s_u_on_export_crop_with_u_and_c2_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_c1_pot) +
            sum(model.s_c2_on_export_crop_with_u_and_c2_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_c1_pot) +
            sum(model.s_c1_on_export_crop_with_u_and_c2_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_c1_pot) +
            sum(model.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) +
            sum(model.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) +
            sum(model.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) +
            sum(model.s_PV_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k]
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) +
            sum(model.s_c1_on_export_crop_with_c1_and_PV_pot[t, k] for k in p.P_export_crop_with_c1_and_PV_pot) +
            sum(model.s_c2_on_export_crop_with_c2_and_PV_pot[t, k] for k in p.P_export_crop_with_c2_and_PV_pot) +
            sum(model.s_PV_on_export_crop_with_c2_and_PV_pot[t, k] for k in p.P_export_crop_with_c2_and_PV_pot) +
            sum(model.s_c1_on_export_crop_with_c1_and_c2_pot[t, k] for k in p.P_export_crop_with_c1_and_c2_pot) +
            sum(model.s_c2_on_export_crop_with_c1_and_c2_pot[t, k] for k in p.P_export_crop_with_c1_and_c2_pot) +
            sum(model.s_PV_on_export_crop_with_PV_and_c1_and_c2_pot[t, k]
                for k in p.P_export_crop_with_PV_and_c1_and_c2_pot) +
            sum(model.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot[t, k]
                for k in p.P_export_crop_with_PV_and_c1_and_c2_pot) +
            sum(model.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot[t, k]
                for k in p.P_export_crop_with_PV_and_c1_and_c2_pot))


def biomass_electricity_production(model, t):
    return model.p_biomass[t] == (
            sum(geo.yield_export_crop_on_c1_pot[k] * 0.0001 *
                (geo.S_export_crop_with_c1_pot[k][1] - model.s_c1_on_export_crop_with_c1_pot[t, k])
                for k in p.P_export_crop_with_c1_pot) +
            sum(geo.yield_export_crop_on_c1_and_PV_pot[k] * 0.0001 *
                (geo.S_export_crop_with_c1_and_PV_pot[k][1] - model.s_c1_on_export_crop_with_c1_and_PV_pot[t, k]
                 - model.s_PV_on_export_crop_with_c1_and_PV_pot[t, k]) for k in p.P_export_crop_with_c1_and_PV_pot) +
            sum(geo.yield_export_crop_on_c2_and_PV_pot[k] * 0.0001 *
                (geo.S_export_crop_with_c2_and_PV_pot[k][1] - model.s_c2_on_export_crop_with_c2_and_PV_pot[t, k]
                 - model.s_PV_on_export_crop_with_c2_and_PV_pot[t, k]) for k in p.P_export_crop_with_c2_and_PV_pot) +
            sum(geo.yield_export_crop_on_PV_and_c1_and_c2_pot[k] * 0.0001 *
                (geo.S_export_crop_with_PV_and_c1_and_c2_pot[k][1] -
                 model.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] -
                 model.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] -
                 model.s_PV_on_export_crop_with_PV_and_c1_and_c2_pot[t, k])
                for k in p.P_export_crop_with_PV_and_c1_and_c2_pot) +
            sum(geo.yield_export_crop_on_PV_pot[k] * 0.0001 *
                (geo.S_export_crop_with_PV_pot[k][1] - model.s_PV_on_export_crop_with_PV_pot[t, k])
                for k in p.P_export_crop_with_PV_pot) +
            sum(geo.yield_export_crop_on_c2_pot[k] * 0.0001 *
                (geo.S_export_crop_with_c2_pot[k][1] - model.s_c2_on_export_crop_with_c2_pot[t, k])
                for k in p.P_export_crop_with_c2_pot) +
            sum(geo.yield_export_crop_on_c1_and_c2_pot[k] * 0.0001 *
                (geo.S_export_crop_with_c1_and_c2_pot[k][1] - model.s_c1_on_export_crop_with_c1_and_c2_pot[t, k]
                 - model.s_c2_on_export_crop_with_c1_and_c2_pot[t, k]) for k in p.P_export_crop_with_c1_and_c2_pot) +
            sum(geo.yield_export_crop_no_pot[k] * 0.0001 * geo.S_export_crop_with_no_pot[k][1]
                for k in p.P_export_crop_with_no_pot) +
            sum(geo.yield_export_crop_on_u_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_pot[k][1] - model.s_u_on_export_crop_with_u_pot[t, k])
                for k in p.P_export_crop_with_u_pot) +
            sum(geo.yield_export_crop_on_u_and_PV_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_PV_pot[k][1] - model.s_u_on_export_crop_with_u_and_PV_pot[t, k] -
                 model.s_PV_on_export_crop_with_u_and_PV_pot[t, k]) for k in p.P_export_crop_with_u_and_PV_pot) +
            sum(geo.yield_export_crop_on_u_and_c1_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_c1_pot[k][1] - model.s_u_on_export_crop_with_u_and_c1_pot[t, k] -
                 model.s_c1_on_export_crop_with_u_and_c1_pot[t, k]) for k in p.P_export_crop_with_u_and_c1_pot) +
            sum(geo.yield_export_crop_on_u_and_c2_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_c2_pot[k][1] - model.s_u_on_export_crop_with_u_and_c2_pot[t, k] -
                 model.s_c2_on_export_crop_with_u_and_c2_pot[t, k]) for k in p.P_export_crop_with_u_and_c2_pot) +
            sum(geo.yield_export_crop_on_u_and_PV_and_c1_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_PV_and_c1_pot[k][1] -
                 model.s_u_on_export_crop_with_u_and_PV_and_c1_pot[t, k] -
                 model.s_PV_on_export_crop_with_u_and_PV_and_c1_pot[t, k] -
                 model.s_c1_on_export_crop_with_u_and_PV_and_c1_pot[t, k])
                for k in p.P_export_crop_with_u_and_PV_and_c1_pot) +
            sum(geo.yield_export_crop_on_u_and_c2_and_PV_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_c2_and_PV_pot[k][1] -
                 model.s_u_on_export_crop_with_u_and_c2_and_PV_pot[t, k] -
                 model.s_PV_on_export_crop_with_u_and_c2_and_PV_pot[t, k] -
                 model.s_c2_on_export_crop_with_u_and_c2_and_PV_pot[t, k])
                for k in p.P_export_crop_with_u_and_c2_and_PV_pot) +
            sum(geo.yield_export_crop_on_u_and_c2_and_c1_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_c2_and_c1_pot[k][1] -
                 model.s_u_on_export_crop_with_u_and_c2_and_c1_pot[t, k] -
                 model.s_c2_on_export_crop_with_u_and_c2_and_c1_pot[t, k] -
                 model.s_c1_on_export_crop_with_u_and_c2_and_c1_pot[t, k])
                for k in p.P_export_crop_with_u_and_c2_and_c1_pot) +
            sum(geo.yield_export_crop_on_u_and_c2_and_PV_and_c1_pot[k] * 0.0001 *
                (geo.S_export_crop_with_u_and_c2_and_PV_and_c1_pot[k][1] -
                 model.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] -
                 model.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] -
                 model.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] -
                 model.s_PV_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k])
                for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot)) * para.residue_rate \
           * para.ratio_biomass_to_electricity


def ground_mounted_PV_electricity_production(model, t):
    if t == 0:
        return model.p_ground_mounted_PV[t] == para.p_ground_mounted_PV_year_basis
    else:
        return model.p_ground_mounted_PV[t] == \
               sum(model.s_PV_on_c1_and_PV_pot[t, k] * geo.PV_output_on_c1_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_c1_and_PV_pot) + \
               sum(model.s_PV_on_export_crop_with_c1_and_PV_pot[t, k] *
                   geo.PV_output_on_export_crop_with_c1_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_c1_and_PV_pot) + \
               sum(model.s_PV_on_u_and_PV_pot[t, k] * geo.PV_output_on_u_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_u_and_PV_pot) + \
               sum(model.s_PV_on_export_crop_with_u_and_PV_pot[t, k] *
                   geo.PV_output_on_export_crop_with_u_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_u_and_PV_pot) + \
               sum(model.s_PV_on_u_and_PV_and_c1_pot[t, k] * geo.PV_output_on_u_and_PV_and_c1_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_u_and_PV_and_c1_pot) + \
               sum(model.s_PV_on_export_crop_with_u_and_PV_and_c1_pot[t, k] *
                   geo.PV_output_on_export_crop_with_u_and_PV_and_c1_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_u_and_PV_and_c1_pot) + \
               sum(model.s_PV_on_u_and_c2_and_PV_pot[t, k] * geo.PV_output_on_u_and_c2_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_u_and_c2_and_PV_pot) + \
               sum(model.s_PV_on_export_crop_with_u_and_c2_and_PV_pot[t, k] *
                   geo.PV_output_on_export_crop_with_u_and_c2_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_u_and_c2_and_PV_pot) + \
               sum(model.s_PV_on_u_and_c2_and_PV_and_c1_pot[t, k] * geo.PV_output_on_u_and_c2_and_PV_and_c1_pot[k]
                   * 0.175 * 0.000001 for k in p.P_with_u_and_c2_and_PV_and_c1_pot) + \
               sum(model.s_PV_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] *
                   geo.PV_output_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot) + \
               sum(model.s_PV_on_PV_and_c1_and_c2_pot[t, k] * geo.PV_output_on_PV_and_c1_and_c2_pot[k] * 0.175
                   * 0.000001 for k in p.P_with_PV_and_c1_and_c2_pot) + \
               sum(model.s_PV_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] *
                   geo.PV_output_on_export_crop_with_PV_and_c1_and_c2_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_PV_and_c1_and_c2_pot) + \
               sum(model.s_PV_on_PV_pot[t, k] * geo.PV_output_on_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_PV_pot) + \
               sum(model.s_PV_on_export_crop_with_PV_pot[t, k] * geo.PV_output_on_export_crop_with_PV_pot[k] * 0.175 *
                   0.000001 for k in p.P_export_crop_with_PV_pot) + \
               sum(model.s_PV_on_c2_and_PV_pot[t, k] * geo.PV_output_on_c2_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_with_c2_and_PV_pot) + para.p_ground_mounted_PV_year_basis + \
               sum(model.s_PV_on_export_crop_with_c2_and_PV_pot[t, k] *
                   geo.PV_output_on_export_crop_with_c2_and_PV_pot[k] * 0.175 * 0.000001
                   for k in p.P_export_crop_with_c2_and_PV_pot)


# This constraint ensures that electricity production projects from ground-mounted PV cannot be uninstalled at the
# island scale from one year to the next.
def ground_mounted_PV_electricity_production_increasing(model, t):
    if t == 0:
        return model.p_ground_mounted_PV[t] == para.p_ground_mounted_PV_year_basis
    else:
        return model.p_ground_mounted_PV[t] >= model.p_ground_mounted_PV[t - 1]


def solar_self_consumption(model, t):
    return model.p_solar_self_consumption[t] == sum(
        model.s_urban_for_solar_self_consumption[t, k] * geo.PV_output_on_urban_for_solar_self_consumption[k] *
        para.solar_panel_power_output * 0.000001 for k in p.P_urb_solar_self_consumption)


# This constraint ensures that we do not uninstall PV panels from the roofs at the island scale
# from one year to the next.
def solar_self_consumption_increasing(model, t):
    if t == 0:
        return model.p_solar_self_consumption[t] == 0
    else:
        return model.p_solar_self_consumption[t] >= model.p_solar_self_consumption[t - 1]


# Constraints definition related to the functions listed above
def define_constraints(model, T):
    model.electricity_production = pyo.Constraint(T, rule=electricity_production)
    model.balance_production_demand_upper_best = pyo.Constraint(T, rule=balance_production_demand_upper_best)
    model.balance_production_demand_lower_best = pyo.Constraint(T, rule=balance_production_demand_lower_best)
    model.balance_production_demand_upper_worst = pyo.Constraint(T, rule=balance_production_demand_upper_worst)
    model.balance_production_demand_lower_worst = pyo.Constraint(T, rule=balance_production_demand_lower_worst)
    model.biomass_surfaces = pyo.Constraint(T, rule=biomass_surfaces)
    model.biomass_electricity_production = pyo.Constraint(T, rule=biomass_electricity_production)
    model.ground_mounted_PV_electricity_production = pyo.Constraint(T, rule=ground_mounted_PV_electricity_production)
    model.ground_mounted_PV_electricity_production_increasing = \
        pyo.Constraint(T, rule=ground_mounted_PV_electricity_production_increasing)
    model.solar_self_consumption = pyo.Constraint(T, rule=solar_self_consumption)
    model.solar_self_consumption_increasing = pyo.Constraint(T, rule=solar_self_consumption_increasing)
