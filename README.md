# Digital Image Processing Lab

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Course](https://img.shields.io/badge/Course-CS--3112-blue)

Lab submissions for the **Digital Image Processing** course (CS-3112), Semester 5.

| | |
|:--|:--|
| **Name** | Syeda Khadija Hassan |
| **Roll No** | 2024-SE-09 |
| **Batch** | BS Software Engineering, 2024-28 |
| **University** | University of Azad Jammu & Kashmir, Muzaffarabad |

## Labs

| Lab | Topic | Status |
|:--:|:--|:--:|
| [Lab 01](Lab%2001) | Python fundamentals and NumPy/Pillow/Matplotlib setup | Done |
| [Lab 02](Lab%2002) | Image loading, color channels, cropping, resizing, histograms, and bit depth | Done |
| [Lab 03](Lab%2003) | Brightness, contrast, gamma correction, negatives, histogram equalization, and thresholding | Done |
| [Lab 04](Lab%2004) | Scaling, cropping, flipping, translation, rotation, interpolation, and input validation | Done |
| [Lab 05](Lab%2005) | 2-D convolution and mean, Gaussian, and median image-noise filtering | Done |

## Repository Structure

```text
DIP-CS-3112/
├── README.md
├── Lab 01/
├── Lab 02/
├── Lab 03/
├── Lab 04/
└── Lab 05/
```

Each lab folder contains its notebook or source files, supporting images or datasets where required, generated outputs, and a lab-specific README.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/hassankhadija06/DIP-CS-3112.git
   cd DIP-CS-3112
   ```
2. Create a virtual environment and install the main packages:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   python -m pip install notebook numpy matplotlib pillow opencv-python scikit-image scipy ipywidgets
   ```
3. Open the required lab notebook:
   ```bash
   jupyter notebook "Lab 05/2024-SE-09-LAB05.ipynb"
   ```

## Tools Used

- Python 3
- NumPy
- OpenCV
- Matplotlib
- Pillow
- scikit-image and SciPy for selected Lab 05 operations
- Jupyter Notebook

