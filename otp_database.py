"""Handle Database using Class"""
import sqlite3
import constant
from sqlite3 import connect


class DatabaseOtp:
    """This class handles and manages a database to store and fetch OTPs. It offers an organized and reliable way to
    store and retrieve OTPs in a database, making it a valuable tool for applications that require secure
    authentication or password reset processes."""

    def __init__(self) -> None:
        """create instance variable for object"""
        self.db = connect(constant.DB)
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS email_otp (id INTEGER PRIMARY KEY, "
                            "email varchar(32), "
                            "sending_time varchar(32),"
                            "otp varchar(6),"
                            "status varchar(10));")

    def create_otp_entry(self, email: str, otp: str) -> None:
        """
        create an otp entry with the following details in a database,
        (id: serial, number, datetime: current, otp, status: pending)
        @param otp: str
        @param email: str
        @return: None
        """
        try:
            self.cursor.execute("INSERT INTO email_otp (email, sending_time, otp, status) VALUES"
                                f"('{email}', '{str(constant.CURRENT_TIME)}', '{otp}', '{constant.STATUS_PENDING}');")
            self.db.commit()
        except sqlite3.OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
        except Exception as e:
            print(e)

    def get_last_otp_data(self, email: str) -> tuple:
        """
        get last generated otp data
        @param email: str
        @return: tuple
        """
        try:
            data = self.cursor.execute(f"SELECT * FROM email_otp WHERE email = '{email}' and status = 'Pending' ORDER "
                                       f"BY "
                                       f"sending_time DESC;")
            return data.fetchall()[0]
        except sqlite3.OperationalError as e:
            print(constant.OPERATIONAL_ERROR, e)
        except IndexError:
            print("No Otp Generated for email {}".format(email))
        except Exception as e:
            print(e)

    def status_update(self, otp_data: tuple, status: str) -> None:
        """
        update status in database execution
        @param otp_data: tuple
        @param status: str
        """
        self.cursor.execute(f"UPDATE email_otp SET status = '{status}' where id = {otp_data[0]}")
        self.db.commit()


if __name__ == "__main__":
    obj = DatabaseOtp()

