from Spaceally import *

sa = Spaceally()
sa.description()

id1 = sa.createuser(username="u1", emailaddress="u1@m.com")
id2 = sa.createuser(username="u2", emailaddress="u2@m.com")
id3 = sa.createuser(username="u3", emailaddress="u3@m.com")
id4 = sa.createuser(username="u4", emailaddress="u4@m.com")

# Assign space to a friend
sa.createassignment(assigner="u1", assigned="u2")
sa.createassignment(assigner="u3", assigned="u2")

# Get space I can assign to
ux="u2"
print(ux + " can assign to:")
for assigner in sa.getAssignments(ux):
    print(assigner)

# get imagesIDs for a user
#ux="u1"
#for imageid in sa.getImageIDs(ux):
#    print(imageid)

# post image to a user
ufrom="u2"
uto="u1"
sa.postImage(url="url1", ufrom="u2", uto="u1")
uto="u3"
sa.postImage(url="url2", ufrom="u2", uto="u3")


# get imagesIDs for a user
ux="u1"
print(ux + "has the following imageIDs")
for imageid in sa.getImageIDs(ux):
    print(imageid)

# get imagesIDs for a user
ux="u3"
print(ux + "has the following imageIDs")
for imageid in sa.getImageIDs(ux):
    print(imageid)
