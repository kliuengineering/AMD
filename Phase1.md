# Phase One - Infrastructure Setup

## Setting Up for Windows
Assuming we have a fresh windows 11 Pro installation, the steps are as follows:
1) Install chocolatey package manager using PowerShell script using: <br>
```Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) ```

2) Install Git <br>
``` choco install git -y ```

3) Install Anaconda Navigator for Python 3; use the official Anaconda website for this.

4) Remember to add environment path for Python 3 (look up online or ChatGPT how to do it).

5) Rmember to check for Pip 3 and run the following if ``` pip --version ``` does not return anything. <br>
    ``` $set PATH=C:\...\anaconda\envs\ML\Scripts;%PATH% ``` <br>
    Again, add it to the path environment just like how we did for Python 3.
    