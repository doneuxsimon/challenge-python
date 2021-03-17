str_a = 'GAGCCTACTAACGGGAT'
stt_b = 'CATCGTAATGACGGCCT'

def distance(str_1,str_2):
        str_1 = str_1.upper()
        str_2 = str_2.upper()
        if len(str_1)==len(str_2):
                i=0
                a=0
                while i<len(str_1):
                        if str_1[i]!=str_2[i]:
                                a += 1  
                        i=i+1
                print(a)
                return a
        else :
                print('Can not work if list does not have same lenght')

distance(str_a,stt_b)