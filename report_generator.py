from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(summary, insights, answer=None):

    filename = "report.pdf"

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>Data Analyst AI Report</b>",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Dataset Summary</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Rows: {summary['rows']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Columns: {summary['columns']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Missing Values: {summary['total_missing_values']}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"]
        )
    )

    for insight in insights:

        elements.append(

            Paragraph(
                f"• {insight}",
                styles["Normal"]
            )

        )

    if answer:

        elements.append(Spacer(1, 20))

        elements.append(

            Paragraph(
                "<b>Latest AI Response</b>",
                styles["Heading2"]
            )

        )

        elements.append(

            Paragraph(
                answer,
                styles["Normal"]
            )

        )

    document.build(elements)

    return filename