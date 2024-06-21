"""
Python Files to Store Constants and Private Variables
"""
from datetime import datetime

# SMTP Google Credentials
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

# STATUS
STATUS_FAILED = "Failed"
STATUS_SUCCESS = "Success"
STATUS_PENDING = "Pending"

# EMAIL VALIDATION
EMAIL_PATTERN = "[a-z0-9._+]+@[a-z0-9]+\.[a-z]{2,4}$"
EMAIL_ERROR = "Email Validation Error - Email Must Follow the Syntax [a-z0-9._+]@[a-z0-9].[a-z]{2,4}"

# DB NAME
DB = "otp.db"

# TIME CONSTANT
CURRENT_TIME = datetime.now().replace(microsecond=0)

# Errors
OPERATIONAL_ERROR = "Error in SQL Execution"
VALUE_ERROR = "Enter a Number Input"
EXPIRY_OTP = "Time Limit Reached Try Again with New OTP"
VALIDATE_OTP = "OTP Validation Successfully"
NO_TRY = "Try Again and Generate New OTP"

# EMAIL BODY
EMAIL_BODY = """
<body
  style="margin: 0;font-family: 'Lucida Sans','Lucida Sans Regular','Lucida Grande','Lucida Sans Unicode', Geneva, Verdana, sans-serif;background: #ffffff;font-size: 14px;">
  <div style="
        max-width: 680px;
        margin: 0 auto;
        padding: 45px 30px 60px;
        background: #f4f7ff;
        background-image: url(https://c4.wallpaperflare.com/wallpaper/424/569/251/artwork-pattern-texture-dark-wallpaper-preview.jpg);
        background-repeat: no-repeat;
        background-size: 800px 452px;
        background-position: top center;
        font-size: 14px;
        color: #434343;">
    <header style="width: 100%;text-align: center;display: block;margin: auto;">
      <img alt="" src="https://avatars.githubusercontent.com/u/109086544?s=200&v=4" width="256"
        style="object-fit: cover;" />
      <br>
      <p style="font-size: 24px;font-weight: 400;color: #00b7ff;">
        {date_today}
      </p>
    </header>
    <main>
      <div
        style="margin: 0;margin-top: 70px;padding: 92px 30px 115px;background: #ffffff;border-radius: 30px;text-align: center;">
        <div style="width: 100%; max-width: 489px; margin: 0 auto;">
          <h1 style="margin: 0;font-size: 24px;font-weight: 500;color: #1f1f1f;">
            Your OTP
          </h1>
          <p style="margin: 0;margin-top: 17px;font-weight: 500;letter-spacing: 0.56px;">
            Thank you for working wtih Trootech Buisness Solution pvt ltd. Use the following OTP
            to complete the procedure to validate your email address. OTP is
            valid for
            <span style="font-weight: 600; color: #1f1f1f;">2 minutes</span>.
            Do not share this code with others, including us.
          </p>
          <p style="margin: 0;margin-top: 60px;font-size: 28px;font-weight: 600;letter-spacing: 15px;color: #ba3d4f;">
            {otp_number}
          </p>
        </div>
      </div>
      <p style="max-width: 400px;margin: 0 auto;margin-top: 90px;text-align: center;font-weight: 500;color: #8c8c8c;">
        Need help?<br>Ask at
        <a href="mailto:archisketch@gmail.com" style="color: #499fb6; text-decoration: none;">
          mohit.prajapat@trootech.com
        </a>
        <br>
        visit our
        <a href="https://www.trootech.com" target="_blank" style="color: #499fb6; text-decoration: none;">
          Help Center
        </a>
      </p>
    </main>
    <footer style="width: 100%;max-width: 490px;margin: 20px auto 0;text-align: center;border-top: 1px solid #e6ebf1;">
      <p style="margin: 0;margin-top: 40px;font-size: 16px;font-weight: 600;color: #434343;">
        Trootech Solution
      </p>
      <p style="margin: 0; margin-top: 8px; color: #434343;">
        Address 6th Floor, B Square 1 Thaltej Ahmedabad.
      </p>
      <p style="margin: 0; margin-top: 16px; color: #434343;">
        Copyright © 2022 Company. All rights reserved.
      </p>
    </footer>
  </div>
</body>
"""