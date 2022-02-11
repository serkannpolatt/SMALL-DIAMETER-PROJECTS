import secrets
import string as st

length=secrets.choice(range(18,21))
symbols=st.ascii_letters+st.digits+st.punctuation
password="".join(secrets.choice(symbols)
for i in range(length))
print(password)
