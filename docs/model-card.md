# Model Card — Incident Classification Reference

## Intended use

Recommend incident category, subcategory, assignment group, and potentially priority to support ServiceNow triage.

## Out-of-scope use

- autonomous remediation of high-impact systems without separate controls;
- employee performance evaluation;
- security enforcement decisions based solely on model output;
- decisions using data fields not approved for model processing.

## Evaluation expectations

A production model should report:

- per-class precision, recall, and F1;
- macro and weighted averages;
- confusion matrix;
- calibration / reliability;
- performance by major service or taxonomy segment;
- error analysis for high-impact classes;
- confidence distribution;
- performance over time.

## Data considerations

Incident data often contains inconsistent taxonomy, duplicate language, templated text, personal data, and historical routing bias. Data quality analysis is therefore part of model validation, not a separate cleanup task.

## Current repository implementation

The Python classifier in `src/classifier.py` is a deterministic demonstration scaffold and is **not represented as a trained production model**. The historical notebook remains the experimental artifact in this repository.
