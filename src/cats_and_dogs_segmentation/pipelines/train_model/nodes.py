"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.1
"""
from typing import Dict, Any

import pytorch_lightning as pl
from cats_and_dogs_segmentation.models.unet import UNetLit
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader


def train(
        train_data_loader: DataLoader,
        val_data_loader: DataLoader,
        config: Dict[str, Any],
        num_epochs: int,
        gpus: int,
        project: str,
) -> str:
    model = UNetLit(config)
    checkpoint_callback = pl.callbacks.ModelCheckpoint(
        monitor='val_acc',
        dirpath='data/06_models/',
        filename='model-{epoch:02d}-{val_acc:.2f}',
        save_top_k=1,
        mode='max',
    )

    trainer = pl.Trainer(logger=WandbLogger(save_dir=f"logs/", project=project),
                         gpus=gpus, max_epochs=num_epochs, callbacks=[checkpoint_callback])

    trainer.fit(model, train_data_loader, val_data_loader)

    return checkpoint_callback.best_model_path
