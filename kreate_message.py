from data_base import SQLighte
import config

class CreateMessage():

    def create_first_message():
        db = SQLighte(config.database)
        rownumber = 0
        reply_message=f"Нові повідомлення на https://replace.org.ua : \r\n \r\n"
        while True:
            result=db.select_single(rownumber, "message_data")
            if result == None:
                break
            one_message = f"Втемі \"{result[5]}\" останнє повідомлення від {result[4]} o {result[3]}. \r\nЩоб прочитати перейдіть за посиланням <a>{result[2]}<\a>. \r\n \r\n"
            reply_message += one_message
            rownumber += 1
            print(result)
        return(reply_message)

    def return_time_last_message():
        db=SQLighte(config.database)
        return((db.select_single(1, "message_data"))[3])


CreateMessage.return_time_last_message()


