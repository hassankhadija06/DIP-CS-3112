# Lab 05 - Convolution and Image Noise Filtering

This lab implements 2-D convolution from first principles and compares mean, Gaussian, and median filters on images containing Gaussian and salt-and-pepper noise.

## Topics

- 2-D convolution with reflect padding
- Kernel validation and odd kernel sizes
- Mean filtering
- Gaussian filtering
- Median filtering
- Gaussian noise
- Salt-and-pepper noise
- OpenCV comparison checks
- Kernel-size comparison at 3×3, 5×5, and 7×7
- PSNR and edge-detail observations
- Hand-calculation and spike-response exercises

## Files

| File | Purpose |
|---|---|
| `2024-SE-09-LAB05.ipynb` | Main notebook |

The notebook uses built-in sample images and generates its demonstration figures during execution.

## Run

```bash
python -m pip install numpy matplotlib opencv-python scikit-image scipy jupyter
jupyter notebook "2024-SE-09-LAB05.ipynb"
```

Run all cells using a Jupyter kernel and verify the final compliance checks and output figures.
