import random
import string
import matplotlib.pyplot as plt

# --- Parameters ---
TARGET_STRING = "Hello, World!"
VALID_GENES = string.ascii_letters + string.punctuation + " "
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
ELITISM_RATE = 0.1 # Percentage of the best individuals to keep

class GeneticAlgorithm:
    """
    A simple Genetic Algorithm implementation to solve the target string problem.
    
    The algorithm follows these steps:
    1. Initialization: Create a random population of individuals.
    2. Fitness: Evaluate how 'fit' each individual is (how close it is to the target).
    3. Selection: Select the best individuals to be parents for the next generation.
    4. Crossover: Combine the 'genes' of two parents to create a child.
    5. Mutation: Introduce small, random changes to the child's genes.
    6. Repeat: Repeat steps 2-5 until a perfect solution is found.
    """
    
    def __init__(self, target, population_size, mutation_rate, elitism_rate):
        self.target = list(target)
        self.target_length = len(target)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        
        # Calculate how many 'elite' individuals to keep each generation
        self.elite_size = int(self.population_size * self.elitism_rate)
        
        # Initialize the population
        self.population = self.create_initial_population()

    def create_individual(self):
        """Creates a single random individual (a list of characters)."""
        return [random.choice(VALID_GENES) for _ in range(self.target_length)]

    def create_initial_population(self):
        """Creates the starting population of random individuals."""
        return [self.create_individual() for _ in range(self.population_size)]

    def calculate_fitness(self, individual):
        """
        Calculates the fitness of an individual.
        Fitness = number of characters that match the target string.
        """
        score = 0
        for i in range(self.target_length):
            if individual[i] == self.target[i]:
                score += 1
        return score

    def crossover(self, parent1, parent2):
        """
        Performs single-point crossover between two parents.
        Takes the first half of parent1's genes and the second half of parent2's.
        """
        # Ensure midpoint is valid even for short strings
        if self.target_length < 2:
            return parent1
        
        midpoint = random.randint(1, self.target_length - 1)
        child = parent1[:midpoint] + parent2[midpoint:]
        return child

    def mutate(self, individual):
        """
        Applies mutation to an individual.
        For each gene, there is a `MUTATION_RATE` chance it will be
        replaced with a new random gene.
        """
        mutated_individual = list(individual) # Work on a copy
        for i in range(self.target_length):
            if random.random() < self.mutation_rate:
                mutated_individual[i] = random.choice(VALID_GENES)
        return mutated_individual

    def evolve(self):
        """Runs one full generation of evolution."""
        
        # 1. Calculate fitness for the entire population
        # We store this as a list of (individual, fitness_score) tuples
        pop_with_fitness = [
            (ind, self.calculate_fitness(ind)) for ind in self.population
        ]
        
        # 2. Sort the population by fitness (highest first)
        pop_with_fitness.sort(key=lambda x: x[1], reverse=True)
        
        # Get the current best individual and its fitness
        self.best_individual = pop_with_fitness[0][0]
        self.best_fitness = pop_with_fitness[0][1]
        
        # 3. Selection (Elitism)
        # The new generation starts with the most 'elite' individuals
        sorted_population = [ind for ind, fitness in pop_with_fitness]
        new_population = sorted_population[:self.elite_size]
        
        # 4. Crossover & 5. Mutation
        # Fill the rest of the new population with children
        
        # We'll use the top 50% of the population as the 'parent pool'
        # This is a simple form of "truncation selection"
        parent_pool = sorted_population[:self.population_size // 2]
        
        num_children = self.population_size - self.elite_size
        
        for _ in range(num_children):
            # Pick two random parents from the pool
            parent1 = random.choice(parent_pool)
            parent2 = random.choice(parent_pool)
            
            # Create the child
            child = self.crossover(parent1, parent2)
            
            # Mutate the child
            mutated_child = self.mutate(child)
            
            # Add the new child to the new population
            new_population.append(mutated_child)
            
        # The new generation is complete
        self.population = new_population

    def run(self):
        """
        Runs the genetic algorithm until the target string is found.
        """
        generation = 0
        
        # Lists to store history for plotting
        generation_history = []
        fitness_history = []
        
        while True:
            self.evolve()
            
            # Store data for plotting
            generation_history.append(generation)
            fitness_history.append(self.best_fitness)
            
            # Convert list of chars to a string for printing
            best_str = "".join(self.best_individual)
            
            # --- MODIFIED: Only print every 10 generations ---
            if generation % 10 == 0 or self.best_fitness == self.target_length:
                print(f"Gen {generation: <4} | Best Fitness: {self.best_fitness: >2}/{self.target_length} | Best String: {best_str}")
            
            # Check for a perfect solution
            if self.best_fitness == self.target_length:
                print(f"\nSolution found in {generation} generations!")
                
                # --- NEW: Plot the results ---
                self.plot_results(generation_history, fitness_history)
                break
                
            generation += 1

    def plot_results(self, generations, fitness_scores):
        """
        Uses matplotlib to plot the fitness over generations.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(generations, fitness_scores)
        plt.title("Genetic Algorithm Performance: Fitness Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Best Fitness Score")
        
        # Set Y-axis limits to be from 0 to the max possible fitness
        plt.ylim(0, self.target_length + 1)
        plt.grid(True)
        
        # Save the plot to a file
        plot_filename = "ga_fitness_plot.png"
        try:
            plt.savefig(plot_filename)
            print(f"Saved fitness plot to: {plot_filename}")
        except Exception as e:
            print(f"Error saving plot: {e}")
        
        # Show the plot
        plt.show()

# --- Main execution ---
if __name__ == '__main__':
    # Create an instance of the algorithm
    ga = GeneticAlgorithm(
        target=TARGET_STRING,
        population_size=POPULATION_SIZE,
        mutation_rate=MUTATION_RATE,
        elitism_rate=ELITISM_RATE
    )
    
    # Run the simulation
    ga.run()

