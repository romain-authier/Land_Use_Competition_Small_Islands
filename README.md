# Constrained Optimization Model -- Land Use Competition (LUC)

## Overview

This repository contains a generic constrained optimization model designed to maximize a food Self-Sufficiency Ratio (SSR) under constraints related to electricity production, urban development, and food production.
We consider an annual time step.

The model utilizes the Pyomo library (Python Optimization Modeling Objects) to solve linear optimization problems. The optimization solver GLPK is used to address these linear constraints.

This model captures land-use competition between two food crops, ground-mounted photovoltaics (PV), and urban development in small island territories. It is particularly tailored for regions 
where a significant portion of agricultural land is dedicated to export crops. In such regions, we consider that these export-oriented agricultural lands may be converted to other uses, including food production, electricity production, or urban development.



The generic model can be found in the LUC_model directory, while the example directory contains a specific application 
of the model to Reunion Island.


### LUC_model Directory

`main.py`: The primary script that orchestrates the execution of the model, including decision variables, constraints, and objective functions.

`energy_constraints.py`: Defines constraints related to balancing electricity production with demand.

`food_constraints.py`: Establishes constraints to ensure that crop production does not exceed demand, and limits the maximum area that can be 
converted from potential to effective food production for each time step.

`urban_constraints.py`: describes the constraints related to urban development according to urban densification rates.

`parcel_size_constraints.py`: Defines size constraints on parcels allocated to electricity production, urban development, or food crop production.

`variables.py`: Contains the definition of all the variables used in the model.

`objective_functions.py`: Describes the objective functions to be maximized under different scenarios (e.g., best-case and worst-case scenarios).

`parcel_indices_lists.py`: Contains lists of indices for parcels with one or more potential land uses.

`parameters.py`: Initializes the model parameters using the values defined in the config.json file located in the example directory.

### Example directory

This folder contains a case study applied to Reunion Island, considering three major crops (rice, fruits, and vegetables). 
The land-use competition between these crops, ground-mounted PV, and urban development is modeled, with the assumption that fruits and vegetables are cultivated within the same areas. 

`scenarios_constraints.py`: Defines optional constraints that can be activated depending on the scenario being constructed, including dietary behaviors, energy production from various energy sources, and urban development dynamics.

`parameters_Reunion.py`: Contains parameters specific to Reunion Island.

`variables_Reunion.py`: Contains variables specific to Reunion Island.

`example_reunion.py`: The main script executing the model for this case study.

`pre-processing.py`: Extracts relevant parcel attributes from the shapefile and prepares them for model input.

`projections_data.py`: Includes projected data on electricity demand and household projections.

`objective_functions_Reunion.py`: Describes objective functions to maximize following a best case and worst case scenario in Reunion.

`energy_constraints_Reunion.py`: Defines energy production-related constraints specific to Reunion Island.

`food_constraints_Reunion.py`: Defines constraints related to crop production specific to Reunion Island.

`config.json`: Contains the parameter values used across both the LUC_model and example directories.

### Specifications of variables, parameters and scenarios

Specifications of some variables, parameters and scenarios are available in the docs file.
Data sources are also specified in this docs file.

## Input data 

The model requires a map of potential land uses at the island scale as input, where each parcel is assigned one or more potential land uses. 
These include:

- Potential for rice production
- Potential for fruit and vegetable production
- Potential for electricity production from ground-mounted PV.
- Potential for urban development.

This map of potential land uses is available using the following link https://www.dropbox.com/scl/fo/8kgc9rmjfmm3d3anjqpxa/AImo126HmB610UhFIHldGXs?rlkey=mt83l9m1smi1idt6qwrzyjfi0&st=o5aezm8h&dl=0. 

Projected data are available in in the input_data file.

## Usage instructions

1. Follow the instructions on activating/deactivating some constraints and objective functions 
within the Python files as needed to reflect the scenarios you wish to model.
2. Run the model by executing `example_Reunion.py`.

## Contributions

Contributions to the development and improvement of this model are welcome!
Please feel free to submit pull requests or open issues for discussion.

## Licence

This model is distributed under the [insert license type] license. For more details, please refer to the `LICENSE.md` file.
