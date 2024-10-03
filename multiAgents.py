# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
        # Start Code Addition for q1 ***********************************************************************
        # Eat food when ghost is not near
        newFood = successorGameState.getFood().asList()
        minFoodist = float("inf")
        for food in newFood:
            minFoodist = min(minFoodist, manhattanDistance(newPos, food))

        # Don't go towards the ghost if you are too close
        for ghost in successorGameState.getGhostPositions():
            if (manhattanDistance(newPos, ghost) < 2):
                return -float('inf')
        #return the reciprocol as the score
        return successorGameState.getScore() + 1.0/minFoodist
        # end code addition for q1 *******************************************************************
        
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """
    
    
    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        "*************************Q2 CODE STARTS HERE ****************************"
        
        def minimax(self, gameState, currentDepth, agentIndex):
            numAgents = gameState.getNumAgents()
            
            
            if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
                return self.evaluationFunction(gameState)
            
            if agentIndex == 0: #Max Pacman
                
                LegalActionsList = gameState.getLegalActions(agentIndex)
                
                ActionsScores = [
                    minimax(self, gameState.generateSuccessor(agentIndex, legalAction), currentDepth, 1)
                    for legalAction in LegalActionsList
                ]
                
                maxScore = max(ActionsScores)
                
                return maxScore
         
            
            if agentIndex != 0: #Min ghosts
                LegalActionsList = gameState.getLegalActions(agentIndex)
                
                if((agentIndex + 1) < numAgents):
                    i = agentIndex + 1
                
                else:
                    currentDepth += 1
                    i = 0
                
                ActionsScores = [
                    minimax(self, gameState.generateSuccessor(agentIndex, legalAction), currentDepth, i)
                    for legalAction in LegalActionsList
                ]
                
                minScore = min(ActionsScores)
                
                return minScore
        
        
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        
        
        # Choose one of the best actions
        
        scores = [
            minimax(self, gameState.generateSuccessor(0, lmove), 0, 1)
            for lmove in legalMoves
        ]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        
        
        return legalMoves[chosenIndex]
        
        
        util.raiseNotDefined()
        

                
    "*************************Q2 CODE ENDS HERE ******************************"    
        
       
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def AB(gameState,agent,depth,a,b):
            result = []
            if not gameState.getLegalActions(agent):
                return self.evaluationFunction(gameState),0
           
            if depth == self.depth or gameState.isLose() or gameState.isWin():
                return self.evaluationFunction(gameState),0

            if agent == gameState.getNumAgents() - 1:
                depth += 1

            

           
            if agent == gameState.getNumAgents() - 1:
                nextAgent = self.index

            
            else:
                nextAgent = agent + 1

            
            for action in gameState.getLegalActions(agent):
                if not result: # First move
                    nextValue = AB(gameState.generateSuccessor(agent,action),nextAgent,depth,a,b)

                    
                    result.append(nextValue[0])
                    result.append(action)

                   
                    if agent == self.index:
                        a = max(result[0],a)
                    else:
                        b = min(result[0],b)
                else:
                  
                    if result[0] > b and agent == self.index:
                        return result

                    if result[0] < a and agent != self.index:
                        return result

                    previousValue = result[0] 
                    nextValue = AB(gameState.generateSuccessor(agent,action),nextAgent,depth,a,b)

                    
                    if agent == self.index:
                        if nextValue[0] > previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
                            
                            a = max(result[0],a)

                    
                    else:
                        if nextValue[0] < previousValue:
                            result[0] = nextValue[0]
                            result[1] = action
                            
                            b = min(result[0],b)
            return result

                                 
        return AB(gameState,self.index,0,-float("inf"),float("inf"))[1]
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    
     #***************************Q4 Code Begins Here******************
    def expectimax(self, agentIndex, currentDepth, gameState):
        if gameState.isWin() or gameState.isLose() or currentDepth == self.depth:
            return self.evaluationFunction(gameState)
        
        if agent != 0: #max for Pac
            return max() #recursive expectimax call required
        
        else: #min for baddies
            nextAgent= agent + 1 #moves to the next characters turn
            if gameState.getNumAgents() == nextAgent:
                nextAgent = 0;
            if nextAgent == 0: 
                depth += 1 #Depth gets higher once everyones moved one time
            #return () something here. recursive call to expetimax required

    #***************************Q4 Code Ends Here*********************
    

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        
        def expectimax(agentIndex, currentDepth, gameState):

            #returns evaluation function if Win/Loss conditions are met or if maximum depth is reached
            if currentDepth == self.depth or gameState.isWin() or gameState.isLose():  
                return self.evaluationFunction(gameState)
            
            if agentIndex != 0:  # Execute expectimax action for ghost

                nextAgent = agentIndex + 1  # Increment to next agent and update depth

                if gameState.getNumAgents() == nextAgent:
                    nextAgent = 0
                if nextAgent == 0:
                    currentDepth += 1

                return sum(expectimax(nextAgent, currentDepth, gameState.generateSuccessor(agentIndex, newState)) for newState in gameState.getLegalActions(agentIndex)) / float(len(gameState.getLegalActions(agentIndex)))
            
            else: #perform maximising action on pacman
                return max(expectimax(1, currentDepth, gameState.generateSuccessor(agentIndex, newState)) for newState in gameState.getLegalActions(agentIndex))
            
            #Maximising action
        maxUtility = float("-inf")
        move = Directions.WEST
        for agentState in gameState.getLegalActions(0):
            utility = expectimax(1, 0, gameState.generateSuccessor(0, agentState))
            if utility > maxUtility or maxUtility == float("-inf"):
                maxUtility = utility
                move = agentState

        return move
        
        
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    totalScore = 0
 
    #Step 0 - Reward for winning, negative for losing
    if(currentGameState.isWin()) : 
        totalScore = 1000
    if(currentGameState.isLose()) :
        totalScore = -1000
        
    #Step 1 - Reward for eating food and getting closer to food
    newFood = currentGameState.getFood().asList()
    foodCount = len(newFood)
    foodScore = 0
    newPos = currentGameState.getPacmanPosition()
    minFoodDist = float("inf")
    for food in newFood:
        minFoodDist = min(minFoodDist, manhattanDistance(newPos, food))
    
    foodScore = foodCount*-500
    foodDistScore = (1/minFoodDist)*10
    
    
    #Step 2 - Penalize for getting close to ghosts
    ghostScore = 0
    numCloseGhosts = 0
    newGhostStates = currentGameState.getGhostStates()
    for ghost in currentGameState.getGhostPositions():
            if (manhattanDistance(newPos, ghost) < 6):
                numCloseGhosts += 1
    ghostScore = numCloseGhosts * -20
    
    #Step 4 - Reward for eating pellets and ghosts

    totalScore = foodScore + totalScore + ghostScore
    return totalScore
 
    
    
    "*****************************Q5 Ends Here***************************************************"

# Abbreviation
better = betterEvaluationFunction
