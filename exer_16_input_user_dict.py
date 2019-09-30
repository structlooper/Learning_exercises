user_info = {
    "name" : input("Enter the name : "),
    "age" : input("Enter the age : "),
    "fav_movi" : input("Enter the fav_movies comma seprated : ").split(","),
    "fav_songs" : input("Enter the fav_songs comma seprated : ").split(","),

}
# user_info = {
#     "name" : "Deepak",
#     "age" : 23,
#     "fav_movi" : ['coco', 'tiger', 'love it'],
#     "fav_songs" : ['happier', ' love songs'],

# }

for info in user_info:
    print(f"{info} : {user_info[info]}")
# print(user_info)