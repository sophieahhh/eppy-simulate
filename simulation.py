import os
import time
from eppy.modeleditor import IDF
from eppy.runner.run_functions import runIDFs

iddfile = r"path_to_EnergyPlus\Energy+.idd"
epwfile = r"path_to_weather_file\weather.epw"
idf_path = r"path_to_idf_file\model.idf"


def make_eplaunch_options(idf):
    return {
        "ep_version": "23-1-0",
        "output_prefix": os.path.splitext(os.path.basename(idf.idfname))[0],
        "output_suffix": "C",
        "output_directory": os.path.dirname(idf.idfname),
        "readvars": False,
        "expandobjects": False,
    }


def main():
    if not os.path.isfile(iddfile):
        raise FileNotFoundError(f"IDD file not found: {iddfile}")
    if not os.path.isfile(epwfile):
        raise FileNotFoundError(f"Weather file not found: {epwfile}")
    if not os.path.isfile(idf_path):
        raise FileNotFoundError(f"IDF file not found: {idf_path}")

    IDF.setiddname(iddfile)

    start_time = time.time()
    idf = IDF(idf_path, epwfile)

    runs = [[idf, make_eplaunch_options(idf)]]
    runIDFs(runs, 1)

    elapsed = time.time() - start_time
    print(f"Done. Time: {elapsed:.2f} s")


if __name__ == "__main__":
    main()