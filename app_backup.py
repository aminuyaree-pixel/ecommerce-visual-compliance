
import streamlit as st
import sys
import pandas as pd
from pathlib import Path

# Project configuration
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Import project modules
from image_detection import detect_product
from visual_search import search_product
from policy_checker import check_product_description
from history import (
    initialize_db,
    save_analysis,
    get_history,
    get_statistics,
    get_analysis_by_id
)
from report_generator import generate_pdf_report


# Page configuration
st.set_page_config(
    page_title="E-Commerce AI Copilot",
    page_icon="🛍️",
    layout="wide"
)

# Initialize database
initialize_db()



# Professional Dashboard Styling
st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #f4f7fc;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Dashboard title */
.dashboard-title {
    font-size: 34px;
    font-weight: 800;
    color: #14213d;
    letter-spacing: -1px;
}

/* Subtitle */
.subtitle {
    color: #64748b;
    font-size: 16px;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #14213d;
}

[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Sidebar divider */
[data-testid="stSidebar"] hr {
    border-color: #334155;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
}

/* Buttons */
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 9px 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
    border: none;
}

/* Section headings */
h1, h2, h3 {
    color: #14213d;
}

/* Data tables */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Input fields */
.stTextInput input,
.stTextArea textarea {
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)



# Professional Sidebar
with st.sidebar:

    st.markdown(
        "<h2 style='color:white;'>🛍️ AI COPILOT</h2>",
        unsafe_allow_html=True
    )

    st.caption("E-Commerce Intelligence Platform")

    st.divider()

    st.markdown("### 🧭 MAIN MENU")

    st.markdown("🏠  Product Analysis")
    st.markdown("🔎  Visual Search")
    st.markdown("🛡️  Policy Compliance")
    st.markdown("📊  Analytics Dashboard")
    st.markdown("📁  Analysis History")
    st.markdown("🖼️  Product Gallery")

    st.divider()

    st.markdown("### 🤖 AI TECHNOLOGY")
    st.caption("YOLO Object Detection")
    st.caption("CLIP Visual Search")
    st.caption("Automated Policy Checking")

    st.divider()

    st.caption("E-Commerce Visual Intelligence")
    st.caption("Version 1.0")

# Professional Main Dashboard Header
st.markdown("""
<div style="background: linear-gradient(135deg, #14213d, #2563eb); padding: 30px; border-radius: 15px; margin-bottom: 25px;">
<h1 style="color: white; font-size: 30px; font-weight: 800; margin-bottom: 10px;">
🛍️ E-Commerce Visual Intelligence
</h1>
<p style="color: #dbeafe; font-size: 16px; margin-bottom: 0;">
AI-powered product detection, visual search and policy compliance.
</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# Professional Dashboard Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🤖 AI Modules",
        value="3",
        help="YOLO Object Detection, CLIP Visual Search and Policy Compliance"
    )

with col2:
    st.metric(
        label="🔍 Analysis Mode",
        value="Image + Text"
    )

with col3:
    st.metric(
        label="🚀 Platform",
        value="AI Powered"
    )

st.divider()


# Product analysis section
st.subheader("📦 Product Analysis")

left, right = st.columns([1, 1])

with left:
    uploaded_image = st.file_uploader(
        "Upload product image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        st.image(
            uploaded_image,
            caption="Uploaded Product",
            use_container_width=True
        )

with right:
    description = st.text_area(
        "Product Description",
        height=180,
        placeholder="Example: Premium leather handbag with elegant design."
    )

    st.info(
        "Upload an image and provide a product description "
        "to begin AI analysis."
    )


analyse = st.button(
    "🚀 Analyse Product",
    type="primary",
    use_container_width=True
)


if analyse:

    if uploaded_image is None:
        st.warning("Please upload a product image.")

    elif not description.strip():
        st.warning("Please enter a product description.")

    else:

        image_path = (
            PROJECT_ROOT / "images" / "uploaded_product.jpg"
        )

        image_path.parent.mkdir(parents=True, exist_ok=True)

        with open(image_path, "wb") as file:
            file.write(uploaded_image.getbuffer())

        try:

            with st.spinner("AI is analysing your product..."):

                # YOLO detection
                detections = detect_product(str(image_path))

                # CLIP visual search
                matches = search_product(str(image_path))

                # Policy checking
                policy = check_product_description(description)

            st.success(
                "Product analysis completed successfully!"
            )

            # Save analysis to SQLite
            save_analysis(
                description=description,
                image_name=uploaded_image.name,
                detections=detections,
                matches=matches,
                findings=policy["findings"]
            )

            st.divider()

            # YOLO results
            st.subheader("1️⃣ YOLO Object Detection")

            if detections:
                st.dataframe(
                    detections,
                    use_container_width=True
                )
            else:
                st.info("No objects detected.")

            st.divider()

            # CLIP results
            st.subheader("2️⃣ CLIP Visual Search")

            if matches:
                for item in matches:
                    st.write(
                        f"**{item['description']}** — "
                        f"{item['score']:.2%}"
                    )
            else:
                st.info("No visual matches found.")

            st.divider()

            # Policy results
            st.subheader("3️⃣ Product Policy Compliance")

            if policy["findings"]:

                st.warning(
                    "Potential policy concerns identified."
                )

                for finding in policy["findings"]:

                    with st.expander(
                        f"⚠️ {finding['category']}"
                    ):

                        st.write(
                            "**Matched phrase:**",
                            finding["matched_phrase"]
                        )

                        st.write(
                            "**Recommendation:**",
                            finding["recommendation"]
                        )

            else:

                st.success(
                    "No matching demonstration rules found."
                )

            # Generate PDF report
            pdf_report = generate_pdf_report(
                description=description,
                detections=detections,
                matches=matches,
                findings=policy["findings"]
            )

            st.download_button(
                label="📄 Download PDF Compliance Report",
                data=pdf_report,
                file_name="product_compliance_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

            st.caption(
                "These are preliminary AI-assisted findings. "
                "Human review is required before making "
                "compliance decisions."
            )

        except Exception as error:

            st.error(
                f"Analysis failed: {error}"
            )


# Analytics Dashboard
st.divider()

st.header("📊 Analytics Dashboard")

stats = get_statistics()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Products Analysed",
    stats["total"]
)

col2.metric(
    "Review Required",
    stats["flagged"]
)

col3.metric(
    "No Demo Rule Matched",
    stats["not_flagged"]
)


# Retrieve saved history
history = get_history()


# Graphical analytics
st.subheader("📈 Compliance Analytics")

if history:

    df = pd.DataFrame(history)

    # Policy review status
    status_counts = df["status"].value_counts()

    st.write("### Policy Review Status")

    st.bar_chart(status_counts)

    # Product analysis timeline
    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    daily_counts = (
        df.groupby(df["created_at"].dt.date)
        .size()
    )

    st.write("### Products Analysed Over Time")

    st.line_chart(daily_counts)

else:

    st.info(
        "Complete a product analysis to generate charts."
    )


# Previous analysis history
st.subheader("📁 Previous Analysis History")

if history:

    df_history = pd.DataFrame(history)

    # Search products
    search_text = st.text_input(
        "🔎 Search analysed products",
        placeholder="Enter product description..."
    )

    # Filter by status
    statuses = ["All"] + sorted(
        df_history["status"].dropna().unique().tolist()
    )

    selected_status = st.selectbox(
        "Filter by compliance status",
        statuses
    )

    filtered_history = df_history.copy()

    if search_text:
        filtered_history = filtered_history[
            filtered_history["description"].str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    if selected_status != "All":
        filtered_history = filtered_history[
            filtered_history["status"] == selected_status
        ]

    st.write(
        f"Showing {len(filtered_history)} of {len(df_history)} records"
    )

    st.dataframe(
        filtered_history[
            ["created_at", "description", "image_name", "status"]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No previous analyses recorded yet.")


# Detailed Historical Analysis
st.divider()

st.subheader("🔍 View Detailed Historical Analysis")

history = get_history()

if history:

    analysis_options = {
        f"ID {item['id']} - {item['description'][:50]}": item["id"]
        for item in history
    }

    selected_analysis = st.selectbox(
        "Select a previous product analysis",
        options=list(analysis_options.keys())
    )

    analysis_id = analysis_options[selected_analysis]

    analysis = get_analysis_by_id(analysis_id)

    if analysis:

        st.write("### 📦 Product Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Analysis ID", analysis["id"])
        col2.metric("Compliance Status", analysis["status"])
        col3.write(analysis["created_at"])

        st.write("**Product Description:**", analysis["description"])
        st.write("**Image Name:**", analysis["image_name"])
        st.download_button(
    label="📄 Download Historical PDF Report",
    data=generate_pdf_report(
        description=analysis["description"],
        detections=analysis["detections"],
        matches=analysis["matches"],
        findings=analysis["findings"]
    ),
    file_name=f"historical_report_{analysis['id']}.pdf",
    mime="application/pdf"
)
        st.divider()

        # YOLO Detection Results
        st.write("### 🎯 YOLO Object Detection")

        if analysis["detections"]:
            st.dataframe(
                pd.DataFrame(analysis["detections"]),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No objects detected.")

        st.divider()

        # CLIP Visual Search Results
        st.write("### 🔎 CLIP Visual Search")

        if analysis["matches"]:

            for item in analysis["matches"]:

                col1, col2 = st.columns([3, 1])

                with col1:
                    st.write(item["description"])

                with col2:
                    st.metric(
                        "Similarity",
                        f"{item['score']:.2%}"
                    )

        else:
            st.info("No visual matches found.")

        st.divider()

        # Policy Compliance Findings
        st.write("### 🛡️ Policy Compliance")

        if analysis["findings"]:

            for finding in analysis["findings"]:

                with st.expander(
                    f"⚠️ {finding['category']}"
                ):

                    st.write(
                        "**Matched phrase:**",
                        finding["matched_phrase"]
                    )

                    st.write(
                        "**Recommendation:**",
                        finding["recommendation"]
                    )

        else:
            st.success(
                "No demonstration policy rules matched."
            )

    else:
        st.warning("Could not retrieve the selected analysis.")

else:
    st.info("No historical analysis available.")




# Product Image Gallery
st.divider()

st.header("🖼️ Product Image Gallery")

image_folder = PROJECT_ROOT / "images"
image_folder.mkdir(parents=True, exist_ok=True)

# Upload Product Images
uploaded_images = st.file_uploader(
    "Upload Product Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_images and st.button("Save Uploaded Images"):

    uploaded_count = 0

    for uploaded_file in uploaded_images:

        save_path = image_folder / uploaded_file.name
        counter = 1

        # Prevent overwriting existing images
        while save_path.exists():

            original_name = Path(uploaded_file.name)

            new_name = (
                f"{original_name.stem}_{counter}"
                f"{original_name.suffix}"
            )

            save_path = image_folder / new_name
            counter += 1

        with open(save_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        uploaded_count += 1

    st.success(
        f"{uploaded_count} image(s) uploaded successfully!"
    )

    st.rerun()


# Load Product Images
image_files = [
    file for file in image_folder.iterdir()
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
]

if image_files:

    # Image Search
    st.subheader("🔎 Search Product Images")

    search_query = st.text_input(
        "Search by image filename",
        placeholder="Enter a filename..."
    )

    filtered_images = [
        file for file in image_files
        if search_query.lower() in file.name.lower()
    ]

    st.write(f"Images found: {len(filtered_images)}")

    if filtered_images:

        columns = st.columns(3)

        for index, image_file in enumerate(filtered_images):

            with columns[index % 3]:

                st.image(
                    str(image_file),
                    caption=image_file.name,
                    use_container_width=True
                )

                if st.button(
                    "View Image",
                    key=f"view_{image_file.name}"
                ):
                    st.session_state["selected_image"] = str(image_file)

        # Display selected image
        selected_image = st.session_state.get("selected_image")

        if selected_image and Path(selected_image).exists():

            st.divider()
            st.subheader("🔍 Selected Product Image")

            st.image(
                selected_image,
                use_container_width=True
            )

    else:
        st.info("No images match your search.")

else:
    st.info("No product images available.")


# Footer
st.divider()

st.caption(
    "E-Commerce Visual Search & Policy Compliance Copilot | "
    "Academic AI Demonstration Project"
)
