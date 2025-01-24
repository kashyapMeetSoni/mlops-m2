```python
 import os

 def run_dvc_update():
     """Updates DVC tracking after data modification."""

     # Add updated data to DVC tracking
     os.system("dvc add data.csv")

     # (Optional) Commit changes in DVC's own files
     os.system("dvc commit data.csv.dvc")

     print("DVC tracking updated.")

 if __name__ == "__main__":
     run_dvc_update()
 ```
