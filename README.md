# Pascal VOC Augmentor
This repository is heavily depending on [imgaug library](https://github.com/aleju/imgaug). This repository allows the user to augment images using Pascal VOC format and it will change the xml files accordingly.

## Installation
Clone this repository
```bash
git clone https://github.com/evanfebrianto/pascal_voc_augmentor.git
```

Move to the directory
```bash
cd pascal_voc_augmentor
```

Install the requirements to run the script
```bash
pip install -r requirements.txt
```

## Usage
Put all your image dataset inside the dataset/images folder and your xml files into the dataset/annotations folder

To run the augmentation script, please execute:
```bash
python scripts/augment_multiprocess.py
```

To visualize it, you can run:
```bash
python scripts/visualize_multiprocess.py
```

## Note
This script will utilize half of your cpu cores and consume your RAM. Please take note that the multiprocess script is still not stable yet. Sometimes, it will freeze due to deadlock process. I am still working to solve it. If that happens, please rerun the process until there is no file in your dataset/images folder.