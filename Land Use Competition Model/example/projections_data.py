# Import of package
import pandas as pd

# Projections for food demand are based on a constant consumption rate per household. In contrast, electricity demand
# projections account for both a constant consumption rate per household and the growing adoption of electric vehicles.

# Population projections
household_data = pd.read_excel("...")
household_projections_best = household_data['best case'].tolist()
household_projections_worst = household_data['worst case'].tolist()

# Electricity demand projections
electricity_demand_data = pd.read_excel("...")
electricity_demand_projections_best = electricity_demand_data['Best case_electrical_demand']
electricity_demand_projections_worst = electricity_demand_data['Worst case_electrical_demand']
