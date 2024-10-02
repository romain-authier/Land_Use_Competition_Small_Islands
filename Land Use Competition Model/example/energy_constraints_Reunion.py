# Import of the optimization package pyomo
import pyomo.environ as pyo

# Imports of useful Python files and functions
from LUC_model import parameters as para
from example import parameters_Reunion as para_reunion
import random


# Electricity generation from oil is decreasing during the planning horizon according to the energy planning in Reunion
# (reduced to 0 by the end of 2030). The future electricity production is assumed to be random.
def electricity_production_from_oil(model, t):
    if t == 0:
        return model.p_oil[t] == para.p_oil_year_basis
    if 1 <= t <= 6:
        return model.p_oil[t] == random.uniform(model.p_oil[t - 1], model.p_oil[t - 1] - 0.054 * t * model.p_oil[t - 1])
    if t >= 7:
        return model.p_oil[t] == 0


# Electricity generation from coal is decreasing to 0 after the first time step according to the energy planning in
# Reunion.
def electricity_production_from_coal(model, t):
    if t == 0:
        return model.p_coal[t] == para.p_coal_year_basis
    if t > 0:
        return model.p_coal[t] == 0


# We assume that electricity production from hydro follows a uniform distribution within a specific range.
def electricity_production_from_hydro(model, t):
    if t == 0:
        return model.p_hydro[t] == para.p_hydro_year_basis
    else:
        return model.p_hydro[t] == random.uniform(para_reunion.hydro_production_low,
                                                  para_reunion.hydro_production_high)


# Electricity production from wind is set to increase until a specific threshold until 2035 according to the energy
# planning in Reunion.
def electricity_production_from_wind(model, t):
    if t == 0:
        return model.p_wind[t] == para.p_wind_year_basis
    else:
        return model.p_wind[t] <= para_reunion.wind_power_threshold


# Constraints definition related to the function listed above
def define_constraints(model, T):
    model.electricity_production_from_hydro = pyo.Constraint(T, rule=electricity_production_from_hydro)
    model.electricity_production_from_wind = pyo.Constraint(T, rule=electricity_production_from_wind)
    model.electricity_production_from_coal = pyo.Constraint(T, rule=electricity_production_from_coal)
    model.electricity_production_from_oil = pyo.Constraint(T, rule=electricity_production_from_oil)
