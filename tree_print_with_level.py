"""
Build below location tree using TreeNode class

Global
|--India
  |--Gujarat
    |--Ahmedabad
    |--Baroda
  |--Karnataka
    |--Bengaluru
    |--Mysuru
|--USA
  |--NewJersy
    |--Princton
    |--Trenton
  |--California
    |--SanFrancisco
    |--Mountain View
    |--Palo Alto

Now modify print_tree method to take tree level as input. And that should print tree only upto that level
"""
class Tree:
    def __init__(self):
        self.data = None
        self.child = []
        self.parent = None
    
    def add_member(self, new_member):
        new_member.parent = self
        self.child.append(new_member)
    
    def _get_level(self):
        if not self.parent:
            return 0
        while self.parent:
            self = self.parent
            return 1 + self._get_level()
    
    def print(self, level):
        spaces = "  "
        decoration = "|--"
        my_level = self._get_level()
        if not self.parent and level >= 0:
            print(self.data)
        if my_level+1 > level:
            return
        for item in self.child:
            printable = spaces * my_level + decoration
            print(printable + item.data)
            if item.child:
                item.print(level)
                
if __name__ == "__main__":
    root = Tree()
    root.data = "Global"
    
    India = Tree()
    India.data = "India"
    root.add_member(India)
    
    Gujarat = Tree()
    Gujarat.data = "Gujarat"
    India.add_member(Gujarat)
    
    Ahmedabad = Tree()
    Ahmedabad.data = "Ahmedabad"
    Gujarat.add_member(Ahmedabad)  

    Baroda = Tree()
    Baroda.data = "Baroda"
    Gujarat.add_member(Baroda)    
    
    Karnataka = Tree()
    Karnataka.data = "Karnataka"
    India.add_member(Karnataka)
    
    Bengaluru = Tree()
    Bengaluru.data = "Bengaluru"
    Karnataka.add_member(Bengaluru)  
    
    Mysuru = Tree()
    Mysuru.data = "Mysuru"
    Karnataka.add_member(Mysuru)
    
    USA = Tree()
    USA.data = "USA"
    root.add_member(USA)
    
    NJ = Tree()
    NJ.data = "NewJersy"
    USA.add_member(NJ)
    
    Princton = Tree()
    Princton.data = "Princton"
    NJ.add_member(Princton)  

    Trenton = Tree()
    Trenton.data = "Trenton"
    NJ.add_member(Trenton)    
    
    California = Tree()
    California.data = "California"
    USA.add_member(California)
    
    sf = Tree()
    sf.data = "SanFrancisco"
    California.add_member(sf)  
    
    MtView = Tree()
    MtView.data = "Mountain View"
    California.add_member(MtView)
    
    PaloAlto = Tree()
    PaloAlto.data = "Palo Alto"
    California.add_member(PaloAlto)    
    
    root.print(2)
    
    
