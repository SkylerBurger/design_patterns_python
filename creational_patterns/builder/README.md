# Builder Design Pattern

**Main Goal**: Separates the construction of a complex object from its representation- the same construction process can yield several different representations.

## Components of the Pattern

The Builder Design Pattern has two main componetnts that work together to build objects: the director and the builder.

### The Director

The Director object is the interface that the client works with to request various representations (instantiated objects). When the client requests a representation, the Director works with one of usually many potential Builder instances to fulfill the request. When the Director works with the Builder, it calls a set of methods on the Builder that builds up the representation one layer at a time. These methods are the same no matter which Builder instance the Director is working with.

General Responsibilities:

- Take in any required arguments from the client.
- Receive, or instantiate, an instance of the appropriate Builder class.
- Call a set of methods on the Builder instance. This set of calls is sometimes referred to as the 'steps' to build the requested representation as is the main difference between the Builder and Factory Design Patterns.
- Store or return the requested representation (the new and complete instantiated object).

### The Builder

The Builder component is a collection of Builder classes that can create a wide array of representations (objects). Each Builder class has an identical interface of methods so the Director can call the same set of methods on a Builder instance regardless of which Builder class the instance was derived from.

Each method of a Builder instance is a 'step' in building the representation requested by the client. This is one of the main differences between the Factory and Builder Patterns- the Factory builds an object in one step while a Builder allows for creation of more complex objects by building it over multiple steps, one step at a time.

"Building it" can sound a bit vague when it comes to instantiating an object but mainly refers to calculating and attaching properties to the representation. Sometimes a certain property needs to be resolved before the next property can be calculated and this is the beauty of the 'steps' the Builder contains. The Builder also has the great honor of being the only component of the Builder Pattern that directly instantiates the requested representation- usually a class that the Builder creates an instance of and perform the steps on.

General Responsibilities:

- Methods match a standard (method names and behaviors) for interacting with the Director
- Direct instantiation of the requested representation
- Performing the 'steps' required to build up the representation one layer at a time

