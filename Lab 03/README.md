# Lab 03 - Image Enhancement and Intensity Transformations

This notebook implements and compares point transformations, histogram processing, and thresholding techniques for an 8-bit grayscale image.

## Topics

- Brightness adjustment
- Linear contrast and contrast centered at 128
- Image negative
- Gamma correction
- 256-bin grayscale histograms
- Global histogram equalization
- CLAHE
- Fixed thresholding
- Otsu thresholding
- Adaptive Gaussian thresholding
- Overflow-safe NumPy arithmetic

## Files

| File | Purpose |
|---|---|
| `2024-SE-09-Lab-03.ipynb` | Main notebook |
| `2024-SE-09-Lab-03.docx` | Submitted lab document |

## Run

```bash
python -m pip install numpy matplotlib opencv-python jupyter
jupyter notebook "2024-SE-09-Lab-03.ipynb"
```

Run all cells after confirming that the input image path in the notebook matches your environment.
