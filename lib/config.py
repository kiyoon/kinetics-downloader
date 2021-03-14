import os

DATASET_ROOT = "/disk/scratch2/s1884147/datasets/OnlyTimeCanTell/kinetics-400"
TRAIN_ROOT = os.path.join(DATASET_ROOT, "train")
VALID_ROOT = os.path.join(DATASET_ROOT, "valid")
TEST_ROOT = os.path.join(DATASET_ROOT, "test")

DATASET_ROOT2 = "/disk/scratch_fast1/s1884147/datasets/OnlyTimeCanTell/kinetics-400/frames"
TRAIN_FRAMES_ROOT = os.path.join(DATASET_ROOT2, "train")
VALID_FRAMES_ROOT = os.path.join(DATASET_ROOT2, "valid")
TEST_FRAMES_ROOT = os.path.join(DATASET_ROOT2, "test")

TRAIN_SOUND_ROOT = os.path.join(DATASET_ROOT, "train_sound")
VALID_SOUND_ROOT = os.path.join(DATASET_ROOT, "valid_sound")
TEST_SOUND_ROOT = os.path.join(DATASET_ROOT, "test_sound")

CATEGORIES_PATH = "resources/categories.json"
CLASSES_PATH = "resources/classes.json"
TRAIN_METADATA_PATH = "resources/kinetics400/train.json"
VAL_METADATA_PATH = "resources/kinetics400/validate.json"
TEST_METADATA_PATH = "resources/kinetics400/test.json"
