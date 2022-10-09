
# Automated Process Simulation in Aspen Plus 

This repository introduces the usage of python scripts to automate Aspen Plus for process simulation. 

The automated process simulation would be helpful if we want to repeatedly change input variable values, run the simulations, and collect output variable values. For example, to **generate a database** (key performance indicators of chemical processes under different operating conditions) **for surrogate modeling**. Additionally, such a method can also be used for the **simulation-based optimization**, such as the stochastic search of the optimal operating condition for chemical processes.

**Input variables**
- [x] **stream variable**: flow rate, temperature, pressure, etc.
- [x] **block variable**: operating pressure, total number of trays, reflux ratio, etc.

**Output variables**
- [x] **stream variable**: mole fraction
- [x] **block variable**: reboiler/condenser heat duty
- [x] **simulation error**

With the above actions, in an automatic manner, **process simulation** and **data collection** can be performed under different operating conditions.

## Example
### Extractive Distillation Column (EDC)
Here, an illustrative example of EDC for the 1-butene/1,3-butadiene separation is introduced. N-methyl-2-pyrrolidone (NMP) is adopted as the solvent. The objective is to collect the key performance indicators (i.e., product purity and reboiler heat duty) of the EDC under varying operating conditions (i.e., number of trays, reflux ratio, and flow rate of solvent). Meanwhile, errors that occurred in the simulations are detected and recorded.

## Package
- [pywin32](https://pypi.org/project/pywin32/): provide access to APIs

## Software
- **Aspen Plus:** chemical process simulation

## Maintainer
Mr. Zihao Wang: zwang@mpi-magdeburg.mpg.de
