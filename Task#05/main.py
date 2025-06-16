# chat_with_bot.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the fine-tuned model
model = AutoModelForCausalLM.from_pretrained("empathetic_model/checkpoint-500")
tokenizer = AutoTokenizer.from_pretrained("empathetic_model/checkpoint-500")

print("🤖 EmpathyBot is here. Type something to share your feelings. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("🤖 EmpathyBot: Take care of yourself. You’re doing great! 🌷")
        break

    # Format input with separator token
    input_text = f"User: {user_input}\nEmpathyBot:"
    inputs = tokenizer(
    input_text,
    return_tensors="pt",
    padding=True,
    truncation=True,
    return_attention_mask=True
    )
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Generate response
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=100,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

# Extract the bot's response after "EmpathyBot:"
    if "EmpathyBot:" in response:
        response = response.split("EmpathyBot:")[-1].strip()

    print(f"🤖 EmpathyBot: {response}\n")
