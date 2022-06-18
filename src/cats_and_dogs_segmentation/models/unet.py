from typing import Dict, Any

import pytorch_lightning as pl
from pytorch_toolbelt.losses import BinaryFocalLoss
from ternausnet.models import UNet11
from torch.optim import Adam
from torch.optim import lr_scheduler


class UNetLit(pl.LightningModule):

    def __init__(self, config: Dict[str, Any]):
        super().__init__()

        self.lr = config["lr"]
        self.eps = config["eps"]
        self.step_size = config["step_size"]
        self.gamma = config["gamma"]

        self.model = UNet11(pretrained=True)
        self.loss_fn = BinaryFocalLoss()

    def forward(self, x):
        outputs = self.model(x)
        return outputs

    def configure_optimizers(self):
        optimizer = Adam(self.model.parameters(), lr=self.lr, eps=self.eps)
        scheduler = lr_scheduler.StepLR(optimizer, step_size=self.step_size, gamma=self.gamma)
        return [optimizer], [scheduler]

    def training_step(self, batch, batch_idx):
        x, y = batch
        outputs = self(x)
        loss = self.loss_fn(outputs, y)
        preds = (outputs > 0.5).float()
        self.log("train_loss", loss)
        self.log("train_acc", (preds == y).float().mean(), on_step=False, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        outputs = self(x)
        loss = self.loss_fn(outputs, y)
        preds = (outputs > 0.5).float()
        self.log("val_loss", loss)
        self.log("val_acc", (preds == y).float().mean(), on_step=False, on_epoch=True)
        return loss

    def test_step(self, batch, batch_idx):
        x, y = batch
        outputs = self(x)
        loss = self.loss_fn(outputs, y)
        preds = (outputs > 0.5).float()
        self.log("test_loss", loss)
        self.log("test_acc", (preds == y).float().mean(), on_step=False, on_epoch=True)
        return loss
