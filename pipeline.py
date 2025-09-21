import pandas as pd
from io import StringIO

# Simulated CSV input as a string (since file upload isn't possible)
csv_data = """name,age,score
Alice,25,80
Bob,,75
Charlie,30,
"""

# Step 1: Load Data
def load_data():
    print("Loading data...")
    return pd.read_csv(StringIO(csv_data))

# Step 2: Preprocess (fill missing values)
def preprocess_data(df):
    print("Filling missing values...")
    return df.fillna(df.mean(numeric_only=True))

# Step 3: Normalize data
def normalize_data(df):
    print("Normalizing data...")
    numeric = df.select_dtypes(include='number')
    df[numeric.columns] = (numeric - numeric.min()) / (numeric.max() - numeric.min())
    return df

# Step 4: Display Data (instead of saving to file)
def show_data(df):
    print("Final Processed Data:")
    print(df)

# Main function
def run_pipeline():
    df = load_data()
    df = preprocess_data(df)
    df = normalize_data(df)
    show_data(df)

# This block must be indented
if __name__ == "__main__":
    run_pipeline()
