import json

# Loading of the config file
with open(r'C:\Users\authier\PycharmProjects\pythonProject6\example\config.json') as f:
    config_data = json.load(f)

# Access to parameters
parameters = config_data["parameters"]

# Specifications of parameters
p_oil_year_basis = parameters["p_oil_year_basis"]
p_coal_year_basis = parameters["p_coal_year_basis"]
elec_consumption_year_basis = parameters["elec_consumption_year_basis"]
domestic_elec_consumption_year_basis = parameters["domestic_elec_consumption_year_basis"]
p_ground_mounted_PV_year_basis = parameters["p_ground_mounted_PV_year_basis"]
p_solar_self_consumption_year_basis = parameters["p_solar_self_consumption_year_basis"]
p_wind_year_basis = parameters["p_wind_year_basis"]
p_imported_biomass_year_basis = parameters["p_imported_biomass_year_basis"]
p_hydro_year_basis = parameters["p_hydro_year_basis"]
residue_rate = parameters["residue_rate"]
ratio_biomass_to_electricity = parameters["ratio_biomass_to_electricity"]
disconnection_threshold_intermittent_RE_low = parameters["disconnection_threshold_intermittent_RE_low"]
disconnection_threshold_intermittent_RE_high = parameters["disconnection_threshold_intermittent_RE_high"]
kcal_crop_c1 = parameters["kcal_crop_c1"]
kcal_crop_c2 = parameters["kcal_crop_c2"]
demand_crop_c1 = parameters["demand_crop_c1"]
demand_crop_c2 = parameters["demand_crop_c2"]
yield_crop_c1_best = parameters["yield_crop_c1_best"]
yield_crop_c1_worst = parameters["yield_crop_c1_worst"]
initial_production_crop_c1 = parameters["initial_production_crop_c1"]
initial_production_crop_c2 = parameters["initial_production_crop_c2"]
initial_surface_area_crop_c1 = parameters["initial_surface_area_crop_c1"]
initial_surface_area_crop_c2 = parameters["initial_surface_area_crop_c2"]
solar_panel_power_output = parameters["solar_panel_power_output"]
urban_extension_surfaces_non_residential_medium_planning = \
    parameters["urban_extension_surfaces_non_residential_medium_planning"]
urban_extension_area_per_household_medium_planning = parameters["urban_extension_area_per_household_medium_planning"]
