# Phase Two - Intro to Unit Test

## Table of Contents
1. [Session #2](#Session-2)
2. [Session #3](#Session-3)
3. [Session #4](#Session-4)




## Session 2
1. Go here -> ``` cd C:\Develop\unittest\AmdOpenSilPkg\opensil-uefi-interface\UnitTest\Source\Xmp\ ``` 

2. The .inf file -> Every UT has an .inf file; it is an instruction set describing what are needed to build the UT module; it has a RIGID structure.

3. FILE_GUID: It is an unique ID hash. <br>
MODULE_TYPE: Should be the same for all tests. <br>
VERSION_STRING: Should be the same. <br>

4. [SOURCES]: Whatever you need to compile this UT.
    - Minimum 2 source files should be here: function you're trying to test + your .c file which declares the test
    - For example, in the following, the 1st file is the UT, the 2nd and 3rd files are the test targets. <br>
``` 
    [Sources]
        FchAbSetInputBlkUt.c
        ../../../../../../../../AmdOpenSilPkg/opensil-uefi-interface/OpenSIL/xUSL/FCH/Common/MultiFch/MultiFchInit.h
        ../../../../../../../../AmdOpenSilPkg/opensil-uefi-interface/OpenSIL/xUSL/FCH/Common/FchCore/FchAb/FchAb.c 
```

5. [Packages]: .dec decoration files, how EDK defines .inf files. Can look up EDK specs and it describes all the definitions needed for dependencies. (UEFI standards for all devices).

6. [LibraryClasses]: Think of them as #includes; they are libs that we need to bring into UT for some uses. Important part is that they allow us to do fakes, mocks, and stubs. Common ones to include are:
```
[LibraryClasses]
    UtBaseLib               // always include this
    UtIoMockLib             // low level io stuff, "mocks" actual IOs
    UtPciStubLib            
    UtMmioMockLib
    UtxSIMMockLib
    UtSmnAccessStubLib
    UtSilServicesMockLib
```

7. To be careful -> if a function to be tested, calls something outside from it, then there is a good chance there already exists a mock for it.

8. Fakes, Mocks, and Stubs are all inside here ``` C:\Develop\unittest\AmdOpenSilPkg\opensil-uefi-interface\UnitTest\Library ``` <br>
We should get familiar with these tools.

9. Back to the HelloWorld example under ~/XML/ <br>
There is always a .json file -> Keeps track of different branches of test cases because we will have multiple test branches just like a tree, and we need to perform an exhuastive search for all possible test cases. <br>

10. Let's look at this piece of .json file: <br>
```
[
  {
    "Iteration": "Default",
    "WelcomeMessage": "SilHelloWorldUt",
    "WelcomeMessageId": 123
  }
]
``` 
- Note that you can put "input variables" in WelcomeMessageId, and retrieve it inside the test's main().

11. Now go through the documentation: <br>
https://github.com/openSIL/unit_test_framework/blob/genoa_poc/documentation/UnitTestFramework.rst

    - UT source structure: 4 functions -> main, TestPrerequisuite, TestBody, TestCleanUp
    - Test Trio = TestPrerequisuite, TestBody, TestCleanUp

12. Pay attention to API call:
    - ``` Status = UtSilInit(); ``` // initializes OpenSIL API; critical to initializes before doing anything.

13. Pay attention to the TestBody function, it has similar starting codes like TestInit. (Described in recording #2 1:16:00)

14. In the TestBody, the if-else tree is where all the branches of tests reside.

15. We should clean up all inside TestCleanUp.

16. In summary, there are a lot of boiler plate for Logging messages. We can re-use them.

17. Looking at FchInitEnvABUt.c
    - In the test body, there should be "Arrange", "Act", "Assert"
        - Arrange -> declare variables, etc.
        - Act -> calling the unit-under-test function.
        - Assert -> checking output of the function, and see if it works.

18. Study carefully on the comments of ``` FchInitEnvAbUt.c ```

19. Remember if we run the command, then we can see the results both in terminal and in the report -> ``` cd C:\Develop\unittest\unit_test_framework\Platform\AmdCommonPkg\Test\UnitTest\Scripts\Dispatcher ```





## Session 3





## Session 4