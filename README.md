# AI/ML Internship Repository - DevelopersHub Corporation

## Overview

This repository contains the code, documentation, and final report for my AI/ML internship at DevelopersHub Corporation, completed in June 2025. The repository includes three project folders corresponding to the tasks I undertook during the internship: Task 4 (General Health Query Chatbot), Task 5 (Mental Health Support Chatbot), and Task 6 (House Price Prediction). Additionally, it includes a comprehensive internship report summarizing the objectives, methodologies, implementations, results, challenges, and learnings for each task.

The projects demonstrate my proficiency in natural language processing (NLP), model fine-tuning, regression modeling, and data visualization, showcasing practical applications of AI/ML techniques to real-world problems.

## Repository Structure

The repository is organized as follows:

- **`Task#04/`**: Contains the code and resources for the General Health Query Chatbot.
- **`Task#05/`**: Contains the code and resources for the Mental Health Support Chatbot.
- **`Task#06/`**: Contains the code and resources for the House Price Prediction model.
- **`Internship_Report_By_Muhammad_Usman.pdf`**: A detailed report documenting the internship projects, including objectives, methodologies, results, and future improvements.

## Task Descriptions

### Task#04: General Health Query Chatbot

- **Objective**: Develop a chatbot to answer general health queries with a friendly, safe, and informative tone, avoiding specific medical advice.
- **Key Features**:
  - Built using the Mistral-8x7B-Instruct model via the OpenRouter API.
  - Implemented safety filters for sensitive queries (e.g., "emergency," "suicide").
  - Deployed with a Streamlit web interface featuring conversational history and Lottie animations.
- **Folder Contents**:
  - `chat_app.py`: Main script for the chatbot implementation.
  - `requirements.txt`: Dependencies (e.g., Streamlit, Requests).
  - Other supporting files (e.g., Lottie animation JSON files, if applicable).
- **How to Run**:
  1. Install dependencies: `pip install -r Task#04/requirements.txt`.
  2. Obtain an OpenRouter API key and set it as an environment variable (`OPENROUTER_API_KEY`).
  3. Run the Streamlit app: `streamlit run Task#04/chat_app.py`.
  4. Access the app in your browser (typically at `http://localhost:8501`).

### Task#05: Mental Health Support Chatbot

- **Objective**: Create an empathetic chatbot to provide supportive responses for mental health concerns using a fine-tuned DistilGPT2 model.
- **Key Features**:
  - Fine-tuned DistilGPT2 on the EmpatheticDialogues dataset for empathetic responses.
  - Implemented via a command-line interface for user interaction.
  - Configured with generation parameters (e.g., `top_k=50`, `top_p=0.95`) for coherent outputs.
- **Folder Contents**:
  - `back.py`: Script for data preprocessing and model fine-tuning.
  - `main.py`: Script for loading the fine-tuned model and running the command-line interface.
  - `requirements.txt`: Dependencies (e.g., Transformers, PyTorch, Datasets).
  - `./empathetic_model/`: Directory for the fine-tuned model (not included due to size; instructions for retraining provided).
- **How to Run**:
  1. Install dependencies: `pip install -r Task#05/requirements.txt`.
  2. To retrain the model, run: `python Task#05/back.py` (requires access to the EmpatheticDialogues dataset).
  3. To use the chatbot, run: `python Task#05/main.py` and follow the prompts.
  4. Note: The fine-tuned model is not included; retrain using `back.py` or contact the author for the model files.

### Task#06: House Price Prediction

- **Objective**: Build a regression model to predict house prices based on features like area, bedrooms, and location.
- **Key Features**:
  - Utilized GradientBoostingRegressor for robust regression modeling.
  - Preprocessed the Kaggle House Price Prediction Dataset with one-hot encoding and StandardScaler.
  - Evaluated with Mean Absolute Error (MAE: 960,714.33) and Root Mean Squared Error (RMSE: 1,299,273.84).
  - Visualized results with a scatter plot of predicted vs. actual prices.
- **Folder Contents**:
  - `House_prediction_DevHub_Task06.ipynb`: Jupyter Notebook with data preprocessing, model training, evaluation, and visualization.
  - `Housing.csv`: Dataset file (if included; otherwise, downloadable from Kaggle).
  - `requirements.txt`: Dependencies (e.g., Pandas, Scikit-learn, Matplotlib, Seaborn).
- **How to Run**:
  1. Install dependencies: `pip install -r Task#06/requirements.txt`.
  2. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction) if not included.
  3. Open and run the Jupyter Notebook: `jupyter notebook Task#06/House_prediction_DevHub_Task06.ipynb`.

## Internship Report

- **File**: `Internship_Report_By_Muhammad_Usman.pdf`
- **Description**: A comprehensive report detailing the three tasks, including:
  - Objectives, methodologies, implementations, results, challenges, and learnings for each task.
  - Future improvements to enhance project functionality.
  - References to datasets, APIs, and libraries used.
- **How to Access**: Open the PDF file using any PDF viewer (e.g., Adobe Acrobat, browser-based viewers).
- **Note**: The report provides a complete narrative of the internship, complementing the code in the task folders.

## Prerequisites

To run the projects, ensure the following are installed:
- Python 3.8 or higher
- A code editor (e.g., VS Code) or Jupyter Notebook for Task#06
- Internet access for API calls (Task#04) or dataset downloads (Task#06)
- GPU (optional, for faster fine-tuning in Task#05)

Install dependencies for each task using the respective `requirements.txt` files:
```bash
pip install -r Task#0X/requirements.txt
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Usmansarwar143/developershub-internship-tasks
   ```
2. Navigate to the desired task folder (`Task#04`, `Task#05`, or `Task#06`) and follow the specific instructions in the "How to Run" section for each task.
3. For Task#04, set up an OpenRouter API key as an environment variable.
4. For Task#06, ensure the dataset (`Housing.csv`) is available or downloaded from Kaggle.
5. For Task#05, retrain the model if the fine-tuned model is not provided.

## Usage Notes

- **Task#04**: Requires an active internet connection and OpenRouter API key. Ensure API rate limits are respected during testing.
- **Task#05**: The fine-tuned DistilGPT2 model is not included due to size constraints. Retraining requires significant computational resources (e.g., GPU recommended).
- **Task#06**: The Jupyter Notebook is self-contained but requires the dataset file. Visualizations are best viewed in a Jupyter environment.
- **Report**: The PDF report is standalone and does not require additional setup.

## Future Improvements

- **Task#04**: Integrate a medical knowledge base and deploy on mobile platforms for broader accessibility.
- **Task#05**: Use larger models (e.g., GPT-Neo) and develop a web-based interface for improved user experience.
- **Task#06**: Implement feature selection and ensemble models to enhance prediction accuracy.

Refer to the `Internship_Report_By_Muhammad_Usman.pdf` for detailed suggestions.

## Contributing

This repository is a record of my internship work and is not open for contributions. However, feedback or questions are welcome via GitHub Issues or by contacting me at [your-email@example.com].


## Acknowledgments

- **DevelopersHub Corporation**: For providing the internship opportunity and project guidance.
- **Hugging Face**: For the Transformers library and EmpatheticDialogues dataset.
- **Kaggle**: For the House Price Prediction Dataset.
- **OpenRouter**: For access to the Mistral-8x7B-Instruct model.

## Contact

For inquiries, please reach out to:
- **Muhammad Usman Sarwar**
- **Email**: [muhammadusman.becsegf22@iba-suk.eu.pk]
- **GitHub**: [https://www.github.com/Usmansarwar143]

---

*Last Updated: June 16, 2025*
