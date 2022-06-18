import random
from typing import Dict, List

import torch
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""


def download_and_transform_data(
        data_dir: str
) -> datasets.OxfordIIITPet:
    """ Downloads and transforms the Oxford-IIIT Pet dataset.

    Args:
        data_dir:
            Directory in which to save the dataset.

    Returns:
        Pytorch's Oxford-IIIT Pet dataset.
    """

    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])

    target_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.PILToTensor(),
        # Transform classes (animal, animal_border, background) into (animal, background).
        # Binary classes are needed to use the pretrained model.
        lambda x: torch.div(x.type(torch.FloatTensor), 2, rounding_mode='trunc')
    ])

    pets_dataset = datasets.OxfordIIITPet(
        root=data_dir,
        target_types='segmentation',
        download=True,
        transform=transform,
        target_transform=target_transform,
    )

    return pets_dataset


def split_data(
        pets_dataset: datasets.OxfordIIITPet,
        val_ratio: float,
        test_ratio: float,
        seed: int
) -> Dict[str, datasets.OxfordIIITPet]:
    """Split the Oxford-IIIT Pet dataset into train, val and test sets.

    Args:
        pets_dataset:
            Pytorch's Oxford-IIIT Pet dataset.
        val_ratio:
            Fraction of dataset to use for validation.
        test_ratio:
            Fraction of dataset to use for testing.
        seed:
            Seed for random numbers generator.

    Returns:
        A dict containing train, validation and test datasets.
    """

    random.seed(seed)

    dataset_length = len(pets_dataset)
    val_size, test_size = int(val_ratio * dataset_length), int(test_ratio * dataset_length)
    train_size = dataset_length - (val_size + test_size)
    train_set, val_set, test_set = torch.utils.data.random_split(
        pets_dataset,
        [train_size,
         val_size,
         test_size]
    )
    pets_dataset_splits = {"train": train_set, "val": val_set, "test": test_set}
    return pets_dataset_splits


def prepare_dataloaders(
        pets_dataset_splits: Dict[str, datasets.OxfordIIITPet],
        batch_size: int,
        num_workers: int,
) -> List[DataLoader]:
    """Makes dataloaders from datasets.

    Args:
        pets_dataset_splits:
            A dict containing train, validation and test datasets.
        batch_size:
            Size of batches returned by dataloaders.
        num_workers:
            Number of workers to be used by dataloaders.

    Returns:
        A list containing train, validation and test dataloaders.
    """

    dataloaders = [DataLoader(
            pets_dataset_splits[dataset_type],
            batch_size=batch_size,
            num_workers=num_workers,
            # Only shuffle the train dataset
            shuffle=(dataset_type == 'train')
        )
        for dataset_type in ('train', 'val', 'test')
    ]
    return dataloaders
