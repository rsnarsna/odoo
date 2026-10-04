param(
    [string]$OdooVersion = "18.0"
)

$TargetDir = Join-Path $PSScriptRoot "..\oca"
Write-Host "Cloning OCA modules for version $OdooVersion into $TargetDir..." -ForegroundColor Cyan

$repos = @(
    "https://github.com/OCA/helpdesk.git",
    "https://github.com/OCA/contract.git",
    "https://github.com/OCA/field-service.git",
    "https://github.com/OCA/dms.git",
    "https://github.com/OCA/account-financial-reporting.git",
    "https://github.com/OCA/account-financial-tools.git",
    "https://github.com/OCA/payroll.git",
    "https://github.com/OCA/stock-logistics-barcode.git",
    "https://github.com/OCA/delivery-carrier.git"
)

foreach ($repo in $repos) {
    $repoName = [System.IO.Path]::GetFileNameWithoutExtension($repo)
    $dest = Join-Path $TargetDir $repoName
    if (-not (Test-Path $dest)) {
        Write-Host "Cloning $repoName (branch $OdooVersion)..." -ForegroundColor Yellow
        git clone --depth 1 -b $OdooVersion $repo $dest
    } else {
        Write-Host "$repoName already exists in oca/, skipping." -ForegroundColor Gray
    }
}

Write-Host "Done! Remember to run 'docker compose restart web' and 'Update Apps List' in Odoo." -ForegroundColor Green
