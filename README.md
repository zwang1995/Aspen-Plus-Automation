
# Python Automates Aspen Plus for Process Simulation

This repository introduces the use of python scripts to automate Aspen Plus for process simulation.

**Manipulate the INPUT:**
- [x] **stream variable**: modify the flow rate, temperature, etc.
- [x] **block variable**: modify the operating pressure, total number of stages, reflux ratio, etc.

**Monitor the OUTPUT:**
- [x] **stream variable**: mole fraction
- [x] **block variable**: reboiler/condenser heat duty
- [x] **simulation error**

With the above actions, in an automatic manner, **process simulation** and **data collection** can be performed under different operating conditions.

## Example
### Extractive Distillation for 1-Butene/1,3-Butadiene Separation using N-Methyl-2-pyrrolidone (NMP)
For simplicity, only the extractive column is considered here.

## Package
- [pywin32](https://pypi.org/project/pywin32/): access APIs with Python

## Software
- **Aspen Plus:** process simulation

## Maintainer
Mr. Zihao Wang: zwang@mpi-magdeburg.mpg.de
