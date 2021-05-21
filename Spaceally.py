class Spaceally:
    def __init__(self):
        self.userlist={}
        self.assignments={}
        self.images={}

    # respons to /Spaceally/users/ POST
    def users_post(self, username, emailaddress):
        self.userlist[emailaddress]=username

        return 1

    # respons to /spaceally/users/ GET
    def users_get(self):
        return self.userlist

    # respons to /spaceally/assignments/assigned/ POST
    def assignments_post(self, assigner, assigned):
        if assigned in self.assignments:
            self.assignments[assigned].append(assigner)
        else:
            self.assignments[assigned]=[assigner]
        return 1

    # respons to /spaceally/assignments/assigned/ GET
    def assignments_get(self, assigned):
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

    def show_users(self):
        print()
        print("userlist:")
        for email, username in self.userlist.items():
            print(email + " " + username)

    def show_assignments(self):
        print()
        print("assignments:")
        for assigned, assigners in self.assignments.items():
            print(assigned + " can post images to:")
            for assigner in assigners:
                print(assigner)
        #for email, username in self.userlist.items():
        #    print(username + " can post images to:")
        #    for assigner in self.assignments_get(username):
        #        print(assigner)

    def show_images(self):
        print()
        print("images:")
        for receiver, pics  in self.images.items():
            print(receiver + " has the following images:")
            for pic in pics:
                print(pic)
