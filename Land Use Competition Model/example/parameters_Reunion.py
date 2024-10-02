import json

# Loading of the config file
with open(r'C:\Users\authier\PycharmProjects\pythonProject6\example\config.json') as f:
    config_data = json.load(f)

# Access to parameters
parameters = config_data["parameters"]

# Additional parameters to define for Reunion in relation to existing parameters
# Additional parameters according to the specificities of electricity production from various energy sources
wind_power_threshold = parameters["wind_power_threshold"]
hydro_production_low = parameters["hydro_production_low"]
hydro_production_high = parameters["hydro_production_high"]

# Additional parameters related to the addition of a crop to the generic model
kcal_crop_c3 = parameters["kcal_crop_c3"]
demand_crop_c3 = parameters["demand_crop_c3"]
initial_production_crop_c3 = parameters["initial_production_crop_c3"]
initial_surface_area_crop_c3 = parameters["initial_surface_area_crop_c3"]
crop_c1_surface_limit = parameters["crop_c1_surface_limit"]
yield_crop_c3 = parameters["yield_crop_c3"]

# Additional parameters according to the introduction of various dietary behaviors between traditional (trad) profile
# and mediterranean (med) profile
demand_crop_c1_trad = parameters["demand_crop_c1_trad"]
demand_crop_c1_med = parameters["demand_crop_c1_med"]
demand_crop_c2_trad = parameters["demand_crop_c2_trad"]
demand_crop_c2_med = parameters["demand_crop_c2_med"]
demand_crop_c3_trad = parameters["demand_crop_c3_trad"]
demand_crop_c3_med = parameters["demand_crop_c3_med"]

# Additional parameters according to the introduction of various urban development dynamics encompassing low and
# high rates of urban densification
urban_extension_area_per_household_low_planning = parameters["urban_extension_area_per_household_low_planning"]
urban_extension_area_per_household_high_planning = parameters["urban_extension_area_per_household_high_planning"]
urban_extension_surfaces_non_residential_low_planning = \
    parameters["urban_extension_surfaces_non_residential_low_planning"]
urban_extension_surfaces_non_residential_high_planning = \
    parameters["urban_extension_surfaces_non_residential_high_planning"]

