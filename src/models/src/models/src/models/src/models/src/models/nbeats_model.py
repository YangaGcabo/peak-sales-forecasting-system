import torch
import pytorch_lightning as pl

class NBeats(pl.LightningModule):
    def __init__(self, input_size):
        super().__init__()
        self.fc = torch.nn.Linear(input_size, 1)

    def forward(self, x):
        return self.fc(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = torch.nn.functional.mse_loss(y_hat, y)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)
