# Data quality and interpretation

## Snapshot checks

The supplied CSV snapshot contains 138,116 order rows, 397,569 order-item rows, 25,000 customer-master rows, and 1,175 product rows. There are 24,911 customers represented in the orders and 15 product categories.

## Separate source totals

The sums below are direct numeric sums across all rows and statuses. They are **not currency-converted consolidated revenue** and are not a claim about the saved PBIX's filter context.

| Source | Net-sales numeric sum | Profit numeric sum |
| --- | ---: | ---: |
| Order-level CSV | 177,134,263.74 | 76,146,395.76 |
| Order-item CSV | 192,398,877.29 | 82,698,038.55 |

The supplied `dataset_statistics.csv` matches the order-level sums. The report's visual bindings reference measures on the `order_items` table. The discrepancy is present in the supplied source files and should be reconciled before financial use.

`Total Products Used` in the supplied statistics file is 138,116. It should not be interpreted as a distinct-product count: the catalog and order items contain 1,175 distinct product IDs.

## Currency

The order source includes USD, EUR, INR, CAD, GBP, AUD, and AED. A `$` display format is not evidence that the source values have been converted. A production model should preserve the original currency and document exchange-rate source, conversion date, and reporting currency.

## Order status

| Status | Order rows |
| --- | ---: |
| Completed | 113,559 |
| Pending | 6,697 |
| Cancelled | 8,398 |
| Returned | 9,462 |

The raw totals include all these statuses. Revenue reporting should explicitly define which statuses and returns adjustments are included.

## Static margin benchmark

The scatter plot's reference line is stored as `0.4298` (42.98%) and labeled `Overall Margin`. It is a constant in the report definition, so its value does not automatically recompute under category or date filters.

## Files and reproducibility

The report and CSV release assets retain the supplied file bytes. CSV filenames have only been normalized to remove duplicate-download suffixes. Checksums are recorded in `release-checksums.sha256`. No data-cleaning corrections, currency conversions, status filters, or DAX changes were applied to the original report as part of repository creation.
