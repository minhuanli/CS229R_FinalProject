import numpy as np

class BaldwinOptimize:
    
    def __init__(self, fitness_function, initial_points, dim=1, population_size=200):
        self.fitness_function = fitness_function
        self.current_points = initial_points
        
        self.points_track = []
        self.points_track.append(self.current_points)
        
        #TODO: Add Assertion about the dimension here
        
    def evaluation(self, points=None):      
        if points == None:
            self.fitness_score = self.fitness_function(self.current_points) 
        else:
            self.fitness_score = self.fitness_function(points)
            
    def learning(self,):
        #TODO: make this function parallel

        
    