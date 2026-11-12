#!/usr/bin/env python3
"""Profile the supplied e-commerce CSVs without exporting individual records."""
import argparse
import csv
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        yield from csv.DictReader(handle)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_directory", type=Path)
    args = parser.parse_args()
    root = args.data_directory
    filenames = [
        "ecommerce_sales_customer_analytics_150k.csv",
        "order_items.csv", "customer_master.csv", "product_catalog.csv",
        "dataset_statistics.csv",
    ]
    missing = [name for name in filenames if not (root / name).is_file()]
    if missing:
        parser.error("Missing CSVs: " + ", ".join(missing))

    customer_ids, product_ids, order_ids = set(), set(), set()
    customers_used, products_used = set(), set()
    order_rows = line_rows = customer_rows = product_rows = 0
    duplicate_orders = duplicate_customers = duplicate_products = 0
    unknown_customers = orphan_lines = unknown_products = 0
    currencies, statuses = Counter(), Counter()
    categories = set()
    date_min = date_max = None
    order_sales = order_profit = line_sales = line_profit = Decimal("0")

    for row in rows(root / "customer_master.csv"):
        customer_rows += 1
        duplicate_customers += row["customer_id"] in customer_ids
        customer_ids.add(row["customer_id"])
    for row in rows(root / "product_catalog.csv"):
        product_rows += 1
        duplicate_products += row["product_id"] in product_ids
        product_ids.add(row["product_id"])
        categories.add(row["product_category"])
    for row in rows(root / "ecommerce_sales_customer_analytics_150k.csv"):
        order_rows += 1
        duplicate_orders += row["order_id"] in order_ids
        order_ids.add(row["order_id"])
        customers_used.add(row["customer_id"])
        unknown_customers += row["customer_id"] not in customer_ids
        currencies[row["currency"]] += 1
        statuses[row["order_status"]] += 1
        date = row["order_date"]
        date_min = date if date_min is None else min(date_min, date)
        date_max = date if date_max is None else max(date_max, date)
        order_sales += Decimal(row["net_sales"])
        order_profit += Decimal(row["profit"])
    for row in rows(root / "order_items.csv"):
        line_rows += 1
        products_used.add(row["product_id"])
        orphan_lines += row["order_id"] not in order_ids
        unknown_products += row["product_id"] not in product_ids
        line_sales += Decimal(row["net_sales"])
        line_profit += Decimal(row["profit"])

    report = {
        "rows": {"orders": order_rows, "order_items": line_rows,
                 "customer_master": customer_rows, "product_catalog": product_rows},
        "distinct": {"orders": len(order_ids), "customers_with_orders": len(customers_used),
                     "products_in_order_items": len(products_used), "categories": len(categories)},
        "date_range": {"from": date_min, "to": date_max},
        "duplicate_primary_keys": {"orders": duplicate_orders,
                                   "customers": duplicate_customers, "products": duplicate_products},
        "missing_parent_rows": {"orders_without_customer": unknown_customers,
                                "lines_without_order": orphan_lines, "lines_without_product": unknown_products},
        "currencies": dict(sorted(currencies.items())),
        "order_statuses": dict(sorted(statuses.items())),
        "unconverted_numeric_sums": {
            "orders": {"net_sales": str(order_sales), "profit": str(order_profit)},
            "order_items": {"net_sales": str(line_sales), "profit": str(line_profit)},
        },
        "notes": ["Numeric sums span multiple currencies and all order statuses.",
                  "Order-level and order-item sums are kept separate.",
                  "This profile does not execute the PBIX semantic model."],
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
