# ADHD Detection Using Machine Learning

## Overview

This project executes a machine learning pipeline to classify ADHD and non-ADHD subjects using a publicly available clinical dataset, which is the HYPERAKTIV dataset with the goal to explore whether behavioral and clinical features can be used to support ADHD pre-screening and determine an effective, interpretable model for ADHD classification through data-driven methods.
The project focuses on exploratory data analysis (EDA), feature correlation assessment, model training, hyperparameter tuning and performance evaluation using the confusion matrix.

## Problem Statement

Clinical diagnosis of ADHD requires extensive behavioral assessment and professional evaluation across multiple settings which is a time-consuming and resource-intensive process. So, this project explores whether machine learning models can assist as a screening tool by identifying patterns in clinical and physiological features to classify ADHD vs. Control subjects.

## Dataset

The dataset used in this project is a HYPERAKTIV dataset:

- Contains **103 patient records**
- Balanced ADHD and Control groups (Balanced classes help prevent bias during model evaluation)
- Includes demographic, behavioral and physiological features
- Cleaned and preprocessed before model training

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

- Statistical summary of features
- Class distribution visualization
- Correlation matrix analysis

### 2. Data Preprocessing

- Removal of unnecessary columns (IDs, date fields, high-variance noise)
- Handling of missing values
- Feature scaling
- Train-test split

### 3. Model Implementation

The following supervised learning models were implemented and compared:

- k-Nearest Neighbors (kNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Multilayer Perceptron (MLP)

## k-Nearest Neighbors (Primary Model)

kNN was selected as the primary model due to:

- Simplicity and transparency
- Interpretability
- No heavy training phase
- Good generalization on small datasets

### Choosing optimal k

The optimal number of neighbors was selected using the elbow method and validation:

- Original k: 13  
- Final k Selected: **11**

## Model Performance

### kNN Results (k = 11)

- Accuracy: **85.19%**
- 10-Fold Cross Validation: ~80–87%
- 20-Fold Cross Validation: ~80–88%
- LOOCV: ~77.61%

### Classification Metrics

- Precision: ~0.85–0.86
- Recall: ~0.85–0.86
- F1-Score: ~0.85

The model demonstrated strong precision and recall, which is important in medical screening to reduce false negatives.

## Model Comparison Summary

| Model | Performance Behavior |
|-------|----------------------|
| SVM | Performed strongly on smaller dataset (~94%) |
| Decision Tree | Underfit on small data, overfit on resampled data |
| Random Forest | Good performance but overfit on resampled dataset |
| kNN | Stable, interpretable, improved with more data |
| MLP | Best overall performer (up to ~98%) but less interpretable |

Although MLP achieved the highest accuracy, kNN was chosen due to simplicity, transparency and practical deployment considerations.

## Visualizations

The repository includes:

- Data distribution plots
- Correlation heatmap
- KNN hyperparameter tuning plot
- Confusion matrix

All visual outputs are available in the `visualizations/` directory.

## Limitations

- Dataset size (103 samples) is relatively small
- No external validation dataset
- Limited demographic diversity
- Some models risk overfitting on resampled data

## Future Improvements

- Larger and more diverse dataset
- External validation testing
- Hyperparameter tuning optimization

## Applications

- ADHD pre-screening tool
- Clinical decision support system
- Remote screening in rural or underserved areas
- Research tool for behavioral classification studies

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Conclusion

This project demonstrates that even simple machine learning models such as k-Nearest Neighbors can effectively classify ADHD using structured clinical data. While more complex models like MLP achieved higher accuracy, kNN offered a strong balance between interpretability and performance.
Machine learning can serve as a supportive screening tool alongside clinical evaluation, but not as a replacement for professional diagnosis.

## Author

Harshita Rai  
Machine Learning | Bioinformatics | Data Science

## License

This project is licensed under the MIT License.
