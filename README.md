Learning Objectives:
Implement Multi-Agent Search Algorithms: You will implement different strategies including minimax, alpha-beta pruning, and expectimax to optimize Pacman's decisions against adversarial ghost agents.
Evaluation Function Design: You will design a custom evaluation function to improve the reflex agent's performance in real-time.
Understand Game Theory Concepts: You will learn about adversarial search, probabilistic models, and optimization in a multi-agent environment.

Files to Edit:

multiAgents.py: Contains the code for different search agents including reflex, minimax, alpha-beta, and expectimax agents.
Files to Review:

pacman.py: The core logic for running the Pacman game.
game.py: Provides support for different types like GameState, Agent, and Direction.
util.py: Contains useful data structures for search algorithms.
Supporting Files (No Need to Edit):

Graphics files (for display), ghost agents, keyboard controls, autograder scripts, and layout files.
Key Tasks:
Reflex Agent: Improve the reflex agent's decision-making to clear specific layouts efficiently. This involves designing an evaluation function that considers food and ghost proximity.

Minimax Agent: Implement the MinimaxAgent that simulates adversarial search over multiple depths, considering the ghosts as adversaries. Each ghost acts as a "minimizer" while Pacman is the "maximizer."

Alpha-Beta Pruning: Enhance the minimax agent by integrating alpha-beta pruning to optimize the search process. This reduces the number of game states evaluated without affecting the final result.

Expectimax Agent: Implement the ExpectimaxAgent to handle scenarios where ghosts are not perfectly rational. Instead of assuming optimal adversarial behavior, expectimax uses probabilistic modeling to anticipate suboptimal moves.

Better Evaluation Function: Design a robust evaluation function for deeper searches that balances efficiency and performance. The goal is to achieve higher scores in larger layouts while maintaining a reasonable computation time.

Evaluation & Testing:
Grading: Your submission will be graded based on the accuracy of the implementation, the performance of your agents, and the design of your evaluation function. Pacman's ability to clear certain layouts and achieve specific score thresholds will contribute to the final score.

Autograder: The project includes an autograder to test your agents' correctness. You can run the autograder locally by executing:
python3 autograder.py

Performance Metrics: The autograder will evaluate your agents based on criteria like the number of wins, average score, and the time taken for computation. Be mindful of the constraints on the number of state evaluations to avoid penalties.





