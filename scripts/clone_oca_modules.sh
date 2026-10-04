#!/bin/bash
# Script to clone popular OCA Enterprise-alternative modules for Odoo 18.0

ODOO_VERSION="${1:-18.0}"
TARGET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../oca" && pwd)"

echo "Cloning OCA modules for version ${ODOO_VERSION} into ${TARGET_DIR}..."

repos=(
    "https://github.com/OCA/helpdesk.git"
    "https://github.com/OCA/contract.git"
    "https://github.com/OCA/field-service.git"
    "https://github.com/OCA/dms.git"
    "https://github.com/OCA/account-financial-reporting.git"
    "https://github.com/OCA/account-financial-tools.git"
    "https://github.com/OCA/payroll.git"
    "https://github.com/OCA/stock-logistics-barcode.git"
    "https://github.com/OCA/delivery-carrier.git"
)

for repo in "${repos[@]}"; do
    repo_name=$(basename "$repo" .git)
    destination="${TARGET_DIR}/${repo_name}"
    if [ ! -d "$destination" ]; then
        echo "Cloning $repo_name (branch $ODOO_VERSION)..."
        git clone --depth 1 -b "$ODOO_VERSION" "$repo" "$destination" || echo "Branch $ODOO_VERSION not yet available for $repo_name, skipping."
    else
        echo "$repo_name already exists in oca/, skipping."
    fi
done

echo "Done! Remember to run 'docker compose restart web' and 'Update Apps List' in Odoo."
