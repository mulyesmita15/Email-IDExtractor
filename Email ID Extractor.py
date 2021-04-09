import re
str1='''

Hello, my name is xyz and my email id is xyz@gmail.com,
And I am learning programming  and I have one more
email:"abc@dt.com"
and some more
email id:<dt@codelover.com>

email:"codelife@dt.com.in" and I have one more gold@codelover.com.

'''
list1=re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")