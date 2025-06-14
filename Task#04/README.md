# U-Care Buddy: A Streamlit Health Chatbot

## Overview
U-Care Buddy is a web-based chatbot application built using Streamlit, designed to provide general health-related information in a friendly and safe manner. The app leverages the Mistral AI model (Mixtral-8x7b-instruct) via the OpenRouter API to answer user queries while adhering to strict safety guidelines. The chatbot ensures that responses are general, evidence-based, and encourage users to consult healthcare professionals for personalized advice.

## Task Objective
The primary objective of U-Care Buddy is to create a user-friendly platform that delivers reliable, general health information in response to user queries. The app aims to:
- Provide clear, empathetic, and accurate responses based on widely accepted medical knowledge.
- Prioritize user safety by avoiding specific medical diagnoses, treatment plans, or harmful suggestions.
- Detect sensitive keywords related to medical emergencies and redirect users to seek professional help.
- Maintain a conversational history for a seamless user experience.
- Enhance the interface with engaging Lottie animations and a clean, modern design.

## Dataset Used
No specific dataset was used for training or fine-tuning the model, as U-Care Buddy relies on the pre-trained Mixtral-8x7b-instruct model accessed via the OpenRouter API. The system prompt and unsafe keyword list were manually curated to ensure safe and appropriate responses. The unsafe keyword list includes terms like "suicide," "heart attack," "diagnose," and others to flag potentially serious queries.

## Models Applied
- **Model**: Mistral AI Mixtral-8x7b-instruct
- **API**: OpenRouter API (`https://openrouter.ai/api/v1/chat/completions`)
- **Configuration**:
  - Temperature: 0.7 (to balance creativity and coherence in responses)
  - Max Tokens: 500 (to limit response length for clarity and relevance)
- **Frontend**: Streamlit for the web interface, with custom CSS for styling and Lottie animations for visual appeal.
- **Safety Mechanism**: A keyword-based filter to detect unsafe queries related to medical emergencies or inappropriate requests (e.g., diagnoses or prescriptions).

## Key Results and Findings
- **Functionality**: The chatbot successfully responds to general health queries with clear, friendly, and evidence-based information while consistently reminding users to consult healthcare professionals.
- **Safety Compliance**: The unsafe keyword detection effectively identifies sensitive queries, preventing the model from providing potentially harmful responses and redirecting users to seek professional help.
- **User Experience**: The Streamlit interface, enhanced with Lottie animations and a clean design, provides an engaging and intuitive experience. The conversation history feature allows users to track their interactions seamlessly.
- **Limitations**: The app relies on an external API, which may introduce latency or dependency on internet connectivity. The keyword-based safety filter may occasionally flag benign queries if they contain trigger words, requiring refinement for better precision.
- **Future Improvements**:
  - Implement a more sophisticated natural language processing approach for safety checks (e.g., context-aware filtering).
  - Add multi-language support to make the app accessible to a broader audience.
  - Integrate additional health-related resources or links to reputable medical websites.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/u-care-buddy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd u-care-buddy
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenRouter API key:
   - Replace `API_KEY` in the code with your valid OpenRouter API key.
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dependencies
- Python 3.8+
- Streamlit
- Requests
- Streamlit-Lottie

Install dependencies using:
```bash
pip install streamlit requests streamlit-lottie
```

## Usage
1. Launch the app using the command above.
2. Enter a general health-related question in the text input field (e.g., "What causes a sore throat?").
3. Submit the query to receive a response from U-Care Buddy.
4. View the conversation history displayed above the input field.
5. For sensitive queries (e.g., involving emergencies), the app will display a warning and advise seeking professional help.

## Safety Guidelines
- The chatbot avoids providing specific medical diagnoses, treatment plans, or medication advice.
- Queries containing unsafe keywords (e.g., "heart attack," "suicide") trigger a warning message directing users to consult a healthcare professional or emergency services.
- All responses include a reminder to seek personalized advice from a qualified medical professional.

## Contact
For questions, feedback, or contributions, please reach out to:
- **Developer**: Usman Sarwar
- **LinkedIn**:[Connect With Developer!](www.linkedin.com/in/muhammad-usman-018535253)
- **Email**: muhammadusman.becsef22@iba-suk.edu.pk
- **GitHub**: [See GitHub](https://github.com/Usmansarwar143)
- **Organization**: Developers Hub Corporation
- **Website**: [Visit Organization](https://www.developershub.com)

## Credits
Developed by **Usman Sarwar**, a Machine Learning Intern at Developers Hub Corporation.
