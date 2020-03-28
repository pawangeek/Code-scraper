import os  

def check_lines(links_of_href):

    f = open("links.txt", "r+")
    line = f.readlines()
    f.close()

    new_line =[]

    for i in line:
        i = i[:-1] # For removing /n from last
        new_line.append(i)

    new_links = list(set(links_of_href).difference(set(new_line)))

    if len(new_links)>=1:
        with open("links.txt", 'a') as f:
            for item in new_links:      
                f.write("%s\n" % item)
        f.close()
    
    return (new_links)