# Import of Python functions
import geopandas as gpd

# In this file is described a pre-processing step in which we convert map of potential land uses into a set of
# parcel attributes such as id (id), surface area (area), producible PV (PVOUT), sugarcane yield (rdt_can) and
# vegetables yield (rdt_mar)

# Crop c1: Rice
# Crop c2: Vegetables
# Crop c3: Fruits
# The index u_pot refers to the potential for urban development
# Major crop for export: Sugarcane

# Read the map of potential land uses
gdf = gpd.read_file("...")


# Create masks to identify potential areas for urban development, production of crop c1,
# crop c2 and c3, and electricity production from ground_mounted PV.
mask_u = gdf['pot_urbain'] == 1
mask_c1 = gdf['pot_riz'] == 1
mask_PV = gdf['pot_solar'] == 1
mask_c2 = gdf['pot_maraic'] == 1

# Create masks to identify non-potential areas for urban development, production of crop c1,
# crop c2 and c3, electricity production from ground_mounted PV.
mask_not_u = gdf['pot_urbain'] != 1
mask_not_c1 = gdf['pot_riz'] != 1
mask_not_PV = gdf['pot_solar'] != 1
mask_not_c2 = gdf['pot_maraic'] != 1

# Create masks to identify agricultural areas associated to the major crop for export and other areas
mask_export_crop = gdf['libelle3'] == 'Canne a sucre'
mask_not_export_crop = gdf['libelle3'] != 'Canne a sucre'

# Create masks to identify urban areas for solar self-consumption given a maximum allowable size
mask_urban_area = (gdf['libelle1'] == 'Espace artificialise') & (gdf['geometry'].area <= 2)


# Filtering parcels in several groups according the potential land uses and the initial existing land use of the parcel
gdf_filtered_1 = gdf[mask_u & mask_export_crop & mask_not_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_2 = gdf[mask_u & mask_not_export_crop & mask_not_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_3 = gdf[mask_not_u & mask_export_crop & mask_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_4 = gdf[mask_not_u & mask_not_export_crop & mask_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_5 = gdf[mask_not_u & mask_export_crop & mask_not_c1 & mask_not_PV & mask_c2]
gdf_filtered_6 = gdf[mask_not_u & mask_not_export_crop & mask_not_c1 & mask_not_PV & mask_c2]
gdf_filtered_7 = gdf[mask_not_u & mask_export_crop & mask_PV & mask_not_c2 & mask_not_c1]
gdf_filtered_8 = gdf[mask_not_u & mask_not_export_crop & mask_PV & mask_not_c1 & mask_not_c2]
gdf_filtered_9 = gdf[mask_u & mask_export_crop & mask_not_c1 & mask_PV & mask_not_c2]
gdf_filtered_10 = gdf[mask_u & mask_not_export_crop & mask_not_c1 & mask_PV & mask_not_c2]
gdf_filtered_11 = gdf[mask_u & mask_export_crop & mask_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_12 = gdf[mask_u & mask_not_export_crop & mask_c1 & mask_not_PV & mask_not_c2]
gdf_filtered_13 = gdf[mask_u & mask_export_crop & mask_not_c1 & mask_not_PV & mask_c2]
gdf_filtered_14 = gdf[mask_u & mask_not_export_crop & mask_not_c1 & mask_not_PV & mask_c2]
gdf_filtered_15 = gdf[mask_not_u & mask_export_crop & mask_c1 & mask_PV & mask_not_c2]
gdf_filtered_16 = gdf[mask_not_u & mask_not_export_crop & mask_c1 & mask_PV & mask_not_c2]
gdf_filtered_17 = gdf[mask_not_u & mask_export_crop & mask_not_PV & mask_c2 & mask_c1]
gdf_filtered_18 = gdf[mask_not_u & mask_not_export_crop & mask_not_PV & mask_c2 & mask_c1]
gdf_filtered_19 = gdf[mask_not_u & mask_export_crop & mask_PV & mask_c2 & mask_not_c1]
gdf_filtered_20 = gdf[mask_not_u & mask_not_export_crop & mask_PV & mask_c2 & mask_not_c1]
gdf_filtered_21 = gdf[mask_u & mask_export_crop & mask_c1 & mask_not_PV & mask_c2]
gdf_filtered_22 = gdf[mask_u & mask_not_export_crop & mask_c1 & mask_not_PV & mask_c2]
gdf_filtered_23 = gdf[mask_u & mask_export_crop & mask_c1 & mask_PV & mask_not_c2]
gdf_filtered_24 = gdf[mask_u & mask_not_export_crop & mask_c1 & mask_PV & mask_not_c2]
gdf_filtered_25 = gdf[mask_u & mask_export_crop & mask_not_c1 & mask_PV & mask_c2]
gdf_filtered_26 = gdf[mask_u & mask_not_export_crop & mask_not_c1 & mask_PV & mask_c2]
gdf_filtered_27 = gdf[mask_not_u & mask_export_crop & mask_PV & mask_c2 & mask_c1]
gdf_filtered_28 = gdf[mask_not_u & mask_not_export_crop & mask_PV & mask_c2 & mask_c1]
gdf_filtered_29 = gdf[mask_u & mask_export_crop & mask_c1 & mask_PV & mask_c2]
gdf_filtered_30 = gdf[mask_u & mask_not_export_crop & mask_c1 & mask_PV & mask_c2]
gdf_filtered_31 = gdf[mask_not_u & mask_export_crop & mask_not_PV & mask_not_c2 & mask_not_c1]
gdf_filtered_32 = gdf[mask_export_crop]
gdf_filtered_33 = gdf[mask_urban_area]


# List of the surfaces of agricultural parcels (related to the major crop) and non-agricultural parcels with one
# or several potential land uses
S_export_crop_with_u_pot = list(zip(gdf_filtered_1['id'], gdf_filtered_1['geometry'].area))
S_with_u_pot = list(zip(gdf_filtered_2['id'], gdf_filtered_2['geometry'].area))
S_export_crop_with_c1_pot = list(zip(gdf_filtered_3['id'], gdf_filtered_3['geometry'].area))
S_with_c1_pot = list(zip(gdf_filtered_4['id'], gdf_filtered_4['geometry'].area))
S_export_crop_with_c2_pot = list(zip(gdf_filtered_5['id'], gdf_filtered_5['geometry'].area))
S_with_c2_pot = list(zip(gdf_filtered_6['id'], gdf_filtered_6['geometry'].area))
S_export_crop_with_PV_pot = list(zip(gdf_filtered_7['id'], gdf_filtered_7['geometry'].area))
S_with_PV_pot = list(zip(gdf_filtered_8['id'], gdf_filtered_8['geometry'].area))
S_export_crop_with_u_and_PV_pot = list(zip(gdf_filtered_9['id'], gdf_filtered_9['geometry'].area))
S_with_u_and_PV_pot = list(zip(gdf_filtered_10['id'], gdf_filtered_10['geometry'].area))
S_export_crop_with_u_and_c1_pot = list(zip(gdf_filtered_11['id'], gdf_filtered_11['geometry'].area))
S_with_u_and_c1_pot = list(zip(gdf_filtered_12['id'], gdf_filtered_12['geometry'].area))
S_export_crop_with_u_and_c2_pot = list(zip(gdf_filtered_13['id'], gdf_filtered_13['geometry'].area))
S_with_u_and_c2_pot = list(zip(gdf_filtered_14['id'], gdf_filtered_14['geometry'].area))
S_export_crop_with_c1_and_PV_pot = list(zip(gdf_filtered_15['id'], gdf_filtered_15['geometry'].area))
S_with_c1_and_PV_pot = list(zip(gdf_filtered_16['id'], gdf_filtered_16['geometry'].area))
S_export_crop_with_c1_and_c2_pot = list(zip(gdf_filtered_17['id'], gdf_filtered_17['geometry'].area))
S_with_c1_and_c2_pot = list(zip(gdf_filtered_18['id'], gdf_filtered_18['geometry'].area))
S_export_crop_with_c2_and_PV_pot = list(zip(gdf_filtered_19['id'], gdf_filtered_19['geometry'].area))
S_with_c2_and_PV_pot = list(zip(gdf_filtered_20['id'], gdf_filtered_20['geometry'].area))
S_export_crop_with_u_and_c2_and_c1_pot = list(zip(gdf_filtered_21['id'], gdf_filtered_21['geometry'].area))
S_with_u_and_c2_and_c1_pot = list(zip(gdf_filtered_22['id'], gdf_filtered_22['geometry'].area))
S_export_crop_with_u_and_PV_and_c1_pot = list(zip(gdf_filtered_23['id'], gdf_filtered_23['geometry'].area))
S_with_u_and_PV_and_c1_pot = list(zip(gdf_filtered_24['id'], gdf_filtered_24['geometry'].area))
S_export_crop_with_u_and_c2_and_PV_pot = list(zip(gdf_filtered_25['id'], gdf_filtered_25['geometry'].area))
S_with_u_and_c2_and_PV_pot = list(zip(gdf_filtered_26['id'], gdf_filtered_26['geometry'].area))
S_export_crop_with_PV_and_c1_and_c2_pot = list(zip(gdf_filtered_27['id'], gdf_filtered_27['geometry'].area))
S_with_PV_and_c1_and_c2_pot = list(zip(gdf_filtered_28['id'], gdf_filtered_28['geometry'].area))
S_export_crop_with_u_and_c2_and_PV_and_c1_pot = list(zip(gdf_filtered_29['id'], gdf_filtered_29['geometry'].area))
S_with_u_and_c2_and_PV_and_c1_pot = list(zip(gdf_filtered_30['id'], gdf_filtered_30['geometry'].area))
S_export_crop_with_no_pot = list(zip(gdf_filtered_31['id'], gdf_filtered_31['geometry'].area))
S_export_crop_initial = (sum(gdf_filtered_32['geometry'].area))
S_urban_solar_self_consumption = list(gdf_filtered_33['geometry'].area)

# List of the theoretical yields associated to crop c2 and to the major crop
yield_export_crop_on_u_pot = list(gdf_filtered_1['rdt_can'])
yield_export_crop_on_c1_pot = list(gdf_filtered_3['rdt_can'])
yield_export_crop_on_c2_pot = list(gdf_filtered_5['rdt_can'])
yield_c2_on_export_crop_with_c2_pot = list(gdf_filtered_5['rdt_mar'])
yield_c2_on_c2_pot = list(gdf_filtered_6['rdt_mar'])
yield_export_crop_on_PV_pot = list(gdf_filtered_7['rdt_can'])
yield_export_crop_on_u_and_PV_pot = list(gdf_filtered_9['rdt_can'])
yield_export_crop_on_u_and_c1_pot = list(gdf_filtered_11['rdt_can'])
yield_export_crop_on_u_and_c2_pot = list(gdf_filtered_13['rdt_can'])
yield_c2_on_export_crop_with_u_and_c2_pot = list(gdf_filtered_13['rdt_mar'])
yield_c2_on_u_and_c2_pot = list(gdf_filtered_14['rdt_mar'])
yield_export_crop_on_c1_and_PV_pot = list(gdf_filtered_15['rdt_can'])
yield_export_crop_on_c1_and_c2_pot = list(gdf_filtered_17['rdt_can'])
yield_c2_on_export_crop_with_c1_and_c2_pot = list(gdf_filtered_17['rdt_mar'])
yield_c2_on_c1_and_c2_pot = list(gdf_filtered_18['rdt_mar'])
yield_export_crop_on_c2_and_PV_pot = list(gdf_filtered_19['rdt_can'])
yield_c2_on_export_crop_with_c2_and_PV_pot = list(gdf_filtered_19['rdt_mar'])
yield_c2_on_c2_and_PV_pot = list(gdf_filtered_20['rdt_mar'])
yield_export_crop_on_u_and_c2_and_c1_pot = list(gdf_filtered_21['rdt_can'])
yield_c2_on_export_crop_with_u_and_c2_and_c1_pot = list(gdf_filtered_21['rdt_mar'])
yield_c2_on_u_and_c2_and_c1_pot = list(gdf_filtered_22['rdt_mar'])
yield_export_crop_on_u_and_PV_and_c1_pot = list(gdf_filtered_23['rdt_can'])
yield_export_crop_on_u_and_c2_and_PV_pot = list(gdf_filtered_25['rdt_can'])
yield_c2_on_export_crop_with_u_and_c2_and_PV_pot =list(gdf_filtered_25['rdt_mar'])
yield_c2_on_u_and_c2_and_PV_pot = list(gdf_filtered_26['rdt_mar'])
yield_export_crop_on_PV_and_c1_and_c2_pot = list(gdf_filtered_27['rdt_can'])
yield_c2_on_export_crop_with_PV_and_c1_and_c2_pot = list(gdf_filtered_27['rdt_mar'])
yield_c2_on_PV_and_c1_and_c2_pot = list(gdf_filtered_28['rdt_mar'])
yield_export_crop_on_u_and_c2_and_PV_and_c1_pot = list(gdf_filtered_29['rdt_can'])
yield_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = list(gdf_filtered_29['rdt_mar'])
yield_c2_on_u_and_c2_and_PV_and_c1_pot = list(gdf_filtered_30['rdt_mar'])
yield_export_crop_no_pot = list(gdf_filtered_31['rdt_can'])


# List of producible solar PV for parcels with a potential for ground-mounted solar PV production
PV_output_on_export_crop_with_PV_pot = list(gdf_filtered_7['PVOUT'])
PV_output_on_PV_pot = list(gdf_filtered_8['PVOUT'])
PV_output_on_export_crop_with_u_and_PV_pot = list(gdf_filtered_9['PVOUT'])
PV_output_on_u_and_PV_pot = list(gdf_filtered_10['PVOUT'])
PV_output_on_export_crop_with_c1_and_PV_pot = list(gdf_filtered_15['PVOUT'])
PV_output_on_c1_and_PV_pot = list(gdf_filtered_16['PVOUT'])
PV_output_on_export_crop_with_c2_and_PV_pot = list(gdf_filtered_19['PVOUT'])
PV_output_on_c2_and_PV_pot = list(gdf_filtered_20['PVOUT'])
PV_output_on_export_crop_with_u_and_PV_and_c1_pot = list(gdf_filtered_23['PVOUT'])
PV_output_on_u_and_PV_and_c1_pot = list(gdf_filtered_24['PVOUT'])
PV_output_on_export_crop_with_u_and_c2_and_PV_pot = list(gdf_filtered_25['PVOUT'])
PV_output_on_u_and_c2_and_PV_pot = list(gdf_filtered_26['PVOUT'])
PV_output_on_export_crop_with_PV_and_c1_and_c2_pot = list(gdf_filtered_27['PVOUT'])
PV_output_on_PV_and_c1_and_c2_pot = list(gdf_filtered_28['PVOUT'])
PV_output_on_export_crop_with_u_and_c2_and_PV_and_c1_pot = list(gdf_filtered_29['PVOUT'])
PV_output_on_u_and_c2_and_PV_and_c1_pot = list(gdf_filtered_30['PVOUT'])
PV_output_on_urban_for_solar_self_consumption = list(gdf_filtered_33['PVOUT'])



