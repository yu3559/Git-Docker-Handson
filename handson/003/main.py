import torch

if torch.cuda.is_available():
    print("✅ GPU is available!")
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
else:
    print("❌ GPU is not available.")
