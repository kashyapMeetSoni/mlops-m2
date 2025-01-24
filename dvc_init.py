import os

def run_dvc_init():
    """Initializes DVC and adds data tracking."""

    # Initialize DVC
    os.system("dvc init --no-scm")  # --no-scm because we're using Git through GitHub

    # Add data to DVC tracking
    os.system("dvc add data.csv")

    # (Optional) Commit changes in DVC's own files
    os.system("dvc commit data.csv.dvc")

    print("DVC initialized and data added.")

if __name__ == "__main__":
    run_dvc_init()
