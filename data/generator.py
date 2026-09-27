"""
PulseMind Demo Data Generator

Member 1:
Product + Data + Demo Data Engineering

This file will generate the frozen synthetic feedback dataset
for the PulseMind hackathon demo.
"""

from datetime import date, timedelta


# ============================================================
# PULSEMIND DEMO STORY
# ============================================================

DECISION_ID = "DEC-017"

CSV_BEFORE_COMPLAINTS = 31
CSV_AFTER_COMPLAINTS = 9

PDF_BEFORE_COMPLAINTS = 5
PDF_AFTER_COMPLAINTS = 14

TOTAL_RECORDS = 90


# ============================================================
# NARRATIVE PHASES
# ============================================================

PHASES = {
    1: "CSV complaints rise",
    2: "Decision DEC-017",
    3: "CSV complaints fall",
    4: "PDF complaints rise",
    5: "Pattern detection",
    6: "Recommendation",
}


# ============================================================
# DATA SOURCES FROM THE FROZEN CONTRACT
# ============================================================

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


SEGMENTS = [
    "Free",
    "Pro",
    "Business",
]


# ============================================================
# PRODUCT AREAS
# ============================================================

PRODUCT_AREAS = [
    "Reporting",
    "Authentication",
    "Search",
    "Dashboard",
    "Appearance",
]


# ============================================================
# PLACEHOLDER
# ============================================================

def generate_feedback():
    """
    Generate the final 90 feedback records.

    This function will be completed after the team freezes
    the PDF 5 -> 14 percentage interpretation.
    """

    feedback = []

    # Final record generation will be added here.

    return feedback


def main():
    print("PulseMind data generator")
    print("-------------------------")
    print(f"Target records: {TOTAL_RECORDS}")
    print(f"CSV complaints: {CSV_BEFORE_COMPLAINTS} -> {CSV_AFTER_COMPLAINTS}")
    print(f"PDF complaints: {PDF_BEFORE_COMPLAINTS} -> {PDF_AFTER_COMPLAINTS}")
    print()
    print("Final dataset generation is waiting for the team decision")
    print("on the PDF 5 -> 14 percentage stated in the execution plan.")


if __name__ == "__main__":
    main()