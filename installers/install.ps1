$engine = Join-Path $PSScriptRoot 'install.py'
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $engine @args
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $engine @args
} else {
    Write-Error 'Python 3 is required for the agent-stack installer.'
    exit 1
}
exit $LASTEXITCODE
