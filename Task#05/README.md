# EmpathyBot: DevelopersHub Summer AI/ML Internship Task 05

## Overview
This project, developed as part of the DevelopersHub Summer AI/ML Internship (Task 05), implements **EmpathyBot**, a conversational chatbot designed to provide empathetic responses to user inputs. The bot is fine-tuned on the EmpatheticDialogues dataset using the DistilGPT2 model from Hugging Face's Transformers library. The project includes scripts for training the model (`back.py`) and interacting with the bot (`main.py`), offering a lightweight and user-friendly solution for empathetic dialogue generation.

## Task Objective
The primary objective of Task 05 was to create a chatbot capable of generating empathetic and contextually relevant responses. The goals include:
- Fine-tuning a DistilGPT2 model on the EmpatheticDialogues dataset to enhance its ability to respond empathetically.
- Developing a user-friendly interface for real-time interaction with the bot.
- Ensuring the model generates coherent and non-repetitive responses using controlled generation parameters.

## Dataset Used
The **EmpatheticDialogues** dataset, available through the Hugging Face Datasets library, was used for fine-tuning. It contains multi-turn conversations labeled with emotions, designed to train models for empathetic dialogue. Key details:
- **Source**: Hugging Face (`load_dataset("empathetic_dialogues")`).
- **Structure**: Includes columns such as `utterance` (user or bot text), split into training, validation, and test sets.
- **Preprocessing**:
  - Utterances were tokenized using the DistilGPT2 tokenizer with a maximum length of 128 tokens.
  - Padding was applied using the end-of-sequence token to handle variable-length inputs.
  - Labels were set as copies of input IDs for causal language modeling.

## Models Applied
- **Model**: DistilGPT2 (a distilled version of GPT-2, optimized for efficiency).
- **Library**: Hugging Face Transformers (`AutoModelForCausalLM`, `AutoTokenizer`).
- **Training Configuration**:
  - Fine-tuned for 3 epochs with a batch size of 4 (training and evaluation).
  - Training arguments included logging every 10 steps, saving checkpoints every 500 steps, and limiting to 2 saved checkpoints.
  - The model was trained using the `Trainer` API from Transformers.
- **Generation Parameters** (for response generation):
  - Maximum length: 100 tokens.
  - Sampling with top-k (50), top-p (0.95), and temperature (0.8) for diverse yet coherent outputs.
  - No-repeat n-gram size of 2 to prevent repetitive phrases.
- **Hardware**: Training was performed on a local machine with PyTorch and GPU support (if available).

## Key Results and Findings
- **Functionality**: EmpathyBot successfully generates empathetic responses to user inputs, maintaining conversational flow and emotional sensitivity.
- **Performance**: The fine-tuned model, saved at checkpoint-500, produces coherent responses with controlled randomness, avoiding excessive repetition.
- **User Experience**: The `main.py` script provides a simple command-line interface for real-time interaction, with a clear exit mechanism ("quit").
- **Limitations**:
  - The DistilGPT2 model, while efficient, has limited capacity compared to larger models like GPT-3, potentially affecting response depth.
  - The EmpatheticDialogues dataset may not cover all emotional contexts, limiting generalization.
  - Training on a small batch size and for only 3 epochs may not fully optimize the model.
- **Future Improvements**:
  - Fine-tune a larger model (e.g., GPT-2 medium) for improved response quality.
  - Increase training epochs or use a larger batch size with gradient accumulation.
  - Incorporate user feedback to refine responses and expand the dataset.
  - Deploy the bot as a web application using Streamlit or Flask for broader accessibility.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Usmansarwar143/developershub-internship-tasks
   ```
2. Navigate to the project directory:
   ```bash
   cd Task#05
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure a compatible GPU is available for faster training (optional but recommended).

## Dependencies
- Python 3.8+
- transformers
- datasets
- torch
- numpy

Install dependencies using:
```bash
pip install transformers datasets torch numpy
```

## Usage
### Training the Model
1. Run the training script to fine-tune the DistilGPT2 model:
   ```bash
   python back.py
   ```
2. The script will:
   - Load and preprocess the EmpatheticDialogues dataset.
   - Train the model for 3 epochs, saving checkpoints in `./empathetic_model`.
   - Save the final model and tokenizer to `empathetic_model`.

### Interacting with EmpathyBot
1. Run the chat script to interact with the fine-tuned model:
   ```bash
   python main.py
   ```
2. Follow the prompts:
   - Enter your message to share feelings (e.g., "I'm feeling stressed today").
   - Type `quit` to exit.
3. The bot will respond empathetically, leveraging the fine-tuned model from `empathetic_model/checkpoint-500`.

## Project Structure
- `back.py`: Script for training and saving the fine-tuned DistilGPT2 model.
- `main.py`: Script for real-time interaction with EmpathyBot.
- `empathetic_model/`: Directory containing the fine-tuned model and tokenizer.
- `logs/`: Directory for training logs.
- `requirements.txt`: List of required Python packages.

## Contact
For questions, feedback, or contributions, please reach out to:
- **Developer**: Muhammad Usman
- **Email**: muhammadusman.becsef22@iba-suk.edu.pk
- **LinkedIn:** [Connect with me!](https://www.linkedin.com/in/muhammad-usman-018535253)
- **GitHub**: [See GitHub](https://github.com/Usmansarwar143)
- **Organization**: Developers Hub Corporation
- **Website**: [Visit Oranization](https://www.developershub.com)

## Credits
Developed by **Muhammad Usman**, a Machine Learning Intern at Developers Hub Corporation.
