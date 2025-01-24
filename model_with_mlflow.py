import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import mlflow

def train_and_log_model(data_path, experiment_name, run_name, model_params=None):
    """Trains a linear regression model and logs metrics to MLflow."""

    # Set the experiment name (if it doesn't exist, it will be created)
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name=run_name):
        # Load data
        df = pd.read_csv(data_path)
        X = df[['feature1', 'feature2']]
        y = df['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train model
        if model_params is None:
            model_params = {}  # Use default parameters if none provided
        model = LinearRegression(**model_params)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Log parameters and metrics to MLflow
        mlflow.log_params(model_params)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        mlflow.sklearn.log_model(model, "model")  # Log the model itself

        print(f"Run '{run_name}' of experiment '{experiment_name}' completed with MSE: {mse:.2f}, R2: {r2:.2f}")

if __name__ == "__main__":
    # Example usage:
    train_and_log_model("data.csv", "m2-experiment", "run-1", {"fit_intercept": True})
    train_and_log_model("data.csv", "m2-experiment", "run-2", {"fit_intercept": False})
    train_and_log_model("data.csv", "m2-experiment", "run-3")  # Using default model parameters
