# Solution for AI in Production Course (Coursera)

## Instructions

### A script is available to automate the ingestion (and re-train all models):
```
cd solution-guidance/
python model.py
```
it takes [Random Forest Regression](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) by default, however [Extra Trees Regression](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html) is also available as an option when adding the following argument:
```
python model.py extratrees
```

Course link: [learn/ibm-ai-workflow-ai-production](https://www.coursera.org/learn/ibm-ai-workflow-ai-production)

---
PART 1: Data Investigation

1. Assimilate the business scenario and articulate testable hypotheses.
1. State the ideal data to address the business opportunity and clarify the rationale for needing specific data.
1. Create a python script to extract relevant data from multiple data sources, automating the process of data ingestion.
1. Investigate the relationship between the relevant data, the target and the business metric.
1. Articulate your findings using a deliverable with visualizations.

PART 2: Model Iteration

1. State the different modeling approaches that you will compare to address the 1. business opportunity.
1. Iterate on your suite of possible models by modifying data transformations, 1. pipeline architectures, hyperparameters and other relevant factors.
1. Re-train your model on all of the data using the selected approach and prepare 1. it for deployment.
1. Articulate your findings in a summary report.

PART 3: Model Production

1. Build a draft version of an API with train, predict, and logfile endpoints.
1. Using Docker, bundle your API, model, and unit tests.
1. Using test-driven development, iterate on your API in a way that anticipates 1. scale, load, and drift.
1. Create a post-production analysis script that investigates the relationship 1. between model performance and the business metric.
1. Articulate your summarized findings in a final report.

---
The following questions are being evaluated as part of the peer review submission:

1. Are there unit tests for the API?
1. Are there unit tests for the model?
1. Are there unit tests for the logging?
1. Can all of the unit tests be run with a single script and do all of the unit 1. tests pass?
1. Is there a mechanism to monitor performance?
1. Was there an attempt to isolate the read/write unit tests from production 1. models and logs?
1. Does the API work as expected? For example, can you get predictions for a 1. specific country as well as for all countries combined?
1. Does the data ingestion exists as a function or script to facilitate 1. automation?
1. Were multiple models compared?
1. Did the EDA investigation use visualizations?
1. Is everything containerized within a working Docker image?
1. Did they use a visualization to compare their model to the baseline model?

---
These are data that are minimally required for performance monitoring:
1. runtime - The total amount of time required to process the request. This is a factor that directly affects the end user’s experience and should be monitored.
1. timestamp - Timestamps are needed to evaluate how well the system handles load and concurrency. Additionally, timestamps are useful when connecting predictions to labels that are acquired afterwards. Finally, they are needed for the investigation of events that might affect the relationship between the performance and business metrics.
1. prediction - The prediction is, of course, the primary output of a predition model. It is necessary to track the prediction for comparison to feedback to determine the quality of the predictions. Generally, predictions are returned as a list to accommodate multi-label classification.
1. input_data_summary - Summarizing information about the input data itself. For the predict endpoint this is the shape of the input feature matrix, but for the training endpoint the features and targets should be summarized.
1. model_version_number - The model version number is used to better understand the influence of model improvements (or bugs) on performance.