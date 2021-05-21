from Spaceally import *

sa = Spaceally()

# Skapa användare
id1 = sa.users_post(username="u1", emailaddress="u1@m.com")
id2 = sa.users_post(username="u2", emailaddress="u2@m.com")
id3 = sa.users_post(username="u3", emailaddress="u3@m.com")
id4 = sa.users_post(username="u4", emailaddress="u4@m.com")

sa.show_users()
#print()
#print("Userlist:")
#for email, username in ul.items():
#    print(email + " " + username)

# Assign space to a friend
sa.assignments_post(assigner="u1", assigned="u2")
sa.assignments_post(assigner="u3", assigned="u2")
sa.assignments_post(assigner="u3", assigned="u4")
sa.assignments_post(assigner="u2", assigned="u1")
sa.assignments_post(assigner="u2", assigned="u4")

sa.show_assignments()

# get imagesIDs for a user
#ux="u1"
#for imageid in sa.getImageIDs(ux):
#    print(imageid)

# post image to a user
sa.postImage(url="url1", ufrom="u2", uto="u1")
sa.postImage(url="url2", ufrom="u2", uto="u3")
sa.postImage(url="url3", ufrom="u4", uto="u3")

sa.show_images()

# get imagesIDs for a user
#ux="u1"
#print(ux + "has the following imageIDs")
#for imageid in sa.getImageIDs(ux):
#    print(imageid)

# get imagesIDs for a user
#ux="u3"
#print(ux + "has the following imageIDs")
#for imageid in sa.getImageIDs(ux):
#    print(imageid)

#ul = sa.users_get()
#print(ul)

#sa.description()
