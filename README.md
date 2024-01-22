# Password Strength Checking and Cracking through Dictionary Attacks

The most common and easy way to cracking passwords is through Bruteforcing. Given that many people use common English words or phrases as their passwords, a Dictionary Attack will be highly likely to crack them. Even if the database stores hashed passwords, these kind of passwords are not safe for use.

There are two ways we can try to prevent this:
* Use a strong password with at least 1 uppercase letter, 1 special character and 1 digit.
* Use Salting before hashing passwords.

This is a simple python program, that:
1. Checks for password strength. 
2. It will run a Hashing algorithm to create a SHA256 hash of your password. 
3. It will generate a random string as Salt
4. It will run the Hashing algorithm to create a SHA256 hash of your salt+password. 
5. It will finally try to brute force and attempt to match the Salted Hash and Plain Hash of your password against a dictionary of the most common used passwords.
