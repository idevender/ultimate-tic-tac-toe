# Assignment 1 , CS2005 F2024

For this assignment, the team will produce a component architecture design for their project.  Each member of the team 
will be assigned a specific python module for which they will have to produce the component design.  All the component 
modules must be represented in the overall component architecture.

The team must produce the following deliverables in order for the team members to score their individual scores:
* Meeting notes of regular team meetings. Members who do not attend and participate will not receive a grade 
for their contribution. There should be a team meeting for every classroom session, but meetings do not have 
to be held during the classroom session. 
* A brief description of the project in a document `docs/arch_project.md`
* A short list of the necessary features the team currently plans for the project to have in the same document. 
These do not have to be a definite commitment, as your plans will change and become more detailed as work progresses.
* A diagram of the overall component architecture of the project in the same document. You are strongly advised to 
adopt the general architecture for web applications discussed in the notes, and refine the provided diagram to reflect
the specific needs of your project.
* Detailed documents for each main architectural component. Assuming the team follows the component 
architecture from the notes, the documents should be:
  1. docs/arch_serverAPI.md
  2. docs/arch_applogic.md
  3. docs/arch_store.md
  4. docs/arch_html.md
  5. docs/arch_user.md

## Individual Submission

* individual grades will be based on the team member's design for the individual component assigned by the team
* The team should assign a specific component (from the provided list of 5 provided above) for each individual member 
to compose.
* each member must document the interface for their assigned component with the following elements:
  * a UML diagram depicting the public interface of their module in the architecture document for their module
  * any other discussion needed to understand their module interface can be included in the architecture document for 
the module  
  * a python code module with a stub implementation including stub methods for the interface of their module
  * docstrings for the public classes, attributes and methods of their module
  * at least two unit tests for each kind of public method invocation needed for the project

* Note that the interface for the server module is a set of HTTP/API calls, where the other modules interface consist 
of python methods and structures.

HINT: In designing your component interface:

* You do not have to know exactly how everything will be coded, but you need to imagine how each app feature will be 
implemented in terms of the interface calls and parameters that will be used. You can "mentally trace" each HTTP service 
call. If you think of each HTTP request that 
arrives, and how it will be serviced, and how the program control will flow from one module into the next, 
it will help to decide what interface methods are needed to access each module.
* Requests will arrive at the server module, so it may help to look at the "usual service pattern" for the service 
module provided in the notes to start this activity.
* Implicit in the design of the methods is the design of the classes and other data structures to be stored, retrieved 
and manipulated.
* You need to discuss and review your interface designs and the data structures with teammates, to make sure that the 
design are consistent, and to make sure your component design is providing others with the methods and capabilities 
they need. You need team meetings ot do this.