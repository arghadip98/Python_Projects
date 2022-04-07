letter =''' Dear <|NAME|>,

Congratulations for clearing the SBI Clerk Prelims with a very good percentile.
Now you have selected for the SBI Clerk Mains.
Best wishes for your great life
Greetings from,

            Kolkata Mahendra's

Date: <|DATE|>
'''
name = input("Enter your name\n : ")
date = input("Enter date\n : ")
letter = letter.replace ("<|NAME|>", name)
letter = letter.replace ("<|DATE|>", date)
print (letter)