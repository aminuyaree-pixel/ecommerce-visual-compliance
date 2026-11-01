
from io import BytesIO
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def generate_pdf_report(description, detections, matches, findings):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#172554"),
        fontSize=18,
        spaceAfter=15
    )

    section_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#1D4ED8"),
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = styles["BodyText"]

    story = []

    def safe_text(value):
        return escape(str(value)).replace("\n", "<br/>")

    def add_section(title):
        story.append(Paragraph(title, section_style))

    def add_text(value):
        story.append(
            Paragraph(safe_text(value), body_style)
        )
        story.append(Spacer(1, 6))

    # Report title
    story.append(Paragraph(
        "E-Commerce AI Compliance Report",
        title_style
    ))

    add_text(
        "Generated: " +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    add_text(
        "Report type: AI-assisted product analysis"
    )

    # Product description
    add_section("1. Product Description")
    add_text(description)

    # YOLO detection
    add_section("2. YOLO Object Detection")

    if detections:
        detection_data = [["Detection Result"]]

        for detection in detections:
            detection_data.append([safe_text(detection)])

        table = Table(
            detection_data,
            colWidths=[450]
        )

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0),
             colors.HexColor("#DBEAFE")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 7)
        ]))

        story.append(table)

    else:
        add_text("No objects detected.")

    # CLIP visual search
    add_section("3. CLIP Visual Search")

    if matches:
        match_data = [
            ["Product Match", "Confidence"]
        ]

        for item in matches:
            match_data.append([
                safe_text(item.get("description", "Unknown")),
                f"{float(item.get('score', 0)):.2%}"
            ])

        table = Table(
            match_data,
            colWidths=[330, 120]
        )

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0),
             colors.HexColor("#DBEAFE")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 7)
        ]))

        story.append(table)

    else:
        add_text("No visual matches found.")

    # Policy findings
    add_section("4. Product Policy Review")

    if findings:
        add_text(
            "Potential policy concerns were identified. "
            "Human review is recommended."
        )

        for number, finding in enumerate(findings, 1):
            add_text(f"Finding {number}")
            add_text(
                "Category: " +
                str(finding.get("category", "Unknown"))
            )
            add_text(
                "Matched phrase: " +
                str(finding.get("matched_phrase", "Unknown"))
            )
            add_text(
                "Recommendation: " +
                str(finding.get("recommendation", "Review manually"))
            )

    else:
        add_text(
            "No matching demonstration rules were found."
        )

    # Disclaimer
    add_section("5. Important Disclaimer")

    add_text(
        "This report contains preliminary AI-assisted findings. "
        "Visual similarity scores are not verified product identities. "
        "The demonstration policy checker does not establish official "
        "marketplace policy violations. Human review is required "
        "before making compliance decisions."
    )

    document.build(story)

    buffer.seek(0)

    return buffer.getvalue()
