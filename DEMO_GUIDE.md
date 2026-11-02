# Demonstration Guide

## Suggested 5–7 minute walkthrough

### 1. Introduce the project
Explain that E-Commerce Visual Intelligence is an academic prototype combining computer vision, image-text similarity, simple rule-based description review, history, analytics, and PDF reporting.

### 2. Demonstrate product analysis
- Open the Streamlit application.
- Upload a suitable sample product image.
- Enter a clear, factual product description.
- Run the analysis.
- Explain the YOLO detections, CLIP candidate ranking, and any phrase-review findings.

### 3. Demonstrate reporting
- Download the PDF report.
- Open it and point out the description, model outputs, policy-review section, and disclaimer.

### 4. Demonstrate history and analytics
- Show the newly saved analysis in the history table.
- Open its detailed record.
- Show the summary metrics and charts.

### 5. Demonstrate the image gallery
- Upload one or more sample images.
- Search by filename.
- Open a selected image.

### 6. Explain limitations honestly
State that YOLO is a general pretrained detector, CLIP compares a fixed set of candidate descriptions, and the policy checker uses a small demonstration phrase list. The application supports preliminary review and does not certify products or make final compliance decisions.

## Final verification checklist

- [ ] Application starts with `streamlit run app.py`.
- [ ] Image upload accepts supported image formats.
- [ ] Missing image and missing description produce clear warnings.
- [ ] YOLO results display without crashing.
- [ ] CLIP candidate matches and scores display.
- [ ] Policy findings or the no-match message display.
- [ ] A new analysis appears in history.
- [ ] Historical details open correctly.
- [ ] Analytics metrics and charts display.
- [ ] PDF report downloads and opens.
- [ ] Gallery upload, filename search, and image viewing work.
- [ ] No secrets, virtual environments, private uploads, or generated runtime folders are committed.

## Presentation outline

1. Problem and motivation
2. Project aim and objectives
3. System architecture
4. Technologies used
5. Live product-analysis demonstration
6. Results and interpretation
7. Limitations and responsible use
8. Future improvements
