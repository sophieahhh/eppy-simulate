# EnergyPlus Simulation Script

This script runs a single EnergyPlus simulation using eppy.

## Requirements

- EnergyPlus 23.1.0
- Python 3.8+
- eppy

Install eppy:

pip install eppy

## Configuration

Modify the following paths in the script:

iddfile = "path_to_EnergyPlus/Energy+.idd"  
epwfile = "path_to_weather_file/weather.epw"  
idf_path = "path_to_idf_file/model.idf"

## Usage

Run the script:

python your_script_name.py

## Output

Simulation results will be generated in the same directory as the IDF file.

## References

EnergyPlus  
https://energyplus.net/

eppy – Python interface for EnergyPlus  
https://eppy.readthedocs.io/