from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load model and tokenizer
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.float16, device_map="auto")

# Inference pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def generate_response(prompt, max_new_tokens=256):
    """Generate a response from the model given a prompt."""
    return pipe(prompt, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7)[0]['generated_text']

# LoRA/QLoRA fine-tuning setup (for advanced users)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

def setup_lora(model):
    lora_config = LoraConfig(
        r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"], lora_dropout=0.05, bias="none", task_type="CAUSAL_LM"
    )
    model = prepare_model_for_kbit_training(model)
    return get_peft_model(model, lora_config) 