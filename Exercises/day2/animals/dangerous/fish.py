class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Stonefish', 'White Shark', 'Boxfish', 'Lionfish']
 
    def printMembers(self):
        print('Printing members of the dangerous Fish class')
        for member in self.members:
            print('\t%s ' % member)