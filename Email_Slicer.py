
import re



def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False

def slice(email):

    ind=email.find('@') #2
    user_name=email[0:ind]  #hi@gmail.com # gmail.com


    after_at=email[ind+1:] #gmail.com

    ind1=after_at.find('.')+ind+1
    domain_name=email[ind+1:ind1]

    print('User Name :', user_name)
    print('Domain Name :' ,domain_name)


if __name__ == '__main__':
        s=input()
        if(check(s)==True):
            slice(s)
        else:
            print('Please Enter Valid Email Id')