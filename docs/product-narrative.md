# PulseMind — Product Narrative

## Purpose

This document is the single source of truth for the PulseMind demo story.

The demo follows one continuous product-memory chain:

Customer Feedback → Decision → Outcome → New Feedback → Detection → Recommendation

---

## Phase 1 — CSV Export Complaints Rise

During the first part of the product timeline, customers increasingly report
that CSV exports are slow.

The complaints become more severe over time, moving from medium toward high
severity.

The dataset contains 31 CSV-export complaints that form the evidence for the
later product decision.

Key evidence:

- 31 customer complaints
- Product area: Reporting
- Feature: CSV Export
- Main theme: Performance
- Affected segments include Pro and Business
- Relevant memory records include MEM-00089 and MEM-00091

---

## Phase 2 — Decision DEC-017

On 2026-06-04, the product team records decision DEC-017.

### Problem

Slow CSV exports.

### Decision

Optimize CSV generation.

### Affected users

- Pro
- Business

### Expected outcome

50% reduction in complaints.

The decision becomes part of product memory.

---

## Phase 3 — CSV Complaints Fall

After the CSV optimization decision, CSV complaints decrease.

The measured comparison is:

31 complaints → 9 complaints

This represents approximately a 71% reduction.

Some customers also provide positive feedback indicating that
CSV exports are now faster.

The outcome is recorded as:

- Decision: DEC-017
- Status: effective
- Before: 31 complaints
- After: 9 complaints
- Improvement: 71%
- Measured: 2026-06-25

---

## Phase 4 — PDF Export Complaints Rise

While the CSV problem improves, a separate PDF export problem begins
appearing in the feedback.

The execution plan specifies:

5 PDF complaints → 14 PDF complaints

The increase is described in the execution plan as 188%.

This value must remain aligned with the final team-approved dataset and
demo narrative.

The PDF issue appears across:

- Free
- Pro
- Business

This creates a new signal that was not addressed by DEC-017.

---

## Phase 5 — Pattern Detection

PulseMind's memory and reflection layer identifies PDF export as an
emerging or recurring issue.

The system connects the new PDF feedback with historical product memory.

The important distinction is:

DEC-017 addressed CSV export performance.

The emerging issue concerns PDF export performance.

Therefore, the previous decision does not automatically solve the new
problem.

---

## Phase 6 — Recommendation

PulseMind produces the recommendation:

> Investigate PDF export performance.

The recommendation is grounded in:

1. Recent PDF export complaints.
2. The increasing PDF complaint trend.
3. Historical memory of DEC-017.
4. The measured effectiveness of the CSV optimization.
5. The distinction between CSV and PDF export problems.

The recommendation should explain why the previous CSV intervention
does not cover the emerging PDF issue.

---

# Core Demo Chain

```text
CSV complaints
      ↓
31 complaints
      ↓
DEC-017
Optimize CSV generation
      ↓
CSV complaints fall
      ↓
31 → 9
71% improvement
      ↓
New PDF complaints appear
      ↓
PDF issue detected
      ↓
Investigate PDF export performance