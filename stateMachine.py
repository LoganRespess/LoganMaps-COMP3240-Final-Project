class statemachine:
    def __init__(self, stateTransition, terminalState):
        self.stateTranstion = stateTransition
        self.terminalState = terminalState
        self.countTerminalPathsCache = {}
    def isTerminal(self, state):
        return state in self.terminalState
    def countTerminalPaths(self, state):
        """Counts how many paths go from `state` to any terminal state."""
        acc = int(self.is_terminal(state))
        for actions, next_state in self._state_transitions.get(state, []):
            acc += len(actions) * self.count_terminal_paths(next_state)
        return acc
    def count_terminal_paths(self, state):
        """Counts how many paths go from `state` to any terminal state."""
        if state not in self.countTerminalPathsCache:
            acc = int(self.is_terminal(state))
            for actions, next_state in self._state_transitions.get(state, []):
                acc += len(actions) * self.count_terminal_paths(next_state)
            self.countTerminalPathsCache[state] = acc
        return self.countTerminalPathsCache[state]
