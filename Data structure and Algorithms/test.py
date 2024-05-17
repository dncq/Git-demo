class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

class FamilyTree:
    def __init__(self):
        self.root = None
        self.node_map = {}

    def add_node(self, child, parent):
        if child not in self.node_map:
            self.node_map[child] = Node(child, parent)

        if parent not in self.node_map:
            self.node_map[parent] = Node(parent)

        self.node_map[child].parent = self.node_map[parent]
        self.node_map[parent].children.append(self.node_map[child])

        if self.root is None:
            self.root = self.node_map[child]

    def get_children(self, name):
        print([i.name for i in self.node_map[name].children])
    def printNodemap(self):
        for i in self.node_map:
            print(i, self.node_map[i].children)
    def get_descendants(self, name):
        queue = [self.node_map[name]]
        descendants = set()

        while queue:
            node = queue.pop(0) 
            descendants.add(node)

            for child in node.children:
                queue.append(child)

        return len(descendants) - 1
    def get_generation(self, name):
        node = self.node_map[name]
        generation = 0
        des = node.children
      
        if des == []:
            return generation
        generation += 1
        
            
        
        # while node.parent is not None:
        #     node = node.parent
        #     generation += 1

        # return generation + 1



def main():
    family_tree = FamilyTree()

    while True:
        line = input()
        if line == "***":
            break

        child, parent = line.split()
        family_tree.add_node(child, parent)

    queries = []
    while True:
        line = input()
        if line == "***":
            break
        queries.append(line)
    for line in queries:
        cmd, param = line.split()

        if cmd == "descendants":
            print(family_tree.get_descendants(param))
        elif cmd == "generation":
            print(family_tree.get_generation(param))
    family_tree.get_children("Tuan")

if __name__ == "__main__":
    main()




# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.parent = None
#         self.children = []

# class FamilyTree:
#     def __init__(self):
#         self.people = {}

#     def add_person(self, person):
#         self.people[person.name] = person

#     def find_person(self, name):
#         return self.people[name]

#     def descendants(self, person):
#         count = 1
#         for child in person.children:
#             count += self.descendants(child)
#         return count

#     def generation(self, person):
#         if person.parent is None:
#             return 0
#         else:
#             return 1 + self.generation(person.parent)

# def parse_input(input_file):
#     family_tree = FamilyTree()

#     # Parse the child-parent relations.
#     for line in input_file:
#         if line == "***":
#             break

#         child, parent = line.split()
#         child_person = Person(child)
#         parent_person = Person(parent)

#         family_tree.add_person(child_person)
#         family_tree.add_person(parent_person)

#         child_person.parent = parent_person
#         parent_person.children.append(child_person)

#     # Parse the queries.
#     queries = []
#     for line in input_file:
#         if line == "***":
#             break

#         cmd, param = line.split()
#         queries.append((cmd, param))

#     return family_tree, queries

# def main():
#     input_file = open(r"C:\python code\Data structure and Algorithms\input.txt", "r")
#     family_tree, queries = parse_input(input_file)


#     # Answer the queries.
#     for cmd, param in queries:
#         if cmd == "descendants":
#             person = family_tree.find_person(param)
#             count = family_tree.descendants(person)
#             print(count)
#         elif cmd == "generation":
#             person = family_tree.find_person(param)
#             generation = family_tree.generation(person)
#             print(generation)

# if __name__ == "__main__":
#     main()

