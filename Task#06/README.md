# House Price Prediction: DevelopersHub Summer AI/ML Internship Task 06

## Overview
This project, developed as part of the DevelopersHub Summer AI/ML Internship (Task 06), focuses on building a machine learning model to predict house prices based on various features. The implementation uses a Gradient Boosting Regressor to predict house prices, leveraging a dataset containing housing-related attributes. The project includes data preprocessing, model training, evaluation, and visualization of results.

## Task Objective
The primary objective of this task is to develop a predictive model for house prices using a provided dataset. The goals include:
- Loading and preprocessing housing data to prepare it for machine learning.
- Training a Gradient Boosting Regressor model to predict house prices.
- Evaluating the model’s performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- Visualizing the relationship between actual and predicted house prices to assess model accuracy.

## Dataset Used
The dataset used for this project is sourced from `Housing.csv` (available in the project repository or downloaded from an external archive). It contains the following features:
- **price**: The target variable (house price).
- **area**: The area of the house in square feet.
- **bedrooms**: Number of bedrooms.
- **bathrooms**: Number of bathrooms.
- **stories**: Number of stories in the house.
- **mainroad**: Binary (yes/no) indicating if the house is on a main road.
- **guestroom**: Binary (yes/no) indicating the presence of a guest room.
- **basement**: Binary (yes/no) indicating the presence of a basement.
- **hotwaterheating**: Binary (yes/no) indicating the presence of hot water heating.
- **airconditioning**: Binary (yes/no) indicating the presence of air conditioning.
- **parking**: Number of parking spaces.
- **prefarea**: Binary (yes/no) indicating if the house is in a preferred area.
- **furnishingstatus**: Categorical variable indicating furnishing status (furnished, semi-furnished, unfurnished).

No missing values were found in the dataset, simplifying preprocessing. The dataset was preprocessed by encoding binary features (e.g., yes/no to 1/0) and one-hot encoding the categorical `furnishingstatus` feature.

## Models Applied
- **Model**: Gradient Boosting Regressor (from `sklearn.ensemble`)
- **Preprocessing**:
  - Binary features (`mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`) were mapped to 1 (yes) and 0 (no).
  - The `furnishingstatus` feature was one-hot encoded to create dummy variables.
  - Numeric features were scaled using `StandardScaler` to standardize the data.
- **Train-Test Split**: The dataset was split into 80% training and 20% testing sets with a random state of 42 for reproducibility.
- **Evaluation Metrics**:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

## Key Results and Findings
- **Model Performance**:
  - The Gradient Boosting Regressor achieved an MAE of approximately 960,714.33 and an RMSE of approximately 1,299,273.84 on the test set.
  - These metrics indicate the average prediction error and the spread of errors, respectively, suggesting moderate predictive accuracy but room for improvement.
- **Visualization**: A scatter plot of actual vs. predicted house prices was generated, with a red dashed line representing perfect predictions. The plot shows that while many predictions align closely with actual values, some outliers exist, indicating areas where the model struggles.
- **Limitations**:
  - The model’s performance could be improved by tuning hyperparameters (e.g., learning rate, number of estimators) or exploring other algorithms (e.g., Random Forest, XGBoost).
  - The dataset is relatively small, which may limit the model’s ability to generalize to diverse housing markets.
- **Future Improvements**:
  - Perform hyperparameter tuning using grid search or random search.
  - Explore feature engineering to create new features (e.g., area per bedroom).
  - Test additional regression models to compare performance.
  - Collect a larger dataset to improve model robustness.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd house-price-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the `Housing.csv` dataset is placed in the project directory or update the file path in the notebook.

## Dependencies
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage
1. Open the Jupyter Notebook `House_prediction_DevHub_Task06.ipynb`.
2. Ensure the `Housing.csv` dataset is accessible.
3. Run the notebook cells sequentially to:
   - Load and preprocess the data.
   - Train the Gradient Boosting Regressor.
   - Evaluate the model and visualize results.
4. Review the output metrics (MAE, RMSE) and the scatter plot of actual vs. predicted prices.

## Contact
For questions, feedback, or contributions, please reach out to:
- **Developer**: Muhammad Usman
- **LinkedIn**: [Connect With Developer!](https://www.linkedin.com/in/muhammad-usman-018535253)
- **Email**: muhammadusman.becsef22@iba-suk.edu.pk
- **GitHub**: [See GitHub](https://github.com/Usmansarwar143)
- **Organization**: Developers Hub Corporation
- **Website**: [Visit Organization](https://www.developershub.com)

## Credits
Developed by **Muhammad Usman**, a Machine Learning Intern at Developers Hub Corporation.
