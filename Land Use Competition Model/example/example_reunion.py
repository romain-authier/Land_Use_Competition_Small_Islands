# Import of the optimization package pyomo
import pyomo.environ as pyo

# Import of useful python files
from example import objective_functions_Reunion
from example import energy_constraints_Reunion
from LUC_model import parcel_size_constraints
from LUC_model import urban_constraints
from LUC_model import energy_constraints
from LUC_model import variables
from example import food_constraints_Reunion
from LUC_model import food_constraints
from example import variables_Reunion
import scenarios_constraints

# Choosing a 12 years projection from the year basis
T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Building the model RUN
model = pyo.ConcreteModel(name="(RUN)")

# Activation of variables and constraints in the main file
variables.define_variables(model, T)
variables_Reunion.define_variables(model, T)
food_constraints_Reunion.define_constraints(model, T)
energy_constraints.define_constraints(model, T)
energy_constraints_Reunion.define_constraints(model, T)
parcel_size_constraints.define_constraints_1(model, T)
parcel_size_constraints.define_constraints_2(model, T)
urban_constraints.define_constraints(model, T)
food_constraints.define_constraints(model, T)
scenarios_constraints.define_constraints(model, T)
objective_functions_Reunion.define_objective(model)


###########################################
# SCENARIO S1:
# Optimization of the food SSR for the following specifications:
# Urban component: Limited extent of urban development
# Energy component: Biomass imports and high penetration of intermittent RE in the electricity mix
# Food component: Average diet

# Run the model for the best case scenario
print('For the best case for S1')

model.objective_function_best_case_Reunion.activate()
model.objective_function_worst_case_Reunion.deactivate()
model.balance_production_demand_upper_worst.deactivate()
model.balance_production_demand_lower_worst.deactivate()
model.share_intermittent_RE_low.deactivate()
model.balance_production_demand_crop_c1_worst.deactivate()
model.balance_production_demand_crop_c2_worst.deactivate()
model.balance_production_demand_crop_c3_worst.deactivate()
model.no_biomass_imports.deactivate()
model.balance_production_demand_crop_c2_mediterranean_diet_best.deactivate()
model.balance_production_demand_crop_c2_mediterranean_diet_worst.deactivate()
model.balance_production_demand_crop_c1_mediterranean_diet_best.deactivate()
model.balance_production_demand_crop_c1_mediterranean_diet_worst.deactivate()
model.balance_production_demand_crop_c3_mediterranean_diet_best.deactivate()
model.balance_production_demand_crop_c3_mediterranean_diet_worst.deactivate()
model.urban_development_surfaces_high_planning_best_case.deactivate()
model.urban_development_surfaces_high_planning_worst_case.deactivate()
model.urban_development_surfaces_medium_planning_best_case.deactivate()
model.urban_development_surfaces_medium_planning_worst_case.deactivate()
model.urban_development_surfaces_low_planning_worst_case.deactivate()

solver = pyo.SolverFactory('glpk')
results1 = solver.solve(model)
pyo.assert_optimal_termination(results1)
print("end of the optimization")
