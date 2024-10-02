# Imports of useful packages
import pyomo.environ as pyo
from example import pre_processing as geo
from LUC_model import parcel_indices_lists as p


# The agricultural_area_increasing_constraint ensures that a cultivated parcel cannot be decultivated for the next
# time steps.
# The parcel_size_limit_constraint ensures that a surface allocated to electricity production, urban development or crop
# production inside a parcel does not exceed the total parcel size.


def agricultural_area_increasing_constraint(mdl, var, t, k):
    if t == 0:
        return var[t, k] == 0
    else:
        return var[t, k] >= var[t - 1, k]


def define_constraints_1(model, T):
    increasing_constraints = [
        (model.s_c2_on_export_crop_with_c2_pot, p.P_export_crop_with_c2_pot),
        (model.s_c2_on_c2_pot, p.P_with_c2_pot),
        (model.s_c2_on_export_crop_with_c2_and_PV_pot, p.P_export_crop_with_c2_and_PV_pot),
        (model.s_c2_on_c2_and_PV_pot, p.P_with_c2_and_PV_pot),
        (model.s_c2_on_export_crop_with_c1_and_c2_pot, p.P_export_crop_with_c1_and_c2_pot),
        (model.s_c2_on_c1_and_c2_pot, p.P_with_c1_and_c2_pot),
        (model.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot, p.P_export_crop_with_PV_and_c1_and_c2_pot),
        (model.s_c2_on_PV_and_c1_and_c2_pot, p.P_with_PV_and_c1_and_c2_pot),
        (model.s_c2_on_export_crop_with_u_and_c2_pot, p.P_export_crop_with_u_and_c2_pot),
        (model.s_c2_on_u_and_c2_pot, p.P_with_u_and_c2_pot),
        (model.s_c2_on_export_crop_with_u_and_c2_and_PV_pot, p.P_export_crop_with_u_and_c2_and_PV_pot),
        (model.s_c2_on_u_and_c2_and_PV_pot, p.P_with_u_and_c2_and_PV_pot),
        (model.s_c2_on_export_crop_with_u_and_c2_and_c1_pot, p.P_export_crop_with_u_and_c2_and_c1_pot),
        (model.s_c2_on_u_and_c2_and_c1_pot, p.P_with_u_and_c2_and_c1_pot),
        (model.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot),
        (model.s_c2_on_u_and_c2_and_PV_and_c1_pot, p.P_with_u_and_c2_and_PV_and_c1_pot),

        (model.s_c1_on_export_crop_with_c1_pot, p.P_export_crop_with_c1_pot),
        (model.s_c1_on_c1_pot, p.P_with_c1_pot),
        (model.s_c1_on_export_crop_with_c1_and_PV_pot, p.P_export_crop_with_c1_and_PV_pot),
        (model.s_c1_on_c1_and_PV_pot, p.P_with_c1_and_PV_pot),
        (model.s_c1_on_export_crop_with_c1_and_c2_pot, p.P_export_crop_with_c1_and_c2_pot),
        (model.s_c1_on_c1_and_c2_pot, p.P_with_c1_and_c2_pot),
        (model.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot, p.P_export_crop_with_PV_and_c1_and_c2_pot),
        (model.s_c1_on_PV_and_c1_and_c2_pot, p.P_with_PV_and_c1_and_c2_pot),
        (model.s_c1_on_export_crop_with_u_and_c1_pot, p.P_export_crop_with_u_and_c1_pot),
        (model.s_c1_on_u_and_c1_pot, p.P_with_u_and_c1_pot),
        (model.s_c1_on_export_crop_with_u_and_PV_and_c1_pot, p.P_export_crop_with_u_and_PV_and_c1_pot),
        (model.s_c1_on_u_and_PV_and_c1_pot, p.P_export_crop_with_u_and_PV_and_c1_pot),
        (model.s_c1_on_export_crop_with_u_and_c2_and_c1_pot, p.P_export_crop_with_u_and_c2_and_c1_pot),
        (model.s_c1_on_u_and_c2_and_c1_pot, p.P_with_u_and_c2_and_c1_pot),
        (model.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot, p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot),
        (model.s_c1_on_u_and_c2_and_PV_and_c1_pot, p.P_with_u_and_c2_and_PV_and_c1_pot)
    ]

    # Add constraints to the model
    for var, parc in increasing_constraints:
        model.add_component(
            f'increasing_constraint_{var.name}',
            pyo.Constraint(T, parc,
                           rule=lambda mdl, t, k, var=var: agricultural_area_increasing_constraint(mdl, var, t, k))
        )


def PV_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_PV_pot[t, k] <= geo.S_with_PV_pot[k][1]


def PV_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_export_crop_with_PV_pot[t, k] <= geo.S_export_crop_with_PV_pot[k][1]


def c1_area_limit_rule(mdl, t, k):
    return mdl.s_c1_on_c1_pot[t, k] <= geo.S_with_c1_pot[k][1]


def c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_c1_on_export_crop_with_c1_pot[t, k] <= geo.S_export_crop_with_c1_pot[k][1]


def c2_c3_area_limit_rule(mdl, t, k):
    return mdl.s_c2_on_c2_pot[t, k] + mdl.s_c3_on_c3_pot[t, k] <= geo.S_with_c2_pot[k][1]


def c2_c3_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_c2_on_export_crop_with_c2_pot[t, k] + mdl.s_c3_on_export_crop_with_c3_pot[t, k] <= \
           geo.S_export_crop_with_c2_pot[k][1]


def urban_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_pot[t, k] <= geo.S_with_u_pot[k][1]


def urban_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_pot[t, k] <= geo.S_export_crop_with_u_pot[k][1]


def PV_c1_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_c1_and_PV_pot[t, k] + mdl.s_c1_on_c1_and_PV_pot[t, k] <= geo.S_with_c1_and_PV_pot[k][1]


def PV_c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_export_crop_with_c1_and_PV_pot[t, k] + mdl.s_c1_on_export_crop_with_c1_and_PV_pot[t, k] <= \
           geo.S_export_crop_with_c1_and_PV_pot[k][1]


def PV_c2_c3_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_c2_and_PV_pot[t, k] + mdl.s_c2_on_c2_and_PV_pot[t, k] + mdl.s_c3_on_c3_and_PV_pot[t, k] <= \
           geo.S_with_c2_and_PV_pot[k][1]


def PV_c2_c3_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_export_crop_with_c2_and_PV_pot[t, k] + mdl.s_c2_on_export_crop_with_c2_and_PV_pot[t, k] <= \
           geo.S_export_crop_with_c2_and_PV_pot[k][1]


def c1_c2_area_limit_rule(mdl, t, k):
    return mdl.s_c2_on_c1_and_c2_pot[t, k] + mdl.s_c1_on_c1_and_c2_pot[t, k] <= geo.S_with_c1_and_c2_pot[k][1]


def c1_c2_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_c2_on_export_crop_with_c1_and_c2_pot[t, k] + mdl.s_c1_on_export_crop_with_c1_and_c2_pot[t, k] <= \
           geo.S_export_crop_with_c1_and_c2_pot[k][1]


def urban_PV_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_PV_pot[t, k] + mdl.s_PV_on_u_and_PV_pot[t, k] <= geo.S_with_u_and_PV_pot[k][1]


def urban_PV_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_PV_pot[t, k] + mdl.s_PV_on_export_crop_with_u_and_PV_pot[t, k] <= \
           geo.S_export_crop_with_u_and_PV_pot[k][1]


def urban_c1_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_c1_pot[t, k] + mdl.s_c1_on_u_and_c1_pot[t, k] <= geo.S_with_u_and_c1_pot[k][1]


def urban_c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_c1_pot[t, k] + mdl.s_c1_on_export_crop_with_u_and_c1_pot[t, k] <= \
           geo.S_export_crop_with_u_and_c1_pot[k][1]


def urban_c2_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_c2_pot[t, k] + mdl.s_c2_on_u_and_c2_pot[t, k] <= geo.S_with_u_and_c2_pot[k][1]


def urban_c2_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_c2_pot[t, k] + mdl.s_c2_on_export_crop_with_u_and_c2_pot[t, k] <= \
           geo.S_export_crop_with_u_and_c2_pot[k][1]


def urban_PV_c1_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_PV_and_c1_pot[t, k] + mdl.s_PV_on_u_and_PV_and_c1_pot[t, k] + \
           mdl.s_c1_on_u_and_PV_and_c1_pot[t, k] <= geo.S_with_u_and_PV_and_c1_pot[k][1]


def urban_PV_c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_PV_and_c1_pot[t, k] + \
           mdl.s_PV_on_export_crop_with_u_and_PV_and_c1_pot[t, k] + \
           mdl.s_c1_on_export_crop_with_u_and_PV_and_c1_pot[t, k] <= geo.S_export_crop_with_u_and_PV_and_c1_pot[k][1]


def PV_c1_c2_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_PV_and_c1_and_c2_pot[t, k] + mdl.s_c1_on_PV_and_c1_and_c2_pot[t, k] + \
           mdl.s_c2_on_PV_and_c1_and_c2_pot[t, k] <= geo.S_with_PV_and_c1_and_c2_pot[k][1]


def PV_c1_c2_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_PV_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] + \
           mdl.s_c1_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] + \
           mdl.s_c2_on_export_crop_with_PV_and_c1_and_c2_pot[t, k] <= geo.S_with_PV_and_c1_and_c2_pot[k][1]


def urban_c2_PV_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_c2_and_PV_pot[t, k] + mdl.s_PV_on_u_and_c2_and_PV_pot[t, k] + \
           mdl.s_c2_on_u_and_c2_and_PV_pot[t, k] <= geo.S_with_u_and_c2_and_PV_pot[k][1]


def urban_c2_PV_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_c2_and_PV_pot[t, k] + \
           mdl.s_PV_on_export_crop_with_u_and_c2_and_PV_pot[t, k] + \
           mdl.s_c2_on_export_crop_with_u_and_c2_and_PV_pot[t, k] <= geo.S_export_crop_with_u_and_c2_and_PV_pot[k][1]


def urban_c2_c1_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_c2_and_c1_pot[t, k] + mdl.s_c2_on_u_and_c2_and_c1_pot[t, k] + \
           mdl.s_c1_on_u_and_c2_and_c1_pot[t, k] <= geo.S_with_u_and_c2_and_c1_pot[k][1]


def urban_c2_c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_c2_and_c1_pot[t, k] + \
           mdl.s_c2_on_export_crop_with_u_and_c2_and_c1_pot[t, k] + \
           mdl.s_c1_on_export_crop_with_u_and_c2_and_c1_pot[t, k] <= geo.S_export_crop_with_u_and_c2_and_c1_pot[k][1]


def urban_PV_c2_c1_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_u_and_c2_and_PV_and_c1_pot[t, k] + mdl.s_c2_on_u_and_c2_and_PV_and_c1_pot[t, k] + \
           mdl.s_c1_on_u_and_c2_and_PV_and_c1_pot[t, k] + mdl.s_PV_on_u_and_c2_and_PV_and_c1_pot[t, k] <= \
           geo.S_with_u_and_c2_and_PV_and_c1_pot[k][1]


def urban_PV_c2_c1_export_crop_area_limit_rule(mdl, t, k):
    return mdl.s_u_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] + \
           mdl.s_c2_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] + \
           mdl.s_c1_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] + \
           mdl.s_PV_on_export_crop_with_u_and_c2_and_PV_and_c1_pot[t, k] <= \
           geo.S_export_crop_with_u_and_c2_and_PV_and_c1_pot[k][1]


def define_constraints_2(model, T):
    constraints = [
        ('PV_area_limit', p.P_with_PV_pot, PV_area_limit_rule),
        ('PV_export_crop_area_limit', p.P_export_crop_with_PV_pot, PV_export_crop_area_limit_rule),
        ('c1_area_limit', p.P_with_c1_pot, c1_area_limit_rule),
        ('c1_export_crop_area_limit', p.P_export_crop_with_c1_pot, c1_export_crop_area_limit_rule),
        ('c2_c3_area_limit', p.P_with_c2_pot, c2_c3_area_limit_rule),
        ('c2_c3_export_crop_area_limit', p.P_export_crop_with_c2_pot, c2_c3_export_crop_area_limit_rule),
        ('urban_area_limit', p.P_with_u_pot, urban_area_limit_rule),
        ('urban_export_crop_area_limit', p.P_export_crop_with_u_pot, urban_export_crop_area_limit_rule),
        ('PV_c1_area_limit', p.P_with_c1_and_PV_pot, PV_c1_area_limit_rule),
        ('PV_c1_export_crop_area_limit', p.P_export_crop_with_c1_and_PV_pot, PV_c1_export_crop_area_limit_rule),
        ('PV_c2_c3_area_limit', p.P_with_c2_and_PV_pot, PV_c2_c3_area_limit_rule),
        ('PV_c2_c3_export_crop_area_limit', p.P_export_crop_with_c2_and_PV_pot, PV_c2_c3_export_crop_area_limit_rule),
        ('c1_c2_area_limit', p.P_with_c1_and_c2_pot, c1_c2_area_limit_rule),
        ('c1_c2_export_crop_area_limit', p.P_export_crop_with_c1_and_c2_pot, c1_c2_export_crop_area_limit_rule),
        ('urban_PV_area_limit', p.P_with_u_and_PV_pot, urban_PV_area_limit_rule),
        ('urban_PV_export_crop_area_limit', p.P_export_crop_with_u_and_PV_pot, urban_PV_export_crop_area_limit_rule),
        ('urban_c1_area_limit', p.P_with_u_and_c1_pot, urban_c1_area_limit_rule),
        ('urban_c1_export_crop_area_limit', p.P_export_crop_with_u_and_c1_pot, urban_c1_export_crop_area_limit_rule),
        ('urban_c2_area_limit', p.P_with_u_and_c2_pot, urban_c2_area_limit_rule),
        ('urban_c2_export_crop_area_limit', p.P_export_crop_with_u_and_c2_pot, urban_c2_export_crop_area_limit_rule),
        ('urban_PV_c1_area_limit', p.P_with_u_and_PV_and_c1_pot, urban_PV_c1_area_limit_rule),
        ('urban_PV_c1_export_crop_area_limit', p.P_export_crop_with_u_and_PV_and_c1_pot,
         urban_PV_c1_export_crop_area_limit_rule),
        ('PV_c1_c2_area_limit', p.P_with_PV_and_c1_and_c2_pot, PV_c1_c2_area_limit_rule),
        ('PV_c1_c2_export_crop_area_limit', p.P_export_crop_with_PV_and_c1_and_c2_pot,
         PV_c1_c2_export_crop_area_limit_rule),
        ('urban_c2_PV_area_limit', p.P_with_u_and_c2_and_PV_pot, urban_c2_PV_area_limit_rule),
        ('urban_c2_PV_export_crop_area_limit', p.P_export_crop_with_u_and_c2_and_PV_pot,
         urban_c2_PV_export_crop_area_limit_rule),
        ('urban_c2_c1_area_limit', p.P_with_u_and_c2_and_c1_pot, urban_c2_c1_area_limit_rule),
        ('urban_c2_c1_export_crop_area_limit', p.P_export_crop_with_u_and_c2_and_c1_pot,
         urban_c2_c1_export_crop_area_limit_rule),
        ('urban_PV_c2_c1_area_limit', p.P_with_u_and_c2_and_PV_and_c1_pot, urban_PV_c2_c1_area_limit_rule),
        ('urban_PV_c2_c1_export_crop_area_limit', p.P_export_crop_with_u_and_c2_and_PV_and_c1_pot,
         urban_PV_c2_c1_export_crop_area_limit_rule),
    ]

    for name, index_set, rule in constraints:
        setattr(model, name, pyo.Constraint(T, index_set, rule=rule))
