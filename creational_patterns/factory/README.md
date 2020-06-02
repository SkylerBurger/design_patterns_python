# Factory Design Patterns

**Main Goal**: Decoupling the code that creates objects from the code that uses objects.

In the Factory Design Pattern your code, often referred to as the client, requests objects without regard for which Class(es) are required to instantiate the desired object. Factories handle the task of instantiating new objects based on dynamic input and modularize object creation from the rest of the code.

The Factory Design Pattern comes in two flavors:
- **Factory Method**: A single function that creates objects
- **Abstract Factory**: A collection of Factories with a common API that can be run through an Abstract Factory to produce logically related objects

## Factory Method

The Factory Method design pattern uses a single function to handle the task of object creation. The function is designed to take in one or more parameters that convey aspects of the requested object. The requested object is then instantiated and returned from the Factory Method. With this design pattern, the client code is not concerned with how the object was built or which Class(es) the object was derived from.

The Factory Method is utilized in Django's Model and Form fields. Whenever you're creating a CharField (or other field) and pass keyword arguments, you're asking a Factory to instantiate the requested field object and return it.

### Advantages

- Decoupling object creation from object usage allows for easy tweaking of Factory Methods and the Class(es) they utilize without affecting the code outside of the Factory Method.
- Since it is the duty of a single function (or commonly a limited number of Factory Methods) to instantiate objects, it becomes a lot easier to keep track of those objects if desired.
- If utilized properly, Factory Methods can help keep your code more performant by enforcing a pattern where new objects are only instantiated when absolutely necessary.

### Feed Parser Example

- **main()**

    Represents the client code. Makes a call to `extract_data_from()` and passes a filepath as its only argument. This filepath leads to an XML or JSON file to be parsed.

- **extract_data_from(filepath)**

    This function is not the actual Factory Method, but a wrapper for it. The purpose of this wrapper function is to call the Factory Method, `data_extraction_factory()` within a try/except block. It uses this try/except block to catch and handle expected errors such as an invalid filepath.

- **data_extraction_factory(filepath)**

    This is the actual Factory Method. It's responsiblity is to determine an appropriate Class, instantiate an object, and return it. In this example, the Factory Method examines the file extension portion of the filepath to determine whether it needs to use the `XMLDataParser` or `JSONDataParser` Class. Once it has determined the appropriate Class, it instantiates an object and returns it to the client code.

- **XMLDataParser and JSONDataParser**

    These are the Classes that the Factory Method can choose from. Each is designed to parse a particular filetype and return an object with a common API. In this example, having a common API means both Classes create objects that have a `.data` property where the parsed data is stored. This allows the client code, `main()` in our example, to interact with the returned object the same way whether it's an instance of `JSONDataParser` or `XMLDataParser`.

#### Summary

In this example, the client makes a call to `extract_data_from()`, passing in the filepath of an XML or JSON file, and receives an object containing the parsed data in a `.data` property. The client can then immediately follow that call with code that interacts with the returned object without concerning itself with:

- Error Handling
- Determining which Class(es) parse which file types
- Instantiating an object

To extend the example to handle additional file types, one would simply need to create a DataParser Class for that file type and add logic to the Factory Method so it can utilize that new Class when appropriate. I'd probably have the Factory Method contain or have access to a dictionary containing file extensions as keys, and their accompanying DataParser Class as the value for easy selection of the appropriate DataParser Class.

## Abstract Factory

The Abstract Factory design pattern utilizes a collection of related Factories to instantiate objects. This pattern encourages a common API between related Factories where method and property names are kept generic and apply to all Factories that could be utilized in the Abstract Factory. This common API allows the Abstract Factory to access methods and properties required to instantiate the requested object, no matter which Factory it is currently utilizing.

Similar to the Factory Method design pattern, at some point we need to determine what the requested object is. Factory Methods determine the requested object (and required Class(es)) internally based on the arguments they receive. Abstract Factories can make this same internal determination but they also have access to an additional approach. An Abstract Factory can have a Factory as a parameter (in the form of a method, function, or object) and simply use that Factory to instantiate the requested object.

It is common to start with the Factory Method design pattern and then adapt your code to the Abstract Factory design pattern if you notice a growing number of related Factory Methods in your project.

The `factory_boy` package for Python uses the Abstract Factory design pattern to make testing of Django models easier by adding test-specific properties to your models during runtime.

### Advantages

- Offers all of the same advantages of the Factory Method approach.
- Behavior of your program can be altered dynamically during runtime by specifying which Factory should be utilized by the Abstract Factory.

### Example

#### Summary