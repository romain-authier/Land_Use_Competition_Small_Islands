# Import of the optimization package pyomo
import pyomo.environ as pyo

# Definition of functions to maximize for the best case (lowest population projections) and the worst case
# (highest population projections) for Reunion Island.
# The goal of the optimization is to maximize the food Self-Sufficiency Ratio (SSR).


def objective_function_best_case_Reunion(mdl):
    return sum(mdl.ssr_best_Reunion[t] for t in T)


def objective_function_worst_case_Reunion(mdl):
    return sum(mdl.ssr_worst_Reunion[t] for t in T)


# Definition of maximization
def define_objective(model):
    model.objective_function_best_case_Reunion = pyo.Objective(rule=objective_function_best_case_Reunion,
                                                               sense=pyo.maximize)
    model.objective_function_worst_case_Reunion = pyo.Objective(rule=objective_function_worst_case_Reunion,
                                                                sense=pyo.maximize)


# Choosing a 12 years projection
T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
