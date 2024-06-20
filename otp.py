"""Python Project to Generate and Validate OTPs"""
import math
import re
import random
import constant
from smtplib import SMTP
from datetime import datetime, date
from utils import EmailInvalid
from otp_database import DatabaseOtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class OTP(DatabaseOtp):
    """
    class to implement OTP generation and validation, along with a description of its functionality.
    """

    def __init__(self) -> None:
        """
        create Instances for otp Object
        """
        super().__init__()
        self.otp = ""

    def generate_otp(self) -> str:
        """
        otp generate using random method
        @return: str
        """
        for i in range(6):
            self.otp += str(math.floor(random.random() * 10))
        return self.otp

    def validate_otp(self, email: str) -> None:
        """
        method to validate otp checks time difference not more than 60 seconds &
        tries to match otp for 5 times else return failed
        @param email: str
        """
        otp_data = self.get_last_otp_data(email)
        time_difference = constant.CURRENT_TIME - datetime.strptime(otp_data[2],
                                                                    "%Y-%m-%d %H:%M:%S")
        tries = 5
        while True:
            try:
                if time_difference.total_seconds() > 60:
                    raise Exception(constant.EXPIRY_OTP)
                received_otp = int(input("Enter Received OTP: "))
                if received_otp == int(otp_data[-2]):
                    print(constant.VALIDATE_OTP)
                    self.status_update(otp_data, constant.STATUS_SUCCESS)
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print(constant.NO_TRY)
                        self.status_update(otp_data, constant.STATUS_FAILED)
                        break
                    else:
                        print(f"You are Left With {tries} Tries Try Again")
            except ValueError:
                tries -= 1
                print(f"You are Left With {tries} Tries Try Again")
                print("Try Entering a Numeric OTP Received")
                self.status_update(otp_data, constant.STATUS_FAILED)
            except Exception as e:
                print(e)


class OtpSend(OTP):
    """This code implements a class that generates and send one-time passwords (OTPs)."""

    def __init__(self, email: str) -> None:
        """
        Constructor for the Main Mail Method
        @param email: str
        """
        super().__init__()
        self.email = email
        try:
            self.validate_email(self.email)
            otp = self.generate_otp()
            if self.send_otp(self.email, otp):
                self.create_otp_entry(self.email, otp)
                self.validate_otp(self.email)
        except Exception as e:
            print(e)

    @staticmethod
    def validate_email(email: str) -> None:
        """
        validate Email Address if email follows the Email Pattern
        @param email: str
        """
        if not re.match(constant.EMAIL_PATTERN, email):
            raise EmailInvalid(constant.EMAIL_ERROR)

    @staticmethod
    def send_otp(email: str, otp: str) -> bool:
        """
        send otp methods to send otp to recipient email address using python smtp
        @param email: str
        @param otp: str
        @return: bool
        """
        try:
            with SMTP(constant.SMTP_HOST, constant.SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(constant.SMTP_EMAIL, constant.SMTP_PASSKEY)
                message = MIMEMultipart()
                message["Subject"] = "OTP Validation"
                body = constant.EMAIL_BODY.format(date_today=str(date.today()), otp_number=otp)
                message.attach(MIMEText(body, "html"))
                smtp.sendmail(constant.SMTP_EMAIL, email, message.as_string())
                return True
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        # print("Email Must Follow the Syntax [a-z0-9._+]@[a-z0-9].[a-z]{2,4}")
        # email_input = input("Enter your Email Address: ")
        # obj = OtpSend(email_input)
        obj = OtpSend(constant.TEST_EMAIL)
    except Exception as error:
        print(error)
