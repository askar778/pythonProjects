list_districts = ['ALAPPUZHA', 'ERNAKULAM', 'KOZHIKODE', 'PALAKKAD', 'KOLLAM', 'KANNUR', 'KASARAGOD', 'IDUKKI',
                  'KOTTAYAM', 'THRISSUR', 'PATHANAMTHITTA', 'MALAPPURAM', 'WAYANAD', 'TRIVANDRUM']

class DataFunctions:

    def location_finder(User_answer, districts):

        for name in districts:
            if User_answer == name[0]:
                x = name[1]
                y = name[2]
                print(x, y)

    def check_answer(user_answer):
        if user_answer in list_districts:
            location_finder()
        else:
            print("fail")



