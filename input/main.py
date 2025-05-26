def reading_message():
    with open(r"C:\Users\Aledari\Desktop\vs python\message.py\input\satrting_letter.txt","r")as phastog:
        letter_content = phastog.read()
        return letter_content
    
def reading_names():
    with open(r"C:\Users\Aledari\Desktop\vs python\message.py\names\first_names.txt","r") as phastog:
        names_list=[]
        names = phastog.readlines()
        for i in names:
            x=i.strip("\n")
            if x != "":
                names_list.append(x)
        
        return names_list
            
def out_put(names,letter_content):
    for i in names:
        with open(f"./message.py/output/{i}.txt","w") as fofo:
            final=letter_content.replace("[First Name]",i)
            final = final.replace("[Company Name]","octocode")
            fofo.write(final)

out_put(letter_content=reading_message(),names=reading_names())
print(reading_names())