# Image Manager

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Use](#how-to-use)

## Description

The Image Manager is a Python script designed to efficiently manage and organize image files in a specific directory. This script allows you to list images present in the folder and its subfolders and rename them based on the name of their parent folder.

## Features

- **List Images:** The script displays the list of image files present in the specified directory and its subdirectories. It also provides a summary of image counts for each folder.

- **Rename Images:** The script renames image files, taking into account the name of their parent folder. The new name is in the format "{parent_folder_name}_{image_file}".

## Getting Started

### Prerequisites

To run the Image Manager, ensure that you have the following installed on your system:

- Python (version X.X.X)

### Installation

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Install the required dependencies [if any] using the following command:

   ```bash
   pip install colorama
   ```

## How to Use

1. Set the folder_path variable at the beginning of the script to the path where you want to manage your images.
2. Run the script and enter one of the following commands:
3. list:all: To list all image files in the specified folder and its subfolders.
4. rename:all: To rename all image files in the specified folder and its subfolders.
5. The script will display the list of image files or rename them accordingly.
