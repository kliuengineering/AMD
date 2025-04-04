# Phase One - Infrastructure Setup

## Table of Contents
1. [Builder Setup](#setting-up-for-windows)
2. [Framework Setup](#Framework-Setup)
3. [First Try](#First-Try)
4. [Configures VSCode Intellisense](#Configures-Intellisense)

## Setting Up for Windows

## Session 1

Assuming we have a fresh windows 11 Pro installation, the steps are as follows:
1) Install chocolatey package manager using PowerShell script using: <br>
```Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) ```

2) Install Git <br>
``` choco install git -y ```

3) Install Anaconda Navigator for Python 3; use the official Anaconda website for this.

4) Remember to add environment path for Python 3 (look up online or ChatGPT how to do it). <br>
    - Run ``` pip install mako ``` <br>
    - Run ``` pip install pygount ``` <br>

5) Rmember to check for Pip 3 and run the following if ``` pip --version ``` does not return anything. <br>
    ``` $set PATH=C:\...\anaconda\envs\ML\Scripts;%PATH% ``` <br>
    Again, add it to the path environment just like how we did for Python 3.

6) Create directories C:\Develop\unittest\

7) Install VS Code using ``` choco install vscode -y ```

8) Go into ~/unittest/ <br> 
``` git clone --recurse-submodules https://github.com/openSIL/opensil-uefi-interface.git AmdOpenSilPkg/opensil-uefi-interface ```

9) ``` cd AmdOpenSilPkg/opensil-uefi-interface ``` and then ``` git checkout genoa_poc ```

10) Go back to ~/unittest/, we will do ``` git clone https://github.com/openSIL/AGCL-R.git ``` and then ``` cd AGCL-R ``` and then ``` git checkout genoa_poc ```

11) Go back to ~/unittest/, then ``` git clone https://github.com/openSIL/EDKII-Platform.git Platform ``` and then cd into it, and then ``` git checkout genoa_poc ```

12) Go back to ~/unittest/, we will do ``` git clone https://github.com/openSIL/unit_test_framework.git ``` and then cd into it, and then checkout genoa_poc again.

13) We can do this step after step #27 <br>
cd into ``` ~/unittest/unit_test_framework/AmdOpenSilPkg/ ``` <br>
Copy the entire folder called "opensil-uefi-interface" to ``` ~/unittest/AmdOpoenSilPkg/ ``` <br>
replace everything in the destination (if any prompts).

14) Go back to ~/unittest/, we will do ``` git clone -b edk2-stable202205 https://github.com/tianocore/edk2.git ``` and then perform ``` cd edk2 ``` and then perform ``` git submodule update --init ```

15) Go back to ~/unittest/, we will do ``` git clone https://github.com/tianocore/edk2-platforms.git ``` and then cd into it, and then perform ``` git checkout b8ffb76b471dae5e24badcd9e04033e8c9439ce3 ```

16) Go back to ~/unittest/, we will do ``` git clone https://github.com/openSIL/amd_firmwares.git ``` <br>
Move all contents of ``` amd_firmwares/Firmwares/Genoa ``` into ``` AGCL-R/AgesaModulePkg/Firmwares/Genoa ```

17) Go to ``` ~/unittest/amd_firmwares/Firmwares/Genoa/ ``` and then move everything inside here to ```~/unittest/AGCL-R/AgesaModulePkg/Firmwares/Genoa/ ```

18) Go to ``` ~/unittest/Platform/PlatformTools/ ``` and then find root_dbuild.cmd, and move it to ``` ~/unittest/ ``` and then rename it to dbuild.cmd

19) Go to ``` ~/unittest/ ``` and create a directory called BuildTools, and then create another directory with the exact same name BuildTools inside it. So effectively it will look like ``` ~/unittest/BuildTools/BuildTools/ ```

20) Now, search for a .json file called buildtools.json, and look around to see all the packages that we need. For now, we can ignore ASL as they can be left out at this stage. For NASM, it will be installed together with Strawberry Perl later on, so we do not need to worry about NASM separately. 

21) Specifically, we need to get Visual Studio 2019 and its SDKs, and some Microsoft SDKs stated in the .json file, and Perl (5.40.XX).

22) Firstly, let's work on Visual Studio 2019 -> we will find the 2019 installer here in the ``` /assets/tools/ ``` from this repository. We will then install the 2019 Visual Studio, but only with 2 SDKs -> they are "Windows 10 SDK (10.0.19041.0)" and "MSVC v142 - VS 2019 C++". 

23) After installation, we will then find MSVC package from ``` VisualStudio2019/.../VC/Tools/ ``` and then copy and paste into ``` ~/unittest/BuildTools/BuildTools/ ```

24) We will also go into ``` C:/Program Files (x86)/MicrosoftSDK/Windows Kits/ ``` and copy & paste "10" into ``` ~/unittest/BuildTools/BuildTools/WindowsSDK/ ``` note we need to ``` mkdir WindowsSDK ``` here as well. **important**: for some Windows system, the right Windows Kits is actually located in ```C:/Windows kits``` and not in the ```Program Files (x86)``` folder. Check if the "10" folder has sufficient contents such as the "bin" folder.

25) Now go to [https://strawberryperl.com](...) and download 5.40.XX version, install it. 

26) Go back to ~/unittest/, we will go into ``` ~/unittest/unit_test_framework/ ``` and copy & paste the Platform folder to ```~/unittest/ ``` and overwrite the existing folder. 
    
27) Go to "Environment Variable" for Windows, and add a new "User Variable", set the Variable Name = PYTHON_HOME, Variable Value = \<where your python is installed> <br>
Also add another "User Variable" for ``` PERL_PATH=C:\Strawberry\perl\bin ``` (wherever you installed Perl) 

28) Now cd into unittest, and run ``` dbuild.cmd ut UnitTest\AgesaModuleUtPkgGn.dsc ```

29) Can always do a clean using ``` dbuild.cmd clean ```





## Framework Setup

30) Add "Results" folder inside ~/unittest/

31) Install Dynamo Rio 10 at https://dynamorio.org/page_releases.html

32) Go to ``` ~/unittest/unit_test_framework/Platform/AmdCommonPkg/Test/UnitTtest/Scripts/ ``` we need to configure the dispatcher here. <br>
``` 
{
  "InPath"                : "C:\\Develop\\unittest\\Build\\AmdCommonPkg\\HostTest\\NOOPT_VS2019\\IA32",
  "OutPath"               : "C:\\Develop\\unittest\\Results",
  "RepoPath"              : "C:\\Develop\\unittest",
  "DynamoRioPath"         : "C:\\DynamoRIO-Windows-10.0.0",
  "TestProfile"           : "C:\\Develop\\unittest\\Platform\\AmdCommonPkg\\Test\\UnitTest\\SoC\\Gn\\GnUtMainProfile.json",
  "PerlPath"              : "C:\\Strawberry\\perl\\bin"
}  
```

33) Now we can ``` cd C:\Develop\unittest\unit_test_framework\Platform\AmdCommonPkg\Test\UnitTest\Scripts\Dispatcher ``` <br>
Then we can run ``` python dispatcher.py dispatcher_configs.json ``` 

34) Now we will work on the coverage script at ~/Scripts/Coverage/ <br>
```   
{
  "InPath"                : "C:\\Develop\\unittest\\Results",
  "OutPath"               : "C:\\Develop\\unittest\\Results\\report",
  "RepoPath"              : "C:\\Develop\\unittest",
  "DynamoRioPath"         : "C:\\DynamoRIO-Windows-10.0.0",
  "SrcFileList"           : "C:\\Develop\\unittest\\Platform\\AmdCommonPkg\\Test\\UnitTest\\SoC\\Gn\\GnSrcFileList.json",
  "PerlPath"              : "C:\\Strawberry\\perl\\bin"
}
```

35) Now we can ``` cd C:\Develop\unittest\unit_test_framework\Platform\AmdCommonPkg\Test\UnitTest\Scripts\Coverage ``` <br>
Then we can run ``` python report.py report_configs.json ```

36) Takeaway here: Dispatcher is for single branch of testing of some module; Coverage is for the summary of all Dispatchers and sums up to a single coverage report.

37) In ~/Coverage/report.py <br>
change line 136 to include double slashes, like this -> ``` files = glob.glob (configs["InPath"]+ "\\**\\*.coverage.info", recursive=True) ``` <br>
change line 218 the same way -> ``` genhtml = os.path.join(configs["DynamoRioPath"], "tools\\bin32\\genhtml") ```

38) Now we can run ``` python report.py report_configs.json ``` (if there was a problem that required this change; if not, then it should have worked in the first place.)





## First Try

39) We should now be ready to dive into unit test. Let's now move on to phase 2.





## Configures Intellisense

The following snippet sets an example of how we should configure the VSCode intellisense for this project. The configure file can be found c_cpp_properties.json in VSCode.

```
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**",
                "C:/Windows Kits/10/include/10.0.19041.0/ucrt",
                "C:/Windows Kits/10/include/10.0.19041.0/shared",
                "C:/Programs/VisualStudio2019/IDE/VC/Tools/MSVC/14.29.30133/include",
                "C:/Windows Kits/10/include/10.0.19041.0/um",
                "C:/Windows Kits/10/include/10.0.19041.0/winrt",
                "C:/Develop/unittest/Platform"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "compilerPath": "C:/Programs/VisualStudio2019/IDE/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "windows-msvc-x64",
            "browse": {
                "path": [
                    "${workspaceFolder}",
                    "C:/Develop/unittest/Platform",
                    "C:/Windows Kits/10/include/10.0.19041.0/ucrt",
                    "C:/Windows Kits/10/include/10.0.19041.0/shared"
                ],
                "limitSymbolsToIncludedHeaders": true
            }
        }
    ],
    "version": 4
}
```