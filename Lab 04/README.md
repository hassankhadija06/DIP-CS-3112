# Lab 04 - Geometric Image Transformations

This lab builds a validated and reusable image transformation workflow using OpenCV and NumPy.

## Topics

- Proportional and non-proportional scaling
- Cropping
- Horizontal, vertical, and combined flipping
- Positive and negative translation
- Center-based rotation
- Nearest-neighbor, bilinear, bicubic, and Lanczos interpolation
- Input validation and boundary checks
- Identity-transformation verification
- Interactive parameter controls

## Files

| File | Purpose |
|---|---|
| `2024-SE-09-LAB04.ipynb` | Main notebook |
| `input_image.jfif` | Input image |
| `Output-Images/` | Generated transformed images and comparison figures |

## Run

```bash
python -m pip install numpy matplotlib pillow opencv-python ipywidgets jupyter
jupyter notebook "2024-SE-09-LAB04.ipynb"
```

Run the notebook with widgets enabled. Generated transformations are saved under `Output-Images/`.
