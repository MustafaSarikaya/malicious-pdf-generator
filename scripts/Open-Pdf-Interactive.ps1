<#
.SYNOPSIS
    Opens a PDF file using Adobe Acrobat Reader in the interactive user session.

.DESCRIPTION
    This script creates a scheduled task to run the Open-PDF.ps1 script in the interactive session.

.PARAMETER PdfPath
    The full path to the PDF file to be opened.

.EXAMPLE
    .\Open-PDF-Interactive.ps1 -PdfPath "C:\pdfs\document.pdf"
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$PdfPath
)

# Variables
$taskName = "OpenPDFTask_$($env:USERNAME)_$(Get-Random)"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File `"C:\Users\vboxuser\scripts\Open-Pdf.ps1`" -PdfPath `"$PdfPath`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(5)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

# Create the scheduled task
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal

# Start the scheduled task
Start-ScheduledTask -TaskName $taskName

# Wait for the task to complete
Start-Sleep -Seconds 10

# Delete the scheduled task
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
