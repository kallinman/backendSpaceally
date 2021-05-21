class Spaceally:
    def __init__(self):
        self.userlist={}
        self.assignments={}
        self.images={}

    def createuser(self, username, emailaddress):
        self.userlist[emailaddress]=username

        return 1

    def createassignment(self, assigner, assigned):
        if assigned in self.assignments:
            self.assignments[assigned].append(assigner)
        else:
            self.assignments[assigned]=[assigner]
        return 1

    def getAssignments(self, assigned):
        if assigned in self.assignments:
            return self.assignments[assigned]
        else:
            print(assigned + " has no spaces to assign to")
            return []

    def getImageIDs(self, assigner):
        if assigner in self.images:
            return self.images[assigner]
        else:
            print(assigner + " has no images")
            return []

    def postImage(self, url, ufrom, uto):
        if uto in self.images:
            self.images[uto].append(url)
        else:
            self.images[uto] = [url]


    def description(self):
        print('This is Spaceally')
        print("Users")
        print(self.userlist)
        print()
        print("Assignments")
        print(self.assignments)
        print()
        print("Images")
        print(self.images)
