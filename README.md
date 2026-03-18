This repository is where I put code best practices into action. The goal is to practice writing cleaner, more cohesive, and loosely coupled code.

Each file in this project focuses on refactoring a common problem by applying one or more specific best practice rules. Below is a description of what was explored in each of them.


### **Against FLOAT (`FLOAT.py`)**
* Primitive floating-point types (`float`, `double`) suffer from precision issues, which can cause severe bugs, especially when dealing with money.
* I practiced replacing floats to store monetary values as integers/cents.

### **Law of Demeter (`LeiDeDemeter.py`)**
* Coupling problem caused by objects knowing too much about the internal structure of other objects.
* The code was refactored so that objects only communicate with their immediate friends, delegating behaviors instead of exposing internal structures.

### **Object Calisthenics - Rules 1 & 2 (`ObjectCalRule1&2.py`)**
* Use of only one level of indentation per method by extracting methods to improve readability and focus on single responsibility.
* Use of *Early Return* to eliminate complex and nested conditional flows.

### **Object Calisthenics - Rule 3 (`ObjectCalRule3.py`)**
* Instead of passing a simple `string` or `int` that has no domain meaning, I created specific classes like `Name` and `Age` to ensure validation and encapsulate behavior right at the source.

### **Object Calisthenics - Rules 8 & 9 (`ObjectCalRule8&9.py`)**
* Promotion of high cohesion by dismantling *God classes* into smaller, more focused objects.
* The focus shifted to asking the object to do something with its own data, rather than extracting its data to manipulate it elsewhere.

### **YAGNI, KISS, and SOLID (`YAGNI.py`)**
* **YAGNI:** Removal of speculative code and features built just in case we need them in the future. Focus on the current requirement.
* **KISS:** Refactoring overly complex solutions into simpler, more straightforward, and easier-to-understand approaches.
* **SOLID:** Application of principles like Single Responsibility (SRP) and Dependency Inversion (DIP) to make the architecture more flexible.