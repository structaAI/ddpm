import torch
import torch.nn as nn

def get_time_embedding(timesteps, embedding_dim):
  factor = 10000 ** (torch.arange(0, embedding_dim, 2).float() / embedding_dim)

class DownBlock(nn.Module):
   pass