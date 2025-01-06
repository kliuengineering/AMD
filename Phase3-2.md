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

### Timeline: December 16, 2024 -> TBD

1. The following UTs will be completed:
    - DfHasFch
    - DfHasSmu
    - DfGetSystemInfo

Commonly occuring 