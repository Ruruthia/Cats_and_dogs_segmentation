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
        checkpoints_dir_path: str
) -> str:
    """ Trains a UNetLit model.

    Args:
        train_data_loader:
            Data loader for train dataset.
        val_data_loader:
            Data loader for validation dataset.
        config:
            A dict of model hyperparameters. It should contain following fields:
            lr - learning rate of Adam optimizer
            eps - term added to denominator to improve numerical stability in Adam optimizer
            step_size - period of learning rate decay in scheduler
            gamma - multiplicative factor of learning rate decay in scheduler
        num_epochs:
            Maximum number of epochs to train the model for.
        gpus:
            Number of gpus to use.
        project:
            Project name for wandb.
        checkpoints_dir_path:
            Path to directory for saving model checkpoints - either local or in the Cloud Storage.
    Returns:
        Path to the checkpoint of best model.

    """

    model = UNetLit(config)
    checkpoint_callback = pl.callbacks.ModelCheckpoint(
        monitor='val_acc',
        dirpath=checkpoints_dir_path,
        filename='model-{epoch:02d}-{val_acc:.2f}',
        save_top_k=1,
        mode='max',
    )

    trainer = pl.Trainer(logger=WandbLogger(save_dir="logs/", project=project),
                         gpus=gpus, max_epochs=num_epochs, callbacks=[checkpoint_callback])

    trainer.fit(model, train_data_loader, val_data_loader)

    return checkpoint_callback.best_model_path
