class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.route_dict = {}
        
        for key, value in self.nodes:
            if key in self.route_dict:
                self.route_dict[key].append(value)
            else:
                self.route_dict[key] = [value]
    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        if start not in self.route_dict:
            return []
        all_paths = []
        
        for place in self.route_dict[start]:
            if not place in path:
                new_paths = self.get_paths(place, end, path)
                for p in new_paths:
                    all_paths.append(p)
        return all_paths
                    
            
if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    
    my_graph = Graph(routes)
    print(my_graph.route_dict)
    
    print(my_graph.get_paths("Mumbai", "Bangaluru"))
