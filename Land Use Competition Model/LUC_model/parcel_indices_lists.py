# Imports of useful Python files
from example import pre_processing as geo


# List of indices for each group of non-agricultural parcels with one or several potential land uses

P_with_PV_pot = [k for k in range(len(geo.S_with_PV_pot))]
P_with_c1_and_PV_pot = [k for k in range(len(geo.S_with_c1_and_PV_pot))]
P_with_c2_pot = [k for k in range(len(geo.S_with_c2_pot))]
P_with_c1_and_c2_pot = [k for k in range(len(geo.S_with_c1_and_c2_pot))]
P_with_c2_and_PV_pot = [k for k in range(len(geo.S_with_c2_and_PV_pot))]
P_with_c1_pot = [k for k in range(len(geo.S_with_c1_pot))]
P_with_PV_and_c1_and_c2_pot = [k for k in range(len(geo.S_with_PV_and_c1_and_c2_pot))]
P_with_u_pot = [k for k in range(len(geo.S_with_u_pot))]
P_with_u_and_PV_pot = [k for k in range(len(geo.S_with_u_and_PV_pot))]
P_with_u_and_c1_pot = [k for k in range(len(geo.S_with_u_and_c1_pot))]
P_with_u_and_c2_pot = [k for k in range(len(geo.S_with_u_and_c2_pot))]
P_with_u_and_PV_and_c1_pot = [k for k in range(len(geo.S_with_u_and_PV_and_c1_pot))]
P_with_u_and_c2_and_PV_pot = [k for k in range(len(geo.S_with_u_and_c2_and_PV_pot))]
P_with_u_and_c2_and_c1_pot = [k for k in range(len(geo.S_with_u_and_c2_and_c1_pot))]
P_with_u_and_c2_and_PV_and_c1_pot = [k for k in range(len(geo.S_with_u_and_c2_and_PV_and_c1_pot))]

# List of indices for each group of agricultural parcels with one or several potential land uses

P_export_crop_with_c1_pot = [k for k in range(len(geo.S_export_crop_with_c1_pot))]
P_export_crop_with_PV_pot = [k for k in range(len(geo.S_export_crop_with_PV_pot))]
P_export_crop_with_c2_pot = [k for k in range(len(geo.S_export_crop_with_c2_pot))]
P_export_crop_with_c1_and_PV_pot = [k for k in range(len(geo.S_export_crop_with_c1_and_PV_pot))]
P_export_crop_with_c1_and_c2_pot = [k for k in range(len(geo.S_export_crop_with_c1_and_c2_pot))]
P_export_crop_with_c2_and_PV_pot = [k for k in range(len(geo.S_export_crop_with_c2_and_PV_pot))]
P_export_crop_with_PV_and_c1_and_c2_pot = [k for k in range(len(geo.S_export_crop_with_PV_and_c1_and_c2_pot))]
P_export_crop_with_u_pot = [k for k in range(len(geo.S_export_crop_with_u_pot))]
P_export_crop_with_u_and_PV_pot = [k for k in range(len(geo.S_export_crop_with_u_and_PV_pot))]
P_export_crop_with_u_and_c1_pot = [k for k in range(len(geo.S_export_crop_with_u_and_c1_pot))]
P_export_crop_with_u_and_c2_pot = [k for k in range(len(geo.S_export_crop_with_u_and_c2_pot))]
P_export_crop_with_u_and_PV_and_c1_pot = [k for k in range(len(geo.S_export_crop_with_u_and_PV_and_c1_pot))]
P_export_crop_with_u_and_c2_and_PV_pot = [k for k in range(len(geo.S_export_crop_with_u_and_c2_and_PV_pot))]
P_export_crop_with_u_and_c2_and_c1_pot = [k for k in range(len(geo.S_export_crop_with_u_and_c2_and_c1_pot))]
P_export_crop_with_u_and_c2_and_PV_and_c1_pot = \
    [k for k in range(len(geo.S_export_crop_with_u_and_c2_and_PV_and_c1_pot))]
P_export_crop_with_no_pot = [k for k in range(len(geo.S_export_crop_with_no_pot))]

# List of indices of urban parcels designated for solar self-consumption

P_urb_solar_self_consumption = [k for k in range(len(geo.S_urban_solar_self_consumption))]
