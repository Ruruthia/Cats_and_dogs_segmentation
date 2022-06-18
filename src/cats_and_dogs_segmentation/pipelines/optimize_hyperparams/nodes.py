"""
This is a boilerplate pipeline 'optimize_hyperparams'
generated using Kedro 0.18.1
"""
from typing import Dict, Any

import pytorch_lightning as pl
import wandb
from cats_and_dogs_segmentation.models.unet import UNetLit
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader


def optimize_hyperparams(
        train_data_loader: DataLoader,
        val_data_loader: DataLoader,
        default_config: Dict[str, Any],
        hyperparams_config: Dict[str, Any],
        num_epochs: int,
        gpus: int,
        project: str,
) -> None:
    def train():
        wandb.init(config=default_config)
        config = wandb.config
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

    sweep_config = {
        'method': 'random',
        'metric': {
            'name': 'val_acc',
            'goal': 'maximize'
        },
        "parameters": {

            "lr": {
                "values": hyperparams_config["lr"]
            },
            "eps": {
                "values": hyperparams_config["eps"]
            },
            "step_size": {
                "values": hyperparams_config["step_size"]
            },
            "gamma": {
                "values": hyperparams_config["gamma"]
            },
        }
    }
    sweep_id = wandb.sweep(sweep_config, project="pets_hyperparams")
    wandb.agent(sweep_id, train)
