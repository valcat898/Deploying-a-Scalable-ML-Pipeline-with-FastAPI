# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model was developed by Catherine Valadez on 6/5/2024. RandomForestClassifier from sklearn.ensemble was used. 
The model uses hyperparameters, which are set before the training process begins. 

## Intended Use

The intended use for this model is to predict whether a person makes over or under $50k based on the data 
provided in the 'census.csv' dataset, such as workclass, education, marital-status, occupation, relationship, 
race, sex, and native-country.

## Training Data

The training data was provided by UC Irvine Machine Learning Repository: https://archive.ics.uci.edu/dataset/20/census+income
The dataset was extracted from the 1994 Census database by Barry Becker. The dataset was created to be used as a prediction
task to determine whether a person makes over $50k a year. 

## Evaluation Data

The dataset contains a total of 48,842 instances. The training set consists of 32,561 instances and the test set consists of 
16,281 instances, which means that 66.67% of the data was used for training and 33.33% of data was used for testing. 

## Metrics

The metrics for the model were as follows: 
    - Precision: 0.7361
    - Recall: 0.6302
    - Fbeta: 0.6790

## Ethical Considerations

One ethical consideration to be mindful of is fairness and bias. The model should not be used to discriminate against individuals based 
on race, age, ethnicity, or gender. The model should be evaluated for fairness and bias and take the necessary steps to mitigate any 
biases present. 

## Caveats and Recommendations
Since the dataset originated from a 1994 census database, the model should be used on a more recent database to accurately predict 
whether individuals make more than $50k in the present day.  