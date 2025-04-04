# Phase Three - Phoenix Migration
- ***This may not be available to the public at the time writing this.***

## Table of Contents





## The Context
- This is the latest openSIL library (March, 2025);
- Phoenix code base has many more unit tests and fake/mock/stub libraries available;
- There are many things needed to be done to set up the environment.





## Step by Step Guide

### Pre-req
1. At this point, we need to ensure ```Phase1.md``` and ```Phase2.md``` are working properly;
2. Ensure SSH key is used for Github.
3. Installs Chocolatey:
    - Install chocolatey either via terminal or the official website;
    - If you already have chocolatey, then use this to check what have already been installed: ```choco list -r```
4. For step #3 in "Setting UP" section, you need to ensure the WindowsSDK folder has the following:
    - ```~/WindowsSDK/10/bin```
    - ```~/WindowsSDK/10/include```
    - ```~/WindowsSDK/10/Lib```
    - otherwise build will fail at step #11

### Setting Up
1. Create ```C:/DevelopPhx ```
2. ```cd C:/DevelopPhx``` and then ```git clone git@github.com:AMD-OpenSIL/Seneca.git ./```
3. Copy from your OLD project the contents of BuildTools/BuildTools into
  the NEW BuildTools folder. <br>
  Should be copying: 
    - ASL (read step 4), 
    - MSVC, 
    - NASM (read step 5), 
    - Perl, 
    - WindowsSDK
4. Download ASL: <br>
    - https://www.intel.com/content/www/us/en/download/774849/774850/acpi-component-architecture-downloads-previous-releases-2020.html
    - Selects the option download ```iasl-win-20200110.zip```
    - Unzips it then place the contents into ```BuildTools/ASL/20200110```
    - For example you should have the path ```BuildTools/ASL/20200110/iasl.exe``` once complete.
    - I have also included in the ```~/assets/tools/``` directory of this repo.
5. Download NASM:
    - Go to this link https://www.nasm.us/pub/nasm/releasebuilds/2.15.05/win64/
    and download ```nasm-2.15.05-win64.zip```.
    - Unzip it then go inside the directory, copy the directory nasm-2.15.05 directly into the BuildTools folder.
    - For example you should have the path ```~/BuildTools/nasm-2.15.05/nasm.exe``` once complete.
    - I have also included in the ```~/assets/tools/``` directory of this repo.
6. Local Python Env:
    - Inside BuildTools create a Python folder;
    - From https://www.python.org/downloads/release/python-3114/ download Windows embeddable package (64-bit);
    - I have also included in the ```~/assets/tools/``` directory of this repo.
    - Unzip and copy the folder to your BuildTools/Python folder;
    - In BuildTools/Python, rename python-3.11.4-embed-amd64 to ```3.11.4.S0```
    - Go into the 3.11.4.S0 folder, Rename python311._pth to ```python311.pth```
    - Open python311.pth and uncomment line 5 (import site)
7. Need to acquire GNU Make v4.3 for Windows. Easiest way is through chocolatey package manager:
    - In administrator powershell run: ```choco install make --version=4.3```
    - Copy ```C:\ProgramData\chocolatey\lib\make\tools\install\bin\make.exe``` into folder ```~/BuildTools/MAKE/```
    - I have also included in the ```~/assets/tools/``` directory of this repo.
8. Runs ```C:\DevelopPhx``` back to the root.
9. Creates a directory named ```edk2```
10. Goes into edk2, and then:
    - Runs ```git clone -b edk2-stable202308 https://github.com/tianocore/edk2.git ./edk2-stable202308```
    - Runs ```cd edk2-stable202308```
    - Runs ```git submodule update --init```
        - During this command you will probably be asked to sign in then may encounter some errors. Ignore these errors and move on.
    - Runs ```cd MdePkg\Library\MipiSysTLib\mipisyst```
    - Runs ```git checkout 370b594```
    - Runs ```cd ..\..\..\..\UnitTestFrameworkPkg\Library\CmockaLib\cmocka```
    - Runs ```git checkout 1cc9cde```
    - Runs ```cd ..\..\GoogleTestLib\googletest```
    - Runs ```git checkout 86add13```
11. CheckPoint - we should now be able to run ```ae.cmd 2M unit-test``` from the root directory.

### Configuring Dispatcher and Coverage Report

1. Copy your scripts folder from ```~\[OLD_WORKSPACE\unittest\unit_test_framework\Platform\AmdCommonPkg\Test\UnitTest\Scripts```
  to ```~\[NEW_WORKSPACE]\AGESA\AmdOuiPkg\UnitTest```
2. Within the scripts Coverage and Dispatcher folders, update the config json files
  to match the new directory. Remember to use double backslash
  Notes on this:
    - In dispatcher_configs.json, the following changes are made:
        - ```"InPath"          : "C:\\[Your New Repo]\\Build\\AgesaModulePkg\\HostTest\\NOOPT_VS2019\\IA32",```
        - ```"OutPath"         : "C:\\[Your New Repo]\\Results",```
        - ```"RepoPath"        : "C:\\[Your New Repo]",```
        - ```"DynamoRioPath"   : "C:\\[...]\\DynamoRIO-Windows-10.0.0",```
        - ```"TestProfile"     : "C:\\[Your New Repo]\\AGESA\\AmdOuiPkg\\UnitTest\\SoC\\Phx\\SoC\\PhxUtMainProfile.json",```
        - ```"PerlPath"        : "C:\\[...]\\Strawberry\\perl\\bin"```
    - In report_configs.json, the following changes are made:
        - ```  "InPath"                : "C:\\DevelopPhx\\Results",```
        - ```  "OutPath"               : "C:\\DevelopPhx\\Reports",```
        - ```  "RepoPath"              : "C:\\DevelopPhx",```
        - ```  "DynamoRioPath"         : "C:\\Programs\\DynamoRIO-Windows-10.0.0",```
        - ```  "SrcFileList"           : "C:\\DevelopPhx\\AGESA\\AmdOuiPkg\\UnitTest\\SoC\\Phx\\SilPhxFiles.json",```
        - ```  "PerlPath"              : "C:\\Strawberry\\perl\\bin"```
3. Makes the following changes to dispatcher.py:
    - Line 15: AGESA="AGESA"
    - Line 19: OUI="AGESA\AmdOuiPkg"
    - Line 20: OPENSIL="{}/openSIL".format(OUI)
    - Line 170: ut.cfg_path = os.path.join(repo_path, test["ConfigFile"])
4. Make the followings edits to report.py:
    - Line 61: if "Platform" not in items[0]:
    - Line 64: return items[0]["Platform"]
5. Make the following edits to AGESA\AmdOuiPkg\UnitTest\SoC\Phx\SilPhxFiles.json
    - Delete lines 114-118 inclusive
    - Then, delete lines 61-65 inclusive
6. Make the following edits to AGESA\AmdOuiPkg\UnitTest\SoC\Common\SilCmnFiles.json
    - Delete lines 108-114 inclusive

### Completion - Run Scripts
- At this point the dispatcher and coverage tools should be working as before
    - ```cd C:\DevelopPhx\AGESA\AmdOuiPkg\UnitTest\Scripts\Dispatcher```
        - ```python dispatcher.py dispatcher_configs.json```
    - ```cd C:\DevelopPhx\AGESA\AmdOuiPkg\UnitTest\Scripts\Coverage```
        - ```python report.py report_configs.json```