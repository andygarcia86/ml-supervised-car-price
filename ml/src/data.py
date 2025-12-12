# ml/src/data.py
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


# Adjust these constants as needed for your project
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "used-cars-dataset.csv"   # put your CSV here
TARGET_COLUMN = "selling_price"                           # target column for selling price


def load_dataset(path: Path | None = None) -> pd.DataFrame:
    """
    Load the dataset from a CSV file.

    By default, it loads from data/raw/used-cars-dataset.csv.
    """
    csv_path = path or RAW_DATA_PATH
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {csv_path}. "
            f"Make sure the file exists or pass a valid path."
        )

    df = pd.read_csv(csv_path)
    return df


def split_dataset(
    df: pd.DataFrame,
    test_size: float = 0.3,
    random_state: int = 42,
    stratify: bool = True,
):
    """
    Split the dataset into train and test sets.

    Returns: X_train, X_test, y_train, y_test
    """
    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"TARGET_COLUMN '{TARGET_COLUMN}' not found in dataframe columns: "
            f"{list(df.columns)}"
        )

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    stratify_labels = y if stratify else None

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_labels,
    )

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    # Load the dataset
    print("Loading dataset...")
    df = load_dataset()
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")

    # Split the dataset
    print("\nSplitting dataset...")
    X_train, X_test, y_train, y_test = split_dataset(df, stratify=False)

    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")

    # Save split data
    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(exist_ok=True)

    X_train.to_csv(processed_dir / "X_train.csv", index=False)
    X_test.to_csv(processed_dir / "X_test.csv", index=False)
    y_train.to_csv(processed_dir / "y_train.csv", index=False)
    y_test.to_csv(processed_dir / "y_test.csv", index=False)

    print(f"\nSplit data saved to {processed_dir}")
