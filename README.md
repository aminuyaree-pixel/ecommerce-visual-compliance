# E-Commerce Visual Intelligence

An academic AI demonstration application for product-image analysis, visual similarity exploration, preliminary description checks, analysis history, analytics, and PDF reporting.

> **Important:** This is a demonstration prototype. YOLO detections and CLIP similarity scores are not verified product identities, and the keyword-based policy checker does not determine official marketplace-policy compliance. All findings require human review.

## Features

- **Object detection:** YOLOv8 detects objects in uploaded images using the supplied pretrained model.
- **Visual similarity:** CLIP compares an image with a small, predefined set of product descriptions and ranks the candidates.
- **Description review:** A demonstration rule set flags selected phrases that may warrant further review.
- **Analysis history:** SQLite stores descriptions, image names, detection results, similarity matches, findings, and review status.
- **Analytics:** Streamlit displays analysis totals, review counts, status charts, and a timeline.
- **PDF reports:** ReportLab generates downloadable reports for current and historical analyses.
- **Image gallery:** Upload, search, and view product images.

## Technology stack

| Component | Technology |
|---|---|
| User interface | Streamlit |
| Object detection | Ultralytics YOLOv8 |
| Image/text similarity | OpenAI CLIP via Hugging Face Transformers |
| Model computation | PyTorch |
| Image processing | Pillow |
| Data and analytics | SQLite, pandas |
| PDF reports | ReportLab |

## Repository structure

```text
ecommerce-visual-compliance/
├── app.py
├── image_detection.py
├── visual_search.py
├── policy_checker.py
├── history.py
├── report_generator.py
├── requirements.txt
├── yolov8n.pt
├── bus.jpg
├── README.md
├── ARCHITECTURE.md
└── DEMO_GUIDE.md
```

## Requirements

- Windows, macOS, or Linux
- Python 3.12 is the tested Python version for this project
- Internet access on first run may be needed to download the CLIP model and its processor from Hugging Face
- Enough memory and disk space for PyTorch and the AI models

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aminuyaree-pixel/ecommerce-visual-compliance.git
cd ecommerce-visual-compliance
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local address in the terminal and open the application in a browser.

## How to use

1. Upload a JPG, JPEG, or PNG product image.
2. Enter a description of the product.
3. Select **Analyse Product**.
4. Review the YOLO detections.
5. Review the CLIP candidate descriptions and similarity scores.
6. Review any matched demonstration policy phrases.
7. Download the PDF report.
8. Explore analysis history, analytics, and the product gallery.

## How the AI components work

### YOLOv8

The supplied `yolov8n.pt` model performs general object detection. It is a pretrained general-purpose model, not a custom-trained e-commerce product classifier. Detection results depend on the objects and classes supported by the model.

### CLIP

The application compares the uploaded image against a short, predefined list of text descriptions. The displayed values are relative similarity scores across those candidates. They should not be interpreted as calibrated probabilities or proof of product identity.

### Demonstration policy checker

The policy checker searches the entered description for a small set of configured phrases. It is a rule-based demonstration, not a complete policy engine, legal assessment, or automated approval decision.

## Data and generated files

The application creates local working data, including an SQLite history database and uploaded images. YOLO may also create prediction output folders. These are runtime data and should not normally be committed to GitHub. Review the `.gitignore` file before committing.

Do not upload private, confidential, or personally identifying images or descriptions to a public repository.

## Testing status

The project owner previously reported successful manual checks of product analysis, history, analytics, PDF generation, and the image gallery in a fresh Python 3.12 environment. Re-run these checks after making code or dependency changes and before presenting or deploying the application.

## Known limitations

- The sidebar menu labels are currently informational; they do not navigate to separate application pages.
- CLIP uses a fixed, small candidate-description list.
- YOLO uses a general pretrained model rather than an e-commerce-specific custom model.
- The policy checker only detects configured phrases and can miss issues or flag wording that needs context.
- Local SQLite and image files are not a multi-user cloud storage solution.
- The application has not been represented as a production-ready or officially certified compliance system.

## Project documentation

- [System architecture](ARCHITECTURE.md)
- [Demonstration guide and final checklist](DEMO_GUIDE.md)

## Repository

[GitHub: aminuyaree-pixel/ecommerce-visual-compliance](https://github.com/aminuyaree-pixel/ecommerce-visual-compliance)

**Project:** E-Commerce Visual Intelligence  
**Project type:** Academic AI demonstration prototype
