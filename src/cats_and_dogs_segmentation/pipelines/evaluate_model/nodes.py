"""
This is a boilerplate pipeline 'evaluate_model'
generated using Kedro 0.18.1
"""

from pathlib import Path

import pytorch_lightning as pl
from cats_and_dogs_segmentation.models.unet import UNetLit
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader


def evaluate(
        test_data_loader: DataLoader,
        model_path: str,
        gpus: int,
        project: str,
) -> None:
    """Evaluates a model.

    Args:
        test_data_loader:
            Data loader for test dataset.
        model_path:
            A path to model checkpoint file.
        gpus:
            Number of gpus to use.
        project:
            Project name for wandb.
    """
    model = UNetLit.load_from_checkpoint(checkpoint_path=model_path)

    trainer = pl.Trainer(gpus=gpus, logger=WandbLogger(save_dir='gs://cads-bucket/wandb_logs', project=project,
                                                       name=f'{Path(model_path).stem}_evaluation'))

    trainer.test(model, test_data_loader)
