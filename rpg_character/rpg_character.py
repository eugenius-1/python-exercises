full_dot = '●'
empty_dot = '○'

def create_character(c_name, c_strength, c_intelligence, c_charisma):
    if not isinstance(c_name, str):
        return 'The character name should be a string'
    elif c_name == '':
        return 'The character should have a name'
    elif len(c_name) > 10:
        return 'The character name is too long'
    elif " " in c_name:
        return 'The character name should not contain spaces'

    if not (isinstance(c_strength, int) and isinstance(c_intelligence, int) and isinstance(c_charisma, int)):
        return 'All stats should be integers'
    elif c_strength < 1 or c_intelligence < 1 or c_charisma < 1:
        return 'All stats should be no less than 1'
    elif c_strength > 4 or c_intelligence > 4 or c_charisma > 4:
        return 'All stats should be no more than 4'
    elif (c_strength + c_intelligence + c_charisma) != 7:
        return 'The character should start with 7 points' 
    
    def display_stats(val):
        display_str = ''

        for i in range(1, 11):
            if i <= val:
                display_str += full_dot
            else:
                display_str += empty_dot
        
        return display_str

    return f"{c_name}\nSTR {display_stats(c_strength)}\nINT {display_stats(c_intelligence)}\nCHA {display_stats(c_charisma)}\n"


print(create_character('companyman', 2, 4, 1))
print(create_character('robmarkman', 3, 3, 1))
print(create_character('fsignifier', 2, 4, 1))
print(create_character('gmalone', 4, 1, 2))
print(create_character('profsky', 1, 4, 2))
print(create_character('ejanelle', 2, 3, 2))
print(create_character('beekay', 1, 3, 3))