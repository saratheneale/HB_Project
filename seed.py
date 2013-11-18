# put in a bunch of people and levels and user_levels


# make a main function that says if name = main, add stuff...?

import model

def load_users():
    u1 = model.User(username="pinkiepie", 
                    pettype="dog",
                    petname="Gummy",
                    petgender="m",
                    current_level=2)
    u1.set_password("balloons")    
    model.session.add(u1)

    u2 = model.User(username="rainbowdash", 
                    pettype="penguin",
                    petname="Tank",
                    petgender="m",
                    current_level=1)
    u2.set_password("lightning")    
    model.session.add(u2)

    u3 = model.User(username="twilightsparkle", 
                    pettype="penguin",
                    petname="Owlewiscious",
                    petgender="m",
                    current_level=4)
    u3.set_password("stars")    
    model.session.add(u3) 

    u4 = model.User(username="applejack", 
                    pettype="dog",
                    petname="Winona",
                    petgender="f",
                    current_level=1)
    u4.set_password("apples")    
    model.session.add(u4) 

    u5 = model.User(username="fluttershy", 
                    pettype="bunny",
                    petname="Angel",
                    petgender="m",
                    current_level=3)
    u5.set_password("butterflies")    
    model.session.add(u5) 

def load_levels():
# why isn't the treat postition loading correctly???
    l1 = model.Level(map = "GGG ppp GGG",
                    petStart = "0 1",
                    treatPos = "2 1")
    model.session.add(l1)
# why isn't the treat postition loading correctly???
    l2 = model.Level(map = "GGGG GppG ppGG GGGG",
                    petStart = "0 2",
                    treatPos = "2 1")
    model.session.add(l2)   

    l3 = model.Level(map = "GGGp GGpp GppG ppGG",
                    petStart = "0 3",
                    treatPos = "3 0")
    model.session.add(l3)

    l4 = model.Level(map = "GGGGp GGppp pppGG pGGGG",
                    petStart = "0 3",
                    treatPos = "4 0")
    model.session.add(l4)

def load_user_levels():
    # pinkie does levels 1 and 2
    u_l1 = model.UserLevel(user_id=1, 
                        level_id=1,
                        current_level_input="rr",
                        complete=1)
    model.session.add(u_l1)

    u_l2 = model.UserLevel(user_id=1, 
                        level_id=2,
                        current_level_input="ru",
                        complete=0)
    model.session.add(u_l2)

    # twilight does three levels
    u_l3 = model.UserLevel(user_id=3, 
                        level_id=1,
                        current_level_input="rr",
                        complete=1)
    model.session.add(u_l3)

    u_l4 = model.UserLevel(user_id=3, 
                        level_id=2,
                        current_level_input="rur",
                        complete=1)
    model.session.add(u_l4)

    u_l5 = model.UserLevel(user_id=3, 
                        level_id=3,
                        current_level_input="ruR",
                        complete=1)
    model.session.add(u_l5)

    # fluttershy does two levels
    u_l6 = model.UserLevel(user_id=5,
                        level_id=1,
                        current_level_input="rr",
                        complete=1)
    model.session.add(u_l6)

    u_l7 = model.UserLevel(user_id=5,
                        level_id=2,
                        current_level_input="rur",
                        complete=1)
    model.session.add(u_l7)

def main():
    model.create_tables()
    load_users()
    load_levels()
    load_user_levels()
    model.session.commit()

if __name__ == "__main__":
    main()