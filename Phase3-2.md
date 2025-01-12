# Phase Three - UT Development

## Table of Contents
1. [Commonly Occurred Issues](#Commonly-Occurred-Issues)
2. [UUT Batch 1](#UUT-Batch-1)





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