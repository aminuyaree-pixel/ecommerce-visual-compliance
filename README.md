# E-Commerce Visual Intelligence

An AI-powered application for product image analysis, visual similarity search, and preliminary product policy compliance review.

## 1. Project Overview

E-Commerce Visual Intelligence combines computer vision and natural language processing to support the examination of product images and descriptions.

The application integrates YOLO object detection, CLIP visual similarity search, and automated policy checking in a Streamlit dashboard.

This project is an academic AI demonstration prototype.

## 2. Project Objectives

- Detect objects in product images using YOLO.
- Identify visually similar products using CLIP.
- Examine product descriptions for potential policy concerns.
- Store analysis results using SQLite.
- Display analysis statistics and historical records.
- Generate downloadable PDF reports.

## 3. Key Features

- Product image upload and analysis.
- YOLO object detection.
- CLIP-based visual similarity search.
- Automated product policy checking.
- Product image gallery.
- Analysis history and search.
- Analytics dashboard.
- Historical analysis details.
- PDF compliance reports.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| YOLOv8 | Object detection |
| CLIP | Visual similarity search |
| Transformers | CLIP model loading |
| PyTorch | AI model processing |
| SQLite | Database storage |
| Pandas | Data analysis |
| Pillow | Image processing |
| OpenCV | Computer vision |
| ReportLab | PDF generation |

## 5. Project Structure

```text
ecommerce-visual-compliance/
│
├── app.py
├── app_backup.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── image_detection.py
├── visual_search.py
├── policy_checker.py
├── history.py
├── report_generator.py
│
├── yolov8n.pt
└── bus.jpg
```

## 6. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/aminuyaree-pixel/ecommerce-visual-compliance.git
```

### Step 2: Enter the project directory

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

## 7. How to Use

1. Open the Streamlit application.
2. Upload a product image.
3. Enter the product description.
4. Click Analyse Product.
5. Review YOLO object detection results.
6. Examine CLIP visual similarity results.
7. Review potential policy concerns.
8. Download the PDF report.
9. Explore the analytics dashboard and analysis history.

## 8. Limitations

- AI detection results may not always be accurate.
- Visual similarity does not establish product identity.
- Policy findings are preliminary and require human review.
- The application is an academic demonstration prototype, not an official compliance certification system.

## 9. Future Improvements

- Improved product classification.
- Expanded product image database.
- Enhanced policy checking.
- Cloud deployment.
- Improved user interface and navigation.

## 10. Repository

GitHub: https://github.com/aminuyaree-pixel/ecommerce-visual-compliance

**Project:** E-Commerce Visual Intelligence  
**Type:** Academic AI Demonstration Project
