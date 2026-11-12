# E-Commerce Sales Dashboard

**A Power BI view of sales performance, profitability, and product-category trends.**

Built by **Cordirianto Alvian** to turn an e-commerce dataset into an interactive sales reporting experience.

**Project documentation is available below. The Power BI report and source-data release are prepared but not published yet.**

## Overview

This project brings together sales KPIs, monthly trends, and product-category comparisons on one dashboard. It supports an initial commercial performance review: how much is sold, how much profit is recorded, which categories contribute sales, and how category sales compare with profit margin.

The supplied report contains a single **1920 × 1080** page with a consistent sales-and-profitability layout, four KPI cards, three analytical charts, and two slicers.

## Business questions

- How do net sales, order volume, profit, and average order value compare within a selected period?
- How do recorded sales and profit change month by month?
- Which product categories contribute the most net sales?
- Which categories combine higher sales with stronger margins?
- How does the picture change when a product category or date range is selected?

## Dashboard features

| Component | What it shows |
| --- | --- |
| KPI cards | Total Net Sales, Total Orders, Total Profit, Average Order Value |
| Monthly line chart | Total Net Sales and Total Profit by Month Start |
| Category bar chart | Total Net Sales by product category |
| Sales vs. margin scatter plot | Category-level Total Net Sales and Profit Margin, with profit and order-count tooltips |
| Product Category filter | Dropdown slicer for category selection |
| Date Range filter | Between-date slicer using order date |

The scatter plot includes an **Overall Margin** reference line configured at **42.98%** in the uploaded report. This is a fixed value; see the interpretation notes below.

## Dataset

**Source:** Shair Khan (`datascikhan`), *E-Commerce Sales Analytics Dataset*, Kaggle.  
**[Open the original Kaggle dataset](https://www.kaggle.com/datasets/datascikhan/e-commerce-sales-and-customer-analytics)**  
The Kaggle listing identifies the dataset license as **CC0: Public Domain**. The source data is credited to its publisher; the dashboard is this portfolio's contribution.

The snapshot supplied for this project covers **1 January 2021–31 December 2025**:

| Source file | Rows | Role |
| --- | ---: | --- |
| `ecommerce_sales_customer_analytics_150k.csv` | 138,116 | Order-level sales and customer attributes; imported as `orders` in the report |
| `order_items.csv` | 397,569 | Product-level order lines and financial fields |
| `customer_master.csv` | 25,000 | Customer dimension |
| `product_catalog.csv` | 1,175 | Product dimension, covering 15 categories |
| `dataset_statistics.csv` | 1 | Publisher-supplied summary for the dataset snapshot |

The order file contains **138,116 unique orders** and **24,911 customers with orders**. Its filename includes `150k`, but the supplied snapshot contains the row count shown above.

## Tools and skills

- **Power BI:** report layout, KPI cards, charts, tooltips, and interactive slicers.
- **Power Query / data preparation:** loading and preparing source tables for analysis.
- **Data modeling:** working with customer, order, order-item, and product tables.
- **DAX measures:** sales, orders, profit, average order value, and profit-margin measures referenced by the report.
- **Validation:** a reproducible Python profiling script for table grain, keys, coverage, and numeric reconciliation.

## Open the dashboard

The following steps apply once the download files are published:

1. Download `E-Commerce-Sales-Dashboard.pbix` from the project's release assets.
2. Open it in a current compatible version of **Power BI Desktop**.
3. Use the Product Category dropdown and Date Range slicer to explore the report.
4. To refresh the data, download and extract `ecommerce-source-data.zip`, then use **Transform data → Data source settings** or the query Source steps to point the queries to your local CSV files.
5. Keep the model table names `orders`, `order_items`, `customer_master`, and `product_catalog` when changing source paths, and check that the relationships still filter the charts as intended.

The PBIX is the uploaded report, preserved byte-for-byte. The source-data ZIP contains the five supplied CSVs with duplicate-download suffixes removed from their filenames. These larger files are prepared for distribution as release assets; that release has not been published.

The PBIX download is pending publication. This repository does not yet include a published Power BI Service report link.

## Model and metric documentation

- [Data model and measure references](docs/data-model.md)
- [Data quality and interpretation notes](docs/data-quality.md)
- [Visual inventory extracted from the PBIX](docs/visual-inventory.json)

### Interpretation notes

- **Currency:** the order data contains seven currencies. A dollar format alone does not convert them. Cross-currency totals require a documented exchange-rate method before being interpreted as consolidated USD revenue.
- **Different source totals:** order-level and order-item sales/profit totals differ. The report visuals reference measures on `order_items`; the supplied statistics file aligns with the order-level source. Compare totals at the same grain.
- **Order status:** the source contains completed, pending, cancelled, and returned orders. Confirm the measure's status policy before treating a total as realized revenue.
- **Reference line:** the fixed 42.98% scatter benchmark does not recalculate as an overall-margin measure when slicers change.

These notes document the supplied report and data; this repository does not silently change the PBIX's calculations or report design.

## Reproduce the data checks

Download the five CSVs from the Kaggle source (or extract the source-data ZIP after publication), then run with Python 3 (standard library only):

```bash
python scripts/profile_data.py /path/to/extracted/csvs > data_profile.json
```

The script reports row counts, distinct keys, relationship coverage, currencies, order statuses, and separate order/line-level numeric totals. It does not export customer names or individual records.

## Repository contents

| Location | Contents |
| --- | --- |
| `README.md` | Project overview, dataset attribution, and usage instructions |
| `docs/` | Model references, interpretation notes, visual inventory, and file checksums |
| `scripts/profile_data.py` | Reproducible source-data profiling |
| [Release plan](docs/release-plan.md) | Prepared PBIX and source-data files; publication pending |

## Author

**Cordirianto Alvian**  
[Portfolio](https://cordiriantoalvian.github.io/cordirianto-alvian-portfolio/) · [GitHub](https://github.com/CordiriantoAlvian)
