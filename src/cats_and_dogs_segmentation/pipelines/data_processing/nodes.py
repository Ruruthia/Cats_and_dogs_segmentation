import random
from typing import Dict, List

import torch
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""


def download_and_transform_data(path: str) \
        -> datasets.OxfordIIITPet:

    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])

    target_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.PILToTensor(),
        # Transform classes (animal, animal_border, background) into (animal, background).
        # Binary classes are needed to use the pretrained model.
        lambda x: x.type(torch.FloatTensor) // 2
    ])

    pets_dataset = datasets.OxfordIIITPet(
        root=path,
        target_types='segmentation',
        download=True,
        transform=transform,
        target_transform=target_transform)

    return pets_dataset


def split_data(
        pets_dataset: datasets.OxfordIIITPet,
        val_ratio: float,
        test_ratio: float,
        seed: int
) -> Dict[str, datasets.OxfordIIITPet]:

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
