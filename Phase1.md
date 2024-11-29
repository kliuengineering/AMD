# Phase One - Infrastructure Setup

## Setting Up for Windows
Assuming we have a fresh windows 11 Pro installation, the steps are as follows:
1) Install chocolatey package manager using PowerShell script using: <br>
```Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) ```

2) Install Git <br>
``` choco install git -y ```

3) 