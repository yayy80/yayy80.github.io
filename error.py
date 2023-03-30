import torch
import json

if torch.cuda.is_available():
    response = {"status": "success", "message": "NVIDIA GPU detected!"}
else:
    response = {"status": "error", "message": "No NVIDIA GPU detected."}

print(json.dumps(response))
