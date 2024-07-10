
# Email OTP Validation Python

API, Database & Class Implementation Python Project to Validate OTP Real Time Send and Validation & Updates Database for the Same Status.

- Takes Email input from User and Validates the Email based on email Pattern i.e. [a-z0-9._+]@[a-z0-9].[a-z]{2,4}.
- then, OTP will generate using random module of python
- then, Python SMTP Module is used to send OTP if OTP sends successfully return True else Error.
- if True, then create an entry for OTP details in Database, and execute validate otp method.
- Validation of OTP is based on the following Criteria i.e., OTP must be entered within 60 seconds, OTP must be six digit integer value, OTP must be entered in five Tries.
- If Validation passed the following criteria, then Validate OTP and Update status for the same as Success.
- Else Throw error Message for the same, and update database entry for Failed.




## Documentation Reference

 - [SMTP Documentation](https://docs.python.org/3/library/smtplib.html)
 - [GitHub README](https://github.com/mohit-trootech/Email-OTP-Validation)

## Installation

_**Prerequisite: Install Python into Your System, Install Required Libraries ie. requests, sqlite3, Vonage**_

- Install my-project with git clone

```
  git clone https://github.com/mohit-trootech/Email-OTP-Validation
  cd Email-OTP-Validation
```
-  Create New Files

```
  touch constants.py

[//]: # (SMTP_HOST = "smtp.gmail.com"
[//]: # (SMTP_PORT = 587)
**Read Documentation to Generate app password for SMTP
  Create Reference Constants Variables for Error Free Execution**
```

- Run Python Files

```
  python otp.py
```
