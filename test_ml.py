import pytest
import os
import pandas as pd 
from sklearn.model_selection import train_test_split
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_training_dataset_size():
    """
    # This test checks if the training dataset is the correct size. 
    """
    # Your code here
    project_path = "/workspace/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    train_size = len(train)

    expected_train_size = 26048
    assert train_size == expected_train_size
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_test_dataset_size():
    """
    # This test checks if the testing dataset is the correct size. 
    """
    # Your code here
    project_path = "/workspace/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    test_size = len(test)

    expected_test_size = 6513
    assert test_size == expected_test_size
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_training_dataset_type():
    """
    # This test checks if the data type of the training datatype matched the expected data type.
    """
    # Your code here
    project_path = "/workspace/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size=0.2, random_state=42)

    train_data_type = type(train)

    expected_data_type = pd.DataFrame
    assert train_data_type == expected_data_type
    pass
