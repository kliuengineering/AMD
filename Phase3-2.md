# Phase Three - UT Development

## Table of Contents
1. [Commonly Occurred Issues](#Commonly-Occurred-Issues)
2. [UUT Batch 1](#UUT-Batch-1)
3. [UUT Batch 2](#UUT-Batch-2)
4. [UUT Batch 3](#UUT-Batch-3)
4. [UUT Batch 4](#UUT-Batch-4)





## Commonly Occurred Issues
1. When running dbiuld.cmd, if we see errors like "... incorrect indirection... ", then check codes for passed-by-pointers, for example, <br>
``` foo( CUSTOM_TYPE *Parameter ) {...} ``` <br>
when calling this function, we only do the following: <br>
``` foo( Parameter ); ``` <br>
but not <br>
``` foo( &Parameter ); ``` <br>

## UUT-Batch-1

### Timeline: December 16, 2024 -> January 12, 2025

1. The following UTs will be completed:
    - DfHasFch
    - DfHasSmu
    - DfGetSystemInfo

2. In ```DfHasFch``` UUT, there are function calls which couple to the functions defined in the same file - BaseFabricTopologyCmn.c <br>
To resolve this issue, we cannot mock it conventionally because the compiler will not be able to distinguish the mocked version and the actual definition <br>
So, we need to write targeted fakes to solve this problem.

3. Updated DfHasFch and DfhasSmu are in the codes folder.

4. Pay attention to how to write Fakes as well how to navigate through the libraries to retrieve:
    - what constants and declarations are need for Faking the sub-function calls;
    - which data structures can be stubbed instead.





## UUT-Batch-2

### Timeline: January 12, 2025 -> January 23, 2025

1. The following .c file is the target goal for completion: <br>
``` ~\AmdOpenSilPkg\opensil-uefi-interface\OpenSIL\xUSL\CCX\Zen4\Zen4DownCoreInit.c ```

2. The UUT is complete and uploaded at ```codes/``` dicrectory.

3. Pay attention to the use of CMocka in writing the mock call to a static function (can be found easily inside ```Zen4DownCoreInit.c```).





## UUT-Batch-3

### Timeline: January 23, 2025 -> February 21, 2025

1. The goal of this sprint is to tackle the following initialization file: <br>
``` ~\AmdOpenSilPkg\opensil-uefi-interface\OpenSIL\xUSL\RcMgr\FabricRcInit.c ```

2. We shall pay attention to the usage of IP2IP API with transfer tables. 

3. We may need to create a number of stubs, but mocks may not be needed as the logics do not require a control of rc.

4. The completed UTs can be found on the obsoleted openSIL code base on Github.





## UUT-Batch-4

### Timeline: February 22, 2025 -> March 7, 2025

1. The goal of this sprint is to migrate to the Phoenix code base. 

2. UTs are expected to be written based on the new code base.