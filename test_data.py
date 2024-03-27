import os
import random
import shutil

# Define paths
main_data_dir = 'main'
samples_data_dir = 'samples'
test_data_dir = 'test'

# Create test data directories
test_dir_a = os.path.join(test_data_dir, 'a')
test_dir_b = os.path.join(test_data_dir, 'b')
os.makedirs(test_dir_a, exist_ok=True)
os.makedirs(test_dir_b, exist_ok=True)

# Function to select files for testing
def select_test_files(main_dir, samples_dir, test_dir):
    main_class_dirs = os.listdir(main_dir)
    for class_dir in main_class_dirs:
        main_class_path = os.path.join(main_dir, class_dir)
        samples_class_path = os.path.join(samples_dir, class_dir)
        test_class_path = os.path.join(test_dir, class_dir)
        os.makedirs(test_class_path, exist_ok=True)

        main_files = os.listdir(main_class_path)
        samples_files = os.listdir(samples_class_path)

        test_files = list(set(main_files) - set(samples_files))

        for file in test_files:
            src_path = os.path.join(main_class_path, file)
            dest_path = os.path.join(test_class_path, file)
            shutil.copy(src_path, dest_path)

# Select files for testing for classes a and b
select_test_files(os.path.join(main_data_dir, 'a'), os.path.join(samples_data_dir, 'a'), test_dir_a)
select_test_files(os.path.join(main_data_dir, 'b'), os.path.join(samples_data_dir, 'b'), test_dir_b)

print("Test data created successfully.")
