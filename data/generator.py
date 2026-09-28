"""
PulseMind Demo Data Generator

Member 1:
Product + Data + Demo Data Engineering
"""

import json
from datetime import date, timedelta
from pathlib import Path

TOTAL_RECORDS = 90

SOURCES = [
    "support",
    "app_review",
    "survey",
    "social",
    "community",
    "interview",
    "sales",
    "store_review",
]

SEGMENTS = ["Free", "Pro", "Business"]

PRODUCT_AREAS = [
    "Reporting",
    "Authentication",
    "Search",
    "Dashboard",
    "Appearance",
]

OUTPUT_FILE = Path("mock-data/feedback.json")


def make_record(
    record_id,
    source,
    record_date,
    raw_text,
    product_area,
    feature,
    sentiment,
    severity,
    theme,
    user_segment,
    problem,
):
    return {
        "id": record_id,
        "source": source,
        "date": record_date.isoformat(),
        "rawText": raw_text,
        "productArea": product_area,
        "feature": feature,
        "sentiment": sentiment,
        "severity": severity,
        "theme": theme,
        "userSegment": user_segment,
        "problem": problem,
    }


def generate_feedback():
    feedback = []
    counter = 1

    # ---------------------------------------------------------
    # PHASE 1 — CSV complaints rise
    # 31 complaints
    # ---------------------------------------------------------
    csv_complaints = [
        "CSV export is taking too long.",
        "The CSV download is extremely slow.",
        "Exporting a report to CSV takes too much time.",
        "CSV generation becomes slow with larger reports.",
        "I have to wait too long for CSV exports.",
        "CSV export performance is getting worse.",
        "Large CSV exports frequently take several minutes.",
        "The report export seems stuck before downloading.",
        "CSV downloads are slower than before.",
        "Exporting customer data to CSV is painfully slow.",
        "CSV export delays are affecting our workflow.",
        "Our team waits too long for CSV reports.",
        "CSV export is slow when the report has many rows.",
        "The download spinner stays for a long time during CSV export.",
        "CSV reports are taking too long to generate.",
        "Exporting data to CSV is becoming unreliable and slow.",
        "CSV export performance needs improvement.",
        "The CSV download is very slow for our account.",
        "Generating CSV reports takes too much time.",
        "CSV export is causing delays for our team.",
        "Large CSV reports are especially slow.",
        "The CSV export process feels much slower this week.",
        "CSV downloads take several minutes to complete.",
        "I experienced another slow CSV export today.",
        "Our business users are complaining about CSV speed.",
        "CSV export is too slow for daily reporting.",
        "The export takes too long before the file appears.",
        "CSV generation slows down when the dataset is large.",
        "CSV export latency is becoming a serious problem.",
        "We need faster CSV report generation.",
        "CSV export is still taking too long.",
    ]

    for i, text in enumerate(csv_complaints):
        severity = "medium" if i < 18 else "high"

        feedback.append(
            make_record(
                f"MEM-{counter:05d}",
                SOURCES[i % len(SOURCES)],
                date(2026, 5, 18) + timedelta(days=i % 14),
                text,
                "Reporting",
                "CSV Export",
                "negative",
                severity,
                "performance",
                SEGMENTS[(i + 1) % len(SEGMENTS)],
                "Slow CSV exports",
            )
        )
        counter += 1

    # ---------------------------------------------------------
    # PHASE 3 — CSV complaints fall
    # 9 complaints
    # ---------------------------------------------------------
    csv_after = [
        "CSV export is still slow for very large reports.",
        "Some CSV downloads continue to take longer than expected.",
        "CSV export improved but occasional delays remain.",
        "A large CSV report took longer than expected.",
        "CSV generation is better but can still be slow.",
        "One CSV export was slower than usual today.",
        "CSV export has occasional performance delays.",
        "Large CSV files still need some optimization.",
        "CSV export is mostly faster but a few delays remain.",
    ]

    for i, text in enumerate(csv_after):
        feedback.append(
            make_record(
                f"MEM-{counter:05d}",
                SOURCES[(i + 2) % len(SOURCES)],
                date(2026, 6, 10) + timedelta(days=i),
                text,
                "Reporting",
                "CSV Export",
                "negative",
                "medium",
                "performance",
                SEGMENTS[(i + 1) % len(SEGMENTS)],
                "Slow CSV exports",
            )
        )
        counter += 1

    # Positive feedback after DEC-017
    csv_positive = [
        "CSV exports are much faster now.",
        "The CSV download completed quickly today.",
        "Our reporting workflow is faster after the CSV improvement.",
        "CSV generation performance has improved significantly.",
        "The CSV export is much better than before.",
    ]

    for i, text in enumerate(csv_positive):
        feedback.append(
            make_record(
                f"MEM-{counter:05d}",
                SOURCES[(i + 4) % len(SOURCES)],
                date(2026, 6, 15) + timedelta(days=i),
                text,
                "Reporting",
                "CSV Export",
                "positive",
                "low",
                "praise",
                SEGMENTS[i % len(SEGMENTS)],
                "CSV export improvement",
            )
        )
        counter += 1

    # ---------------------------------------------------------
    # PHASE 4 — PDF complaints rise
    # 14 complaints
    # ---------------------------------------------------------
    pdf_complaints = [
        "PDF export is becoming slow.",
        "Generating PDF reports takes too long.",
        "The PDF download is slower than expected.",
        "PDF reports sometimes take several minutes.",
        "PDF export performance has started getting worse.",
        "The PDF export spinner stays for too long.",
        "Our PDF reports are taking too much time to generate.",
        "PDF generation is slow for larger reports.",
        "The PDF download is becoming unreliable.",
        "PDF export is causing delays for our users.",
        "Generating a PDF report takes much longer now.",
        "PDF export speed needs improvement.",
        "Large PDF reports are especially slow.",
        "We are seeing repeated delays with PDF exports.",
    ]

    for i, text in enumerate(pdf_complaints):
        feedback.append(
            make_record(
                f"MEM-{counter:05d}",
                SOURCES[(i + 1) % len(SOURCES)],
                date(2026, 6, 4) + timedelta(days=i),
                text,
                "Reporting",
                "PDF Export",
                "negative",
                "medium" if i < 7 else "high",
                "performance",
                SEGMENTS[i % len(SEGMENTS)],
                "Slow PDF exports",
            )
        )
        counter += 1

    # ---------------------------------------------------------
    # OTHER PRODUCT FEEDBACK
    # 31 records
    # ---------------------------------------------------------
    other_feedback = [
        (
            "Login sometimes takes too long.",
            "Authentication",
            "Login",
            "negative",
            "medium",
            "performance",
            "Slow mobile login",
        ),
        (
            "Mobile login occasionally fails on the first attempt.",
            "Authentication",
            "Mobile Login",
            "negative",
            "medium",
            "bug",
            "Mobile login issue",
        ),
        (
            "Search results are not always accurate.",
            "Search",
            "Search",
            "negative",
            "medium",
            "usability",
            "Search accuracy",
        ),
        (
            "Search should provide more relevant results.",
            "Search",
            "Search",
            "negative",
            "low",
            "feature_request",
            "Search accuracy",
        ),
        (
            "The dashboard customization options are limited.",
            "Dashboard",
            "Dashboard Customization",
            "negative",
            "low",
            "feature_request",
            "Dashboard customization",
        ),
        (
            "I would like more dashboard layout options.",
            "Dashboard",
            "Dashboard Customization",
            "negative",
            "low",
            "feature_request",
            "Dashboard customization",
        ),
        (
            "The new dashboard is easy to use.",
            "Dashboard",
            "Dashboard",
            "positive",
            "low",
            "praise",
            "Dashboard usability",
        ),
        (
            "Mobile login worked quickly today.",
            "Authentication",
            "Mobile Login",
            "positive",
            "low",
            "praise",
            "Mobile login improvement",
        ),
        (
            "Search is returning useful results.",
            "Search",
            "Search",
            "positive",
            "low",
            "praise",
            "Search experience",
        ),
        (
            "The reporting dashboard is useful.",
            "Dashboard",
            "Reporting Dashboard",
            "positive",
            "low",
            "praise",
            "Dashboard usability",
        ),
        (
            "I like the new report layout.",
            "Reporting",
            "Reports",
            "positive",
            "low",
            "praise",
            "Reporting usability",
        ),
        (
            "The application is easy to navigate.",
            "Dashboard",
            "Navigation",
            "positive",
            "low",
            "praise",
            "Usability",
        ),
        (
            "The search page feels confusing.",
            "Search",
            "Search",
            "negative",
            "medium",
            "usability",
            "Search usability",
        ),
        (
            "Search sometimes returns duplicate results.",
            "Search",
            "Search",
            "negative",
            "medium",
            "bug",
            "Search accuracy",
        ),
        (
            "Dashboard widgets should be easier to rearrange.",
            "Dashboard",
            "Widgets",
            "negative",
            "low",
            "feature_request",
            "Dashboard customization",
        ),
        (
            "The dashboard loads quickly.",
            "Dashboard",
            "Dashboard",
            "positive",
            "low",
            "praise",
            "Dashboard performance",
        ),
        (
            "Login takes longer on mobile networks.",
            "Authentication",
            "Mobile Login",
            "negative",
            "medium",
            "performance",
            "Mobile login",
        ),
        (
            "The login screen is simple and clear.",
            "Authentication",
            "Login",
            "positive",
            "low",
            "praise",
            "Login usability",
        ),
        (
            "Search filters could be improved.",
            "Search",
            "Search Filters",
            "negative",
            "low",
            "feature_request",
            "Search usability",
        ),
        (
            "Reports are easy to understand.",
            "Reporting",
            "Reports",
            "positive",
            "low",
            "praise",
            "Reporting usability",
        ),
        (
            "The dashboard needs more customization.",
            "Dashboard",
            "Dashboard Customization",
            "negative",
            "medium",
            "feature_request",
            "Dashboard customization",
        ),
        (
            "The app review shows a smooth dashboard experience.",
            "Dashboard",
            "Dashboard",
            "positive",
            "low",
            "praise",
            "Dashboard usability",
        ),
        (
            "Search sometimes feels slow.",
            "Search",
            "Search",
            "negative",
            "medium",
            "performance",
            "Search performance",
        ),
        (
            "Mobile login is convenient.",
            "Authentication",
            "Mobile Login",
            "positive",
            "low",
            "praise",
            "Mobile login",
        ),
        (
            "I want saved search preferences.",
            "Search",
            "Search Preferences",
            "negative",
            "low",
            "feature_request",
            "Search feature request",
        ),
        (
            "The reporting section is useful for our team.",
            "Reporting",
            "Reports",
            "positive",
            "low",
            "praise",
            "Reporting usability",
        ),
        (
            "The dashboard widgets sometimes reset.",
            "Dashboard",
            "Widgets",
            "negative",
            "medium",
            "bug",
            "Dashboard customization",
        ),
        (
            "Login was successful and fast.",
            "Authentication",
            "Login",
            "positive",
            "low",
            "praise",
            "Login performance",
        ),
        (
            "Search results should be ranked more accurately.",
            "Search",
            "Search",
            "negative",
            "medium",
            "feature_request",
            "Search accuracy",
        ),
        (
            "The dashboard is much easier to use now.",
            "Dashboard",
            "Dashboard",
            "positive",
            "low",
            "praise",
            "Dashboard usability",
        ),
        (
            "The appearance settings are difficult to find.",
            "Appearance",
            "Appearance Settings",
            "negative",
            "low",
            "usability",
            "Appearance usability",
        ),
    ]

    for i, item in enumerate(other_feedback):
        (
            text,
            product_area,
            feature,
            sentiment,
            severity,
            theme,
            problem,
        ) = item

        feedback.append(
            make_record(
                f"MEM-{counter:05d}",
                SOURCES[(i + 3) % len(SOURCES)],
                date(2026, 5, 20) + timedelta(days=i),
                text,
                product_area,
                feature,
                sentiment,
                severity,
                theme,
                SEGMENTS[(i + 2) % len(SEGMENTS)],
                problem,
            )
        )
        counter += 1

    assert len(feedback) == TOTAL_RECORDS, (
        f"Expected {TOTAL_RECORDS} records, got {len(feedback)}"
    )

    return feedback


def main():
    feedback = generate_feedback()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=2)

    print("PulseMind feedback dataset generated successfully.")
    print(f"Total records: {len(feedback)}")
    print("CSV complaints before: 31")
    print("CSV complaints after: 9")
    print("PDF complaints: 14")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()