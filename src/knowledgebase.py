from pysat.formula import CNF
from pysat.solvers import Solver

class KnowledgeBase:
    def __init__(self):
        self.solver = Solver(name='g3')
        self.clauses = CNF()
        self.variable_mapping = {}
        self.reverse_mapping = {}
        self.next_var = 1

    def _get_variable(self, fact):
        """Maps a fact to a unique variable."""
        if fact not in self.variable_mapping:
            self.variable_mapping[fact] = self.next_var
            self.reverse_mapping[self.next_var] = fact
            self.next_var += 1
        return self.variable_mapping[fact]

    def add_fact(self, fact):
        """Adds a fact to the knowledge base."""
        var = self._get_variable(fact)
        self.clauses.append([var])
        self.solver.add_clause([var])
        print(f"Added fact: {fact}")

    def add_implication(self, fact_a, fact_b):
        """Adds an implication (fact_a implies fact_b) to the knowledge base."""
        var_a = self._get_variable(fact_a)
        var_b = self._get_variable(fact_b)
        self.clauses.append([-var_a, var_b])
        self.solver.add_clause([-var_a, var_b])
        print(f"Added implication: {fact_a} => {fact_b}")

    def query(self, fact):
        """Queries the knowledge base to check if a fact is true."""
        var = self._get_variable(fact)
        result = self.solver.solve(assumptions=[var])
        return result

    def infer_new_facts(self):
        """Infers new facts based on existing knowledge."""
        for var in range(1, self.next_var):
            if self.solver.solve(assumptions=[var]):
                fact = self.reverse_mapping[var]
                print(f"Inferred new fact: {fact}")
    
    def print_knowledge_base(self):
        """Prints the current state of the knowledge base."""
        print("Knowledge Base:")
        for fact, var in self.variable_mapping.items():
            print(f"{fact} (variable: {var})")

# Example usage
# kb = KnowledgeBase()
# kb.add_fact("Breeze at (2,2)")
# kb.add_implication("Breeze at (2,2)", "Pit near (2,2)")
# kb.infer_new_facts()
# kb.print_knowledge_base()
