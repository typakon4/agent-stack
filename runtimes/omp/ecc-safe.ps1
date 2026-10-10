#Requires -Version 7.0
[CmdletBinding()]
param(
    [string]$Workspace = (Get-Location).Path,
    [ValidateNotNullOrEmpty()][string]$Model = 'openai/gpt-5.2',
    [switch]$Rpc,
    [switch]$NoSession,
    [switch]$Check
)
$ErrorActionPreference = 'Stop'
$omp = Join-Path $env:LOCALAPPDATA 'omp/omp.exe'
$source = Join-Path $HOME 'Documents/ECC-ef648e01899b'
$profile = Join-Path $HOME '.omp/profiles/ecc-safe/agent'
$extension = Join-Path $source '.pi/extensions/index.ts'
$config = Join-Path $profile 'config.yml'
$node = (Get-Command node.exe -CommandType Application -ErrorAction Stop).Source
foreach ($path in @($omp, $extension, $config, $node)) {
    if (!(Test-Path -LiteralPath $path -PathType Leaf)) { throw "Required file missing: $path" }
}
$Workspace = (Resolve-Path -LiteralPath $Workspace).Path
if (!(Test-Path -LiteralPath $Workspace -PathType Container)) { throw 'Workspace must be a directory.' }
$pin = & git -C $source rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $pin -ne 'ef648e01899ba3e8dc6371642deaaf64b4477775') {
    throw 'ECC checkout must remain at the reviewed pin; do not update it in place.'
}
$launchArgs = @('--profile', 'ecc-safe', '--cwd', $Workspace, '--config', $config,
    '--trusted-extension', $extension, '--no-extensions', '--no-rules', '--no-title',
    '--append-system-prompt', (Join-Path $PSScriptRoot '../../shared/instructions/verification.md'))
$launchArgs += @('--model', $Model)
if ($Rpc) { $launchArgs += @('--mode', 'rpc', '--no-ui') }
if ($NoSession) { $launchArgs += '--no-session' }
$child = New-Object System.Diagnostics.ProcessStartInfo
$child.FileName = $omp
$child.UseShellExecute = $false
foreach ($argument in $launchArgs) { $child.ArgumentList.Add($argument) }
$child.EnvironmentVariables.Remove('PI_CONFIG_DIR')
$child.EnvironmentVariables.Remove('PI_CONFIG_FILES')
$child.EnvironmentVariables['ECC_PI_RULES'] = 'off'
$child.EnvironmentVariables['ECC_HOOKS_ENABLED'] = 'false'
$child.EnvironmentVariables['ECC_DISABLED_HOOKS'] = 'session:start,session:end:marker'
$child.EnvironmentVariables['ECC_HOOK_NODE'] = $node
$child.EnvironmentVariables['ECC_AGENT_DATA_HOME'] = Join-Path $profile 'ecc-data'
$child.EnvironmentVariables['CLV2_HOMUNCULUS_DIR'] = Join-Path $profile 'ecc-homunculus'
if ($Check) {
    [pscustomobject]@{ Executable = $omp; Profile = 'ecc-safe'; Pin = $pin; Extension = $extension;
        Node = $node; Workspace = $Workspace; Rules = 'off'; Hooks = 'false'; Arguments = $launchArgs }
    return
}
$process = [System.Diagnostics.Process]::Start($child)
$process.WaitForExit()
exit $process.ExitCode
