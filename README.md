# E-Commerce Visual Intelligence

## 1. Project Overview

E-Commerce Visual Intelligence is an AI-powered application designed to support product image analysis, visual similarity search, and product policy compliance review.

The application combines computer vision and natural language processing techniques to help users examine product images and descriptions.

This project is developed as an academic AI demonstration prototype.

## 2. Project Objectives

- Detect objects in product images using YOLO.
- Identify visually similar products using CLIP.
- Examine product descriptions for potential policy concerns.
- Store product analysis results in an SQLite database.
- Provide an analytics dashboard for reviewing analysis activities.
- Generate downloadable PDF reports.

## 3. Key Features

- Product image upload and analysis.
- YOLO object detection.
- CLIP-based visual similarity search.
- Automated product policy checking.
- Product image gallery with filename search.
- Analysis history and detailed historical records.
- Analytics dashboard with charts.
- PDF compliance report generation.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| YOLO | Object detection |
| CLIP | Visual similarity search |
| SQLite | Analysis history storage |
| Pandas | Data processing |
| Pillow | Image processing |
| ReportLab | PDF report generation |

## 5. Project Structure

```text
ecommerce-visual-compliance/
│
├── app.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── image_detection.py
│   ├── visual_search.py
│   ├── policy_checker.py
│   ├── history.py
│   └── report_generator.py
│
├── images/
│
└── other project files
```

*Note: The structure above is illustrative. Update it if your actual folders or filenames differ.*

## 6. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd ecommerce-visual-compliance
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 7. How to Use the Application

1. Open the application.
2. Upload a product image.
3. Enter the product description.
4. Click **Analyse Product**.
5. Review YOLO object detection results.
6. Examine CLIP visual search results.
7. Review product policy findings.
8. Download the PDF report.
9. Explore analysis history and dashboard statistics.

## 8. Limitations

- AI detection and similarity results may not always be accurate.
- Policy findings are preliminary and require human review.
- The application is an academic demonstration prototype and is not a substitute for professional compliance assessment.

## 9. Future Improvements

- Improved product classification.
- Expanded visual product database.
- More comprehensive policy checking.
- Deployment to a cloud hosting platform.

## 10. Author

**E-Commerce Visual Intelligence Project**

Academic AI Demonstration Project.