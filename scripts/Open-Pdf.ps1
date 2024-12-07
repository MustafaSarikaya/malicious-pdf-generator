

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$PdfPath
)

function Write-Log {
    param (
        [string]$Message,
        [string]$Level = 'INFO'
    )
    $timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    $logMessage = "[$timestamp] [$Level] $Message"
    Write-Host $logMessage
    # Optionally, write to a log file
    # Add-Content -Path 'C:\scripts\open_pdf.log' -Value $logMessage
}

try {
    # Check if the PDF file exists
    if (-Not (Test-Path -Path $PdfPath -PathType Leaf)) {
        Write-Log "The file '$PdfPath' does not exist." 'ERROR'
        exit 1
    }

    # Define possible Adobe Acrobat Reader paths
    $acrobatPaths = @(
        "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe",
        "C:\Program Files\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe",
        "C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
    )

    # Find the installed Adobe Acrobat Reader executable
    $acrobatPath = $acrobatPaths | Where-Object { Test-Path $_ } | Select-Object -First 1

    if (-Not $acrobatPath) {
        Write-Log "Adobe Acrobat Reader is not installed at the expected locations." 'ERROR'
        exit 1
    }

    Write-Log "Opening PDF file '$PdfPath' with Adobe Acrobat Reader."

    # Open the PDF file with corrected quotation
    Start-Process -FilePath $acrobatPath -ArgumentList ('"' + $PdfPath + '"')

    exit 0
}
catch {
    Write-Log "An unexpected error occurred: $_" 'ERROR'
    exit 1
}
