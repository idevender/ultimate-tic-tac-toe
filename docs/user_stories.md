# User Stories

## Story 1: First time player

### Written by: Jager Cooper

**As a** newcomer to the world of Tic Tac Toe and Ultimate Tic Tac Toe,  
**I want** a clear tutorial or rulebook integrated into the game,  
**So that** I can understand the game's objective and mechanics effortlessly.

### Description

Joe is a first-time user who has never encountered Tic Tac Toe or Ultimate Tic Tac Toe. Intrigued by a friend's recommendation, Joe visits the game website, creates an account, and eagerly logs in to explore this new gaming experience. Upon entering the game lobby, Joe selects the first available opponent and starts a game. However, Joe quickly realizes that he lacks a fundamental understanding of the game's objective and rules. Frustrated by the lack of guidance, Joe exits the game without completing it.

#### Feature Suggestion

Incorporate an interactive tutorial or rulebook directly within the game interface to assist new players like Joe in learning the game's mechanics and objectives. The tutorial should provide step-by-step instructions, visual aids, and explanations of key concepts to ensure a smooth onboarding experience for beginners.

#### Design Suggestions

- Include tooltips or pop-up hints during gameplay to remind players of the current objective or suggest optimal moves.
- Implement a practice mode where players can play against AI opponents or explore different strategies without the pressure of a competitive match.
  
### Acceptance Criteria

1. A totally new player to the games of tic tac toe and/or ultimate tic tac toe, should have a clear understanding of how to play the game.
2. The tutorial should be accessible from the user's dashboard or main game page with clear navigation instructions.
3. The tutorial content should cover basic gameplay mechanics, such as how to place marks on the board, win conditions, and turn-taking rules.
4. New players should be able to refer back to the tutorial at any point during their gameplay session for quick reminders or clarifications.

### Tasks

- **App Logic Module:** define a clear set of rules, regulations and objectives in a tutorial text to be stored in a string/list to send to Server on request.
- **Server API Module:** request the tutorial from app logic and pass to the front-end to be displayed as an element in the UI.
- **Front-End Module:** Create a UI element that takes a tutorial as a parameter and displays it on the user's dashboard and/or on the main game page during an active game.

### Additional Information

- **Dependency:** Ensure that the tutorial content is written in a clear and understandable manner, catering to users with no prior knowledge of tic tac toe or ultimate tic tac toe.
- **Constraints:** The tutorial should be concise yet comprehensive, covering all essential rules, regulations, and objectives of both tic tac toe and ultimate tic tac toe games.
- **Reference:** Refer to existing game rulebooks or tutorials for inspiration and accuracy in content creation.
- **User Feedback:** Gather feedback from new players to assess the effectiveness and clarity of the tutorial in helping them understand the game objectives.
- **Iterative Improvement:** Plan for iterative updates to the tutorial based on user feedback and any future rule changes or additions to the games.
- **Localization:** Consider the possibility of translating the tutorial into multiple languages to cater to a wider audience of new players.
- **Accessibility:** Ensure that the tutorial is accessible to all users, including those with disabilities, by following accessibility guidelines for UI elements and content presentation.

## Story 2: Improving User Connectivity through Profiles and Friend Lists

### Written by: Devender Singh

**As an** enthusiastic player of Ultimate Tic Tac Toe,     
**I want** to delve into fellow gamers' profiles and befriend them,   
**So that** I can easily connect with friends, track their game progress, and  lay down challenges for thrilling encounters.

### Description

Raj is an ardent Ultimate Tic Tac Toe fanatic and the game’s strategic depth, as well as camaraderie are his driving forces. Raj has faced intense challenges in the game and made new friends who play this game with him. One of the most unforgettable events was a recent match against Avatar; it was more than just a game that he would like to extend beyond one match. Raj dreams of staying in touch with Avatar even after they finish playing games, celebrating respective gaming milestones, and engaging them into friendly rematches.

Nevertheless, it is apparent to him that the current game infrastructure lacks an immediate means for players to stay connected after matches. There is no way through which he could directly interact with Avatar once the game ends, therefore forcing Raj to write down their usernames and keep searching for them in the lobby while hoping that they would meet again someday. This process is inconvenient and completely goes against what he likes about online gaming – seamless feeling and being lost in it simply because he feels cut off from the community he so desires to belong to.

Raj’s level of involvement is hampered by a lack of efficient ways to connect and maintain relationships among players in the ecosystem while ignoring the chance to make the game’s social environment more robust. In a community-driven game, the aspect of reaching out, talking and starting games with friends easily isn’t just an extra feature; it is what makes up for a lively, interactive and coherent player collective. Raj suddenly realizes that it would be possible to enhance her gaming experience from this realization, by having a seamless integration between playing together and staying connected thus turning momentary acquaintanceships into lasting friendships and rivalries.

#### Feature Suggestion

Integrate personalized player profiles within the game interface, showcasing individual achievements, a "Send Friend Request" button to foster connections, and an option for players to initiate chat conversations. Simultaneously, embed a friend list feature on the main dashboard to display friends' interests, recent achievements, his status and facilitate direct game challenges. This setup aims to simplify staying connected, celebrating progress, chatting and initiating matches, enhancing the social interaction and community aspect of the game.

#### Design Suggestions

- **Include Direct Messaging:** Within the player profiles, to enhance communication and community engagement among users.
- **Implement Friend List Integration:s:** Embed a friend list section or tab within the main dashboard, displaying friends' current availability alongside a quick challenge button.
- **Include Notification System:** For friend requests and messages, enhancing user awareness and engagement with the community.
- **Implement a Chat System:** Within the game lobby and friend list, allowing users to discuss strategies or simply chat, enhancing the social experience without interrupting gameplay.

### Acceptance Criteria
- Players must be able to view any player's profile and send friend requests.
- Accepting a friend request should mutually add players to each other's friend lists.
- The friend list must reveal each friend's current online status, with an additional chat feature for direct messaging.
- Friends' profiles should be accessible through the friend list, detailing their latest achievements, game stats, and offer a direct messaging option.
- The system must support notifications for friend requests, messages, and game challenges to enhance user interaction and engagement.

### Tasks
- **Backend Framework:** Construct backend infrastructure for managing user profiles, friend connections, interaction requests, and real-time notifications.
- **UI/UX Development:** Design and implement the interface for user profiles, friend interactions, chat functionalities, and notifications.
- **Integration and Testing:** Ensure the seamless integration of these features with existing game mechanics, like matchmaking and authentication, utilizing the current online player list feature for displaying friends' online status.
- **Chat System Implementation:** Develop a chat system that allows players to communicate directly within the game interface, enhancing the community experience.

### Additional Information
- **Dependencies:** Relies on the established user authentication system and matchmaking algorithms. The implementation of chat and friend interactions will leverage the existing infrastructure for displaying online players.
- **Constraints:** Maintain adjustable privacy controls, allowing users to decide the visibility of their profile details and who can message them.
- **Global Reach and Inclusivity:** Designs should consider internationalization and adhere to inclusivity standards, aiming to serve a diverse and global player base. The introduction of chat and other social features should be accessible to all users, enhancing the overall community feel of the game.
- **Scalability:** The infrastructure for friend interactions and chat must be scalable to support a growing user base. As the game's popularity increases, the system should efficiently handle an expanding number of simultaneous friendships and messages without degradation in performance.
- **Data Privacy and Security:** Implement stringent data protection measures to secure personal and communication data. 
- **User Experience and Customization:** Offer customization options for users to personalize their profiles and chat experiences. This could include avatars, profile themes, and chat color schemes, allowing for a more personalized interaction space within the game environment.
- **Moderation and Reporting:** Establish a robust moderation system to monitor and manage interactions within the community. Users should have the ability to report inappropriate behavior or content, ensuring a safe and respectful environment for all players.
- **Performance Optimization:** Ensure that the introduction of new social features does not adversely affect the game's overall performance. Efficient coding practices and server management should be prioritized to maintain optimal load times and gameplay smoothness.
- **Reference and Best Practices:** Study existing social gaming platforms and community-driven games for insights into engaging social feature implementation. Adopting industry best practices can guide the development process and help avoid common pitfalls.
- **User Feedback Loop:** Create channels for collecting user feedback specifically regarding the new social features. Regularly review and analyze this feedback to understand user needs, preferences, and pain points, facilitating continuous improvement of the friend system and chat functionality.

## Story 3: [Title of User Story]

### Written by: [Your Name]

**As a** [type of user or persona],  
**I want** [a goal or desired functionality],  
**So that** [reason or benefit].

### Description

[Provide a brief description of the user story, including any context or background information that helps understand the user's needs.

[User's name or role] is a [description of the user's background or role] who [describe the user's action or interaction with the product].

When [describe the trigger or event that initiates the user's action], the system responds with [describe the system's response, such as feedback, output, or outcome].

This results in [describe the issue, problem, or impact faced by the user as a result of the system's response].

As a result, [user's name or role] is uncertain about [specific uncertainty or question related to the issue].

The desired outcome is [describe the user's expectation, goal, or desired resolution].

]

#### Feature Suggestion

Incorporate an [interactive element or feature] directly within the [system or platform] to assist [users or specific user group] in [specific action or objective]. The [element or feature] should provide [description of functionality or benefits] to ensure [desired outcome or improvement].

#### Design Suggestions

- Include [additional feature or functionality] during [specific user interaction or scenario] to enhance [user experience or outcome].
- Implement a [new system component or tool] where users can [specific action or benefit] without [potential issue or limitation].

### Acceptance Criteria

1. [Specific condition or action that must be met for the user story to be considered complete]
2. [Another condition or action]
3. [Additional conditions as needed]

### Tasks

- [Task 1: Description of task]
- [Task 2: Description of task]
- [Additional tasks as needed]

### Additional Information

[Include any additional information, such as dependencies, constraints, or references to related user stories or requirements.]

## Story 4: [Title of User Story]

### Written by: [Your Name]

**As a** [type of user or persona],  
**I want** [a goal or desired functionality],  
**So that** [reason or benefit].

### Description

[Provide a brief description of the user story, including any context or background information that helps understand the user's needs.

[User's name or role] is a [description of the user's background or role] who [describe the user's action or interaction with the product].

When [describe the trigger or event that initiates the user's action], the system responds with [describe the system's response, such as feedback, output, or outcome].

This results in [describe the issue, problem, or impact faced by the user as a result of the system's response].

As a result, [user's name or role] is uncertain about [specific uncertainty or question related to the issue].

The desired outcome is [describe the user's expectation, goal, or desired resolution].

]

#### Feature Suggestion

Incorporate an [interactive element or feature] directly within the [system or platform] to assist [users or specific user group] in [specific action or objective]. The [element or feature] should provide [description of functionality or benefits] to ensure [desired outcome or improvement].

#### Design Suggestions

- Include [additional feature or functionality] during [specific user interaction or scenario] to enhance [user experience or outcome].
- Implement a [new system component or tool] where users can [specific action or benefit] without [potential issue or limitation].

### Acceptance Criteria

1. [Specific condition or action that must be met for the user story to be considered complete]
2. [Another condition or action]
3. [Additional conditions as needed]

### Tasks

- [Task 1: Description of task]
- [Task 2: Description of task]
- [Additional tasks as needed]

### Additional Information

[Include any additional information, such as dependencies, constraints, or references to related user stories or requirements.]

## Story 5: [Title of User Story]

### Written by: [Your Name]

**As a** [type of user or persona],  
**I want** [a goal or desired functionality],  
**So that** [reason or benefit].

### Description

[Provide a brief description of the user story, including any context or background information that helps understand the user's needs.

[User's name or role] is a [description of the user's background or role] who [describe the user's action or interaction with the product].

When [describe the trigger or event that initiates the user's action], the system responds with [describe the system's response, such as feedback, output, or outcome].

This results in [describe the issue, problem, or impact faced by the user as a result of the system's response].

As a result, [user's name or role] is uncertain about [specific uncertainty or question related to the issue].

The desired outcome is [describe the user's expectation, goal, or desired resolution].

]

#### Feature Suggestion

Incorporate an [interactive element or feature] directly within the [system or platform] to assist [users or specific user group] in [specific action or objective]. The [element or feature] should provide [description of functionality or benefits] to ensure [desired outcome or improvement].

#### Design Suggestions

- Include [additional feature or functionality] during [specific user interaction or scenario] to enhance [user experience or outcome].
- Implement a [new system component or tool] where users can [specific action or benefit] without [potential issue or limitation].

### Acceptance Criteria

1. [Specific condition or action that must be met for the user story to be considered complete]
2. [Another condition or action]
3. [Additional conditions as needed]

### Tasks

- [Task 1: Description of task]
- [Task 2: Description of task]
- [Additional tasks as needed]

### Additional Information

[Include any additional information, such as dependencies, constraints, or references to related user stories or requirements.]