
# Automatic Process Simulation in Aspen Plus 

This repository introduces how to automate process simulation in Aspen Plus.

Automatic process simulation is highly efficient if we want to obtain the performance of a chemical process under a large number of different operating configurations. This generates datasets of operating configurations (i.e., inputs) and corresponding process performance (i.e., outputs) to support the surrogate modeling of the chemical process. Additionally, it allows for simulation-based optimization to search for  optimal operating conditions of chemical processes.

## Example
### Extractive Distillation Column (EDC)
Here, an illustrative example of EDC for the 1-butene/1,3-butadiene separation is introduced. N-methyl-2-pyrrolidone (NMP) is adopted as the solvent. The objective is to run the simulation and collect the key performance indicators (i.e., product purity and reboiler heat duty) of the EDC under different configurations (i.e., varying numbers of stages, reflux ratios, and flow rates of NMP). Meanwhile, errors that occurred in the simulation are detected and recorded.

**Inputs:**
- [x] stream variables (flow rate, temperature, pressure, etc.)
- [x] block variables (operating pressure, total number of trays, reflux ratio, etc.)

**Outputs:**
- [x] stream variables (mole fraction)
- [x] block variables (reboiler/condenser heat duty)
- [x] simulation error

## Requirements
### Library
- [pywin32](https://pypi.org/project/pywin32/): provide access to Windows APIs from Python

### Software
- Aspen Plus: chemical process simulation

## Author
Zihao Wang (zwang@mpi-magdeburg.mpg.de)

## Additional materials
More introductions to the Aspen Plus automation are referred to some online materials:

- [Mauro Suardi. (2022). Optimize process simulation with Python-Aspen integration.](https://medium.com/eni-digitalks/optimize-process-simulation-with-python-aspen-integration-e343bbab1aa0)
- [Samvith Rao. (2021). Automation of process simulation and data analytics with MATLAB.](https://www.aiche.org/academy/webinars/automation-process-simulation-and-data-analytics-matlab)
