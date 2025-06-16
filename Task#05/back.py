# train_and_save.py

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
import torch

# Load EmpatheticDialogues dataset
dataset = load_dataset("empathetic_dialogues")

# Load tokenizer and model
# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

# Set pad_token as eos_token to avoid the padding error
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("distilgpt2")
model.resize_token_embeddings(len(tokenizer))


# Preprocess data
def preprocess(example):
    inputs = tokenizer(example["utterance"], truncation=True, padding="max_length", max_length=128)
    inputs["labels"] = inputs["input_ids"].copy()
    return inputs


# Apply preprocessing
tokenized = dataset.map(preprocess, remove_columns=dataset["train"].column_names)

# Training arguments
training_args = TrainingArguments(
    output_dir="./empathetic_model",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=10,
    save_steps=500,
    save_total_limit=2,
    do_train=True,
    do_eval=True,  # Optional; remove if not doing eval
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer,
)

# Train the model
trainer.train()

# Save final model and tokenizer
model.save_pretrained("empathetic_model")
tokenizer.save_pretrained("empathetic_model")

print("✨ Model and tokenizer saved to 'empathetic_model'")
