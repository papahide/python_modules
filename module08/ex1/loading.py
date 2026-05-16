import sys


try:
    from importlib import metadata, util
    from matplotlib import pyplot
    import numpy as np
    import pandas as pd
except ModuleNotFoundError as err:
    print(f"ERROR: {err} not installed."
          f"\nTo install use: pip install "
          "-r ex1/requirements.txt")
    sys.exit(1)


def check_dependencie(dependencie: str) -> str:
    dep = util.find_spec(dependencie)
    if not dep:
        return "[KO]"
    return "[OK]"


def gen_matrix_data(number_data: int) -> np.ndarray:
    data = np.random.uniform(0, 100, number_data)
    return data


def pnd_analysis_gen(data: np.ndarray) -> None:
    file_name: str = "matrix_analysis.png"
    df = pd.DataFrame(data, columns=["value"])
    pyplot.hist(df)
    pyplot.title("Matrix")
    pyplot.savefig(file_name)
    pyplot.close()
    print("\nAnalysis complete!")
    print(f"Results saved to: {file_name}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    dependencies: dict[str, str] = {"pandas": "Data manipulation ready",
                                    "numpy": "Numerical computation ready",
                                    "requests": "Network access ready",
                                    "matplotlib": "Visualization ready"}
    print("\nChecking dependencies:")
    for key, value in dependencies.items():
        dep_check: str = check_dependencie(key)
        if dep_check == "[OK]":
            print(f"{dep_check} {key} ({metadata.version(key)}) - {value}")
        else:
            print(f"{dep_check} {key} - Not installed (optional).")
    print("\nAnalyzing Matrix data...")
    n_data = 1000
    print(f"Processing {n_data} data points...")
    m_data = gen_matrix_data(n_data)
    print("Generating visualization...")
    pnd_analysis_gen(m_data)


if __name__ == "__main__":
    main()
