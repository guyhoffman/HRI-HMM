import numpy as np
from matplotlib import pyplot as plt

class BinaryHMM:
    """Implementation of a binary variable Hidden Markov Model
    """
    def __init__(self, varname, startprob, transmat, emissionprob):
        """_summary_

        Args:
            varname (string): Name for hidden variable 
            startprob (2x1 array): Initial (t=0) probability distribution for variable.
            transmat (2x2 array): HMM transition model
            emissionprob (2x2 array): HMM emission model
        """
        ############################################################################
        # TODO: Add any needed initialization for the HMM class here.              #
        ############################################################################
        # YOUR CODE HERE

        raise NotImplementedError()

        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################

    def transition(self):
        """Apply HMM transition model
        """
        ############################################################################
        # TODO: Implement the transition model using matrix multiplication.        #
        ############################################################################
        # YOUR CODE HERE

        raise NotImplementedError()

        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################
        
    def evidence(self, e):
        """Apply the HMM evidence step

        Args:
            e (boolean): This time step's evidence for hidden variable.
        """
        ############################################################################
        # TODO: Implement the emission model using matrix multiplication.          #
        ############################################################################
        # YOUR CODE HERE

        raise NotImplementedError()

        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################
            
    def filter(self, e):
        """Run the Filtering algorithm, including the transition and evidence step 

        Args:
            e (boolean): This time step's evidence for the hidden variable.
        """
        self.timestep()
        self.evidence(e)
        
    def reset(self, startprob=None):
        """Reset model with optional starting probability

        Args:
            startprob (2x1 array, optional): New initial (t=0) probability for HMM. Defaults to None.
        """
        ############################################################################
        # TODO: Implement a reset of the belief for the HMM.                       #
        ############################################################################
        # YOUR CODE HERE

        raise NotImplementedError()

        ############################################################################
        #                             END OF YOUR CODE                             #
        ############################################################################
        
    def print_belief(self):
        """Print belief in numerical and bar graph form.
        """

        print ("Current belief: ", self._belief)
        
        plt.bar([0, 1], self._belief, width=.5)
        ax = plt.gca()

        ax.set_xlim(-.5, 1.5)
        ax.set_ylim(0, 1)
        
        labels = [self._varname, "¬"+self._varname]
        ax.set_xticks([0, 1])
        ax.set_xticklabels(labels)
        
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
