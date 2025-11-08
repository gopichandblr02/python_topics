Basics
### Memory management in Python

Python employs an automatic memory management system, relieving developers from manual memory allocation and deallocation.
This system primarily relies on two mechanisms: reference counting and garbage collection.
1. Reference Counting:
Every object in Python maintains a reference count, which tracks the number of references pointing to it.
When an object's reference count drops to zero, it signifies that no part of the program is currently using or referencing that object.
At this point, Python automatically deallocates the memory occupied by the object, making it available for reuse.
The sys.getrefcount() function can be used to inspect an object's reference count.
2. Garbage Collection:
While reference counting effectively handles most memory deallocation, it cannot resolve circular references (where two 
or more objects refer to each other, preventing their reference counts from reaching zero).
To address this, Python's garbage collector periodically runs, employing a mark-and-sweep algorithm.
This algorithm identifies objects that are no longer accessible from the program, even if their reference counts are 
not zero due to circular references.
Once identified, these unreachable objects are deallocated, preventing memory leaks.
The gc module in Python provides functionalities to interact with the garbage collector, such as manually triggering collection or disabling it.
Memory Allocation:
Python allocates memory for objects in the heap.
For small objects (typically less than 512 bytes), CPython uses a specialized small object allocator that groups memory 
into structures like blocks, pools, and arenas to optimize allocation and reduce overhead.
Larger objects are generally allocated directly using the standard C allocator.
When functions are called, local variables and function call information are stored in the stack memory, which is 
automatically freed upon function completion.
In essence, Python's memory management system automates the complexities of memory handling, aiming for efficient 
memory utilization and preventing common memory-related issues like leaks.
