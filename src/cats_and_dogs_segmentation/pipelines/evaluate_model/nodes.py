"""
This is a boilerplate pipeline 'evaluate_model'
generated using Kedro 0.18.1
"""

import Path
import pytorch_lightning as pl
from cats_and_dogs_segmentation.models.unet import UNetLit
from pytorch_lightning.loggers import WandbLogger


def evaluate(test_data_loader, model_path, gpus, project):
    model = UNetLit.load_from_checkpoint(checkpoint_path=model_path)

    trainer = pl.Trainer(gpus=gpus, logger=WandbLogger(save_dir=f"logs/", project=project,
                                                       name=f'{Path(model_path).stem}_evaluation'))

    trainer.test(model, test_data_loader)