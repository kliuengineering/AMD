import os

void deployment API()
{
    ImplementationParser parser = new ImplementationParser(...);

    parser.run();
}

void debug API()
{
    DebugAPI parser = new DebugAPI(...);

    parser.run();
}

void main(argv[], argc)
{
    if argv[2] ==  deployment:
        implementation = 1;
    else if argv[2] == debug
        implementation = 2;

    switch(implementation)
    {
        case 1:
            deploymentAPI();
        
        case 2:
            
    }
}