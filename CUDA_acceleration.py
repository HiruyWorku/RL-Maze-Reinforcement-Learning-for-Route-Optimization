import torch
import torch.nn as nn

# Define a small network
class TinyPolicyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )
    
    def forward(self, x):
        return self.net(x)

# Create a model and move it to CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

model = TinyPolicyNet().to(device)

# Sample input (e.g., grid coordinates like (0, 0) normalized)
sample_input = torch.tensor([[0.0, 0.0]], dtype=torch.float32).to(device)

# Forward pass
with torch.no_grad():
    output = model(sample_input)

print("Action scores:", output)
