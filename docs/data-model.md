# Data model and measure references

## Table grain and join keys

The PBIX diagram lists four model tables: `customer_master`, `orders`, `order_items`, and `product_catalog`. The following relationships describe the source join keys and expected grain; relationship direction and active status must be checked in Power BI Model view.

| Parent | Key | Child | Child key | Expected relationship |
| --- | --- | --- | --- | --- |
| `customer_master` | `customer_id` | `orders` | `customer_id` | One customer to many orders |
| `orders` | `order_id` | `order_items` | `order_id` | One order to many order lines |
| `product_catalog` | `product_id` | `order_items` | `product_id` | One product to many order lines |

Joining order totals to line items repeats an order's totals across its lines. Aggregate each financial measure at its intended grain before comparing results.

## Fields used in the report

| Model table | Referenced fields |
| --- | --- |
| `orders` | `order_date`, `Month Start` |
| `product_catalog` | `product_category` |
| `order_items` | `Total Net Sales`, `Total Orders`, `Total Profit`, `Average Order Value`, `Profit Margin` |

The report definition exposes the measure names and visual bindings. It does not expose the DAX expressions in the extracted report JSON; the measure formulas remain in the PBIX semantic model. No unverified formula is presented here as an extraction from the model.

## Metric definitions to confirm in the model

| Measure | Business meaning | Validation |
| --- | --- | --- |
| Total Net Sales | Net sales under the current filter context | Confirm source table, status exclusions, and currency policy. |
| Total Orders | Number of unique orders | Check distinct orders rather than counting order lines. |
| Total Profit | Profit under the current filter context | Confirm source table and included costs. |
| Average Order Value | Sales divided by unique orders | Use sales and orders from matching scope and filters. |
| Profit Margin | Profit divided by sales | Use a ratio of totals rather than a simple mean of row percentages. |

## Validation scope

Repository preparation checked the PBIX ZIP structure and parsed its report/page/visual JSON. The report was not opened or recalculated in Power BI Desktop during this preparation. CSV checks are reproducible with `scripts/profile_data.py`; they do not establish the saved DAX measure results or relationship-filter behavior.
