# Import of the optimization package pyomo
import pyomo.environ as pyo

# Import of useful python files
import variables
from LUC_model import objective_functions
from LUC_model import energy_constraints
from LUC_model import parcel_size_constraints
from LUC_model import urban_constraints
from LUC_model import food_constraints

# Building the model LUC
model = pyo.ConcreteModel(name="(LUC)")

# Choosing a 12 years projection
T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Activation of the decision variables, the objective functions and the constraints
variables.define_variables(model, T)
objective_functions.define_objective(model)
energy_constraints.define_constraints(model, T)
parcel_size_constraints.define_constraints_1(model, T)
parcel_size_constraints.define_constraints_2(model, T)
urban_constraints.define_constraints(model, T)
food_constraints.define_constraints(model, T)
