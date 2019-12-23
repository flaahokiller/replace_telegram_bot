from data_base import SQLighte
import config

class CreateMessage():

    def create_first_message(rownumber = 0):#Створює текст повідомлення
        db = SQLighte(config.database)
        reply_message=f"Нові повідомлення на https://replace.org.ua : \r\n \r\n"
        while True:
            result=db.select_single(rownumber, "message_data")
            if result == None:
                break
            one_message = f"Втемі \"{result[5]}\" останнє повідомлення від {result[4]} o {result[3]}. \r\nЩоб прочитати перейдіть за посиланням {result[2]}. \r\n \r\n"
            reply_message += one_message
            rownumber += 1
        return(reply_message)

    def return_id_new_user():#Повертає id для новрго юзера в базі данних.
        db = SQLighte(config.database)
        ids=0
        rownumber=0
        while True:
            id_=db.select_single_user(rownumber, "users")
            if id_ == None:
                return ids
            rownumber+=1
            print(id_[0])
            ids=id_[0]+1



