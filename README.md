# PythonMinMaxStack
A Stack DS for HackerRank challenges which can retrieve the min or max values in O(1) time

## Notes
-This code repeats the code from my Python Stack: https://github.com/asawitt/PythonStack because HackerRank only allows access to modules within the Python Standard Library. If you're using this code elsewhere, and especially if you're also using my PythonStack, you should consider deleting the Stack portion in MinMaxStack.py and importing it as a module in order to avoid unnecessary duplication. 

## Installation
-Fastest would be to copy-paste the contents of MinMaxStack.py into your code 

-Or you could download MinMaxStack.py and throw it in your project directory. Use "from DisjointSet import *" to use it in your code

-You could clone https://github.com/asawitt/PythonMinMaxStack/ , move MinMaxStack.py to your project directory, then use the above import statement if you really want to. Don't. 

## Usage
### To Create a min stack (or max stack) pass in the desired function:
min_stack = MinMaxStack(min) 

max_stack = MinMaxStack(max)
### Push O(1):
min_stack.push(4)
### Peek O(1):
-Returns the value at the top of the stack:

min_stack.peek() #returns 4

### Pop O(1):
-Remove the item at the front of the Stack and return the value

min_stack.pop()

### Display the Stacks
- MinMaxStack uses two stacks, one for the aggregation and one for the values

min_stack.display()

### Getting the size O(1)
-Returns the number of elements in the Stack

min_stack.getSize()

### Check if the Stack is empty O(1)
-Returns True if the Stack is empty, False otherwise

min_stack.isEmpty()

### Get the current min (or max) in the Stack O(1):
min_stack.query() #returns the min value in the stack (or max, depending on the function passed in on initialization)

## License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

