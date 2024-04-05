# Game Framework Proposal

The Game Framework Proposal outlines the architectural redesign and refactoring of modules within our game development project. This proposal encompasses the essential changes required to enhance the overall functionality, performance, and maintainability of our game development framework.

The proposed framework redesign involves restructuring modules, updating interfaces, and incorporating architectural diagrams to illustrate these changes effectively. By refactoring the existing modules and comparing the redesign to the current architecture, we aim to achieve a more efficient and scalable game development environment.

Additionally, the framework proposal provides clear instructions on how to use the redesigned framework, emphasizing the decoupling of modules to address integration issues and improve overall development workflow. Through this proposal, we aim to streamline the game development process and enhance the user experience of our games.

## Refactoring Modules

The Refactoring Modules section of our project focuses on the detailed analysis and restructuring of specific modules within our game development framework. This involves identifying areas for improvement, updating interfaces, and making architectural changes to enhance the functionality and maintainability of these modules.

Each module will undergo a thorough evaluation to identify any inefficiencies, inconsistencies, or outdated design patterns. The refactoring process aims to address these issues by implementing best practices, optimizing code structures, and improving overall performance.

Furthermore, this section will include architectural diagrams and explanations of interface changes to illustrate the redesigned modules effectively. By refactoring these modules, we aim to enhance code readability, reduce technical debt, and improve the overall quality of our game development framework.

## ServerAPI

- **Description:** This module is constructed useing RESTful API's, enforicing decoupling and stateless methods of handling routing requests for updating the game page, moving data, executing updates, and directing calls to game logic.
- **Refactoring Needed:** The ServerAPI needs minimal refactoring, it only needs to implement a way to add more routes/pages and how to set those up, the primary routes of logging in, registering, showing the dashboard, and starting games can work for any implementation. The only refactoring needed in this module would be the check_game_state route which handles move making and updating the front-end, this would need to be adjusted to handle whatever additonal or different data that needs to be passed to the app logic module, given that the game is on a 2d board no refactoring needed, if the game being constructed is more complex then additonal parameters need to be added.
- **Interface Changes:** The interface of the ServerAPI module should be updated to include clear methods for handling game state updates, user authentication, game creation, and move validation.

### Redesign Comparison

#### Existing Architecture

- **Overview:** The current architecture of the ServerAPI module is designed to handle basic routing functionalities effectively. It includes routes for logging in, registering, displaying the dashboard, and starting games, which can be easily extended to accommodate additional routes/pages as needed. The primary focus of this module is to facilitate communication between the frontend, user manager and the game logic, particularly through the check_game_state route, which manages move making and frontend updates. However, this route may require adjustments to handle diverse data requirements for different game implementations.

#### Proposed Redesign

- **Overview:** The proposed redesign of the ServerAPI module aims to maintain its flexibility while enhancing its scalability and adaptability. The primary focus remains on accommodating additional routes/pages seamlessly. Specifically, the check_game_state route will undergo refinements to handle a variety of data structures and parameters required by different game implementations. This includes potential adjustments for complex game structures beyond the basic 2D board scenario.

#### Framework Usage

- **Decoupling Considerations:** The framework addresses decoupling by defining clear interfaces between modules, allowing for independent development and testing of each component.
- **Clear Usage Instructions:** To use the framework effectively, developers should follow the guidelines for implementing routes, handling game state updates, managing user authentication, and integrating with the game logic module. Detailed instructions and examples can be provided in the framework documentation.


## User Management System

### Description
The User Management System oversees the work for managing user data, including registration, login, authentication, and maintaining user sessions within the game development framework. It serves as a foundational component for user interaction with the game, ensuring secure and efficient management of user accounts and their related information.

### Refactoring Needed
The User module requires refactoring to incorporate modern security practices, improve modularity, and enhance scalability. Specific areas of focus include:
- **Security Enhancements:** Implement advanced security features like password salting alongside hashing, and introduce methods for two-factor authentication (2FA) and email verification to bolster user account security.
- **Database Interaction Abstraction:** Refactor to abstract database interactions, enabling flexibility in database choice and technology. This includes creating a database interface that can be implemented for different database systems (SQL, NoSQL).
- **Modular Integration:** Enhance the module's architecture to allow for easier integration with various parts of a two-player game framework, ensuring that user management can adapt to different game mechanics and rules.

### Interface Changes
The changes will include:
- **User Authentication Expansion:** Broaden the user authentication interface to include OAuth and token-based authentication, facilitating integration with third-party services for a wider range of applications.
- **Database Interface Redesign:** Redesign the database interface to be generic, supporting a variety of backends and allowing for seamless migration or changes in database technology.
- **Support for Multi-Game Use:** Adjust the interface to manage user sessions and data across different two-player games, making it versatile and reusable across projects.

### Architectural Diagrams
Architectural enhancements will be visualized through updated UML diagrams, including:
- **Class Diagrams:** Updated diagrams to showcase the new structure of the User and UserManager classes, emphasizing modular design for easy adaptation to different games.
- **Sequence Diagrams:** Flowcharts detailing the registration, login, and authentication processes, including interactions with external authentication services.
- **Component Diagrams:** Demonstrations of how the User module integrates with external services like OAuth providers, and interfaces with the game logic and database layers.

### Redesign Comparison
#### Existing Architecture
- **Tightly Coupled Design:** Initially, the User module was closely tied to a specific database (shelve) and lacked flexibility in security and database technology, limiting its adaptability to different two-player game types.

### Proposed Redesign
- **Layered, Modular Architecture:** The redesign will introduce a modular structure with clear separation of concerns, integrating advanced security practices and database abstraction to facilitate adaptation across a variety of two-player games.

### Framework Usage for Decoupling and Integration

### Decoupling Considerations
- The redesigned module emphasizes decoupling from specific implementations, particularly in database and authentication technologies, via abstract interfaces. This ensures the User module can be integrated into any two-player game framework with minimal dependency issues.

### Clear Usage Instructions
- Detailed documentation will outline the process for integrating the User module into different two-player game projects, configuring database connections, and implementing security mechanisms. This will include guidelines for extending the module to accommodate various game types and user management requirements.

# Frontend

**Description:** This module handles front end operations for a 2-player game, including rendering game boards, managing player interactions, and displaying online player lists.

**Refactoring Needed:** Refactor the module to make it more generic, abstracting game-specific details to make it suitable for any 2-player game, not just tic-tac-toe.

**Interface Changes:** Update method names and parameters to reflect a more generic interface that can be used for various 2-player games.

**Architectural Diagrams:** https://github.com/CS2005W24/term-project-teamg/blob/master/docs/diagrams/html_arch_uml_diagram.png

### Existing Architecture

**Overview:** The current architecture of the frontend module is tightly coupled with the specific requirements of a tic-tac-toe game, handling tasks such as rendering the game board and processing player moves.

### Proposed Redesign

**Overview:** The proposed redesign aims to decouple the module from game-specific details, providing a more generic interface for rendering game boards, managing player interactions, and displaying online players. This includes abstracting game-specific logic into separate components to facilitate integration with different 2-player games.

### Framework Usage

**Decoupling Considerations:** Refactor the module to abstract game-specific logic into separate components, allowing for easier integration with different 2-player games.

**Clear Usage Instructions:** Provide clear documentation and usage examples for developers to easily integrate this frontend module into their 2-player games. Detailed instructions and examples can be provided in the framework documentation.

## Application Logic

- **Description:** Use store and API to manage tic-tac-toe games. Manages tic-tac-toe logic.
- **Refactoring Needed:** Decoupling to reduce dependencies such as the board being displayed using specific coordinates in the frontend. 
                            Create a more abstract algorithm where the object is able to manage itself.
- **Interface Changes:** Allow the gameboard display to be set in applogic rather than coordinates in frontend.
- **Architectural Diagrams:** An object oriented approach rather with self-reliance rather than relying on the database and server.

### Redesign Comparison

#### Existing Architecture

- **Overview:** Refer to arch_applogic.md
- **Module Diagrams:** Refer to app_logic_uml.png

#### Proposed Redesign

- **Overview:** Create a tic-tac-toe game object that is self sufficient and can interact with the frontend's display itself within the game logic.

#### Framework Usage

- **Decoupling Considerations:** Applogic already interacts with database as a framework. The frontend has to handle some logic for the display, it would be best to handle that logic within applogic.py.
- **Clear Usage Instructions:** ServerAPI calls the SuperTicTacToe class and forwards the information to the frontend frontend.

## Database

- **Description:** This module currently handles the persistent storage of game states and user information using a shelve database. It allows for the creation, modification, loading, and removal of both game states and user data.
- **Refactoring Needed:** To convert this module into a framework, the main changes required would involve abstracting the database handling to support different database backends (not just shelve). Additionally, the framework should allow for customization of data schema, error handling, and potentially support for asynchronous operations.
- **Interface Changes:** The interface would need to be redesigned to be more generic, allowing users of the framework to easily switch between different database implementations and customize data storage formats.

### Redesign Comparison

#### Existing Architecture

- **Overview:** The current architecture tightly couples the application with shelve for data storage. Modules directly interact with shelve for storing and retrieving data.

#### Proposed Redesign

- **Overview:** The proposed redesign aims to decouple the application from specific database implementations. It introduces abstraction layers for database interactions, allowing for easier integration of different databases.

#### Framework Usage

- **Decoupling Considerations:** The framework provides interfaces for database interactions, allowing users to switch between different databases without modifying application code significantly.
- **Clear Usage Instructions:** To use the framework to manage game states and user information effectively, developers should defer to the python shelve documentation. Otherwise, there is documentation in ```arch_store.py``` which outlines the methods and their use.