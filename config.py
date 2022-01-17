args_wideresnet = {
    'epochs': 200,
    'optimizer_name': 'SGD',
    'optimizer_hyperparameters': {
        'lr': 0.1,
        'momentum': 0.9,
        'weight_decay': 1e-4
    },
    'scheduler_name': 'CosineAnnealingLR',
    'scheduler_hyperparameters': {
        'T_max': 200
    },
    'batch_size': 256,
}
args_preactresnet18 = {
    'epochs': 200,
    'optimizer_name': 'SGD',
    'optimizer_hyperparameters': {
        'lr': 0.01,
        'momentum': 0.9,
        'weight_decay': 1e-4
    },
    'scheduler_name': 'CosineAnnealingLR',
    'scheduler_hyperparameters': {
        'T_max': 200
    },
    'batch_size': 256,
}