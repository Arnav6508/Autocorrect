def delete_letter(word):
    delete_l = []

    for i in range(len(word)):
        delete_l.append(word[:i]+word[i+1:])

    return  delete_l

def switch_letter(word):
    switch_l = []
    
    for i in range(len(word)-1):
        switch_l.append(word[:i]+word[i+1]+word[i]+word[i+2:])
    
    return switch_l

def replace_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []

    for i in range(len(word)):
        for j in range(26):
            if word[i] == letters[j]: continue
            replace_l.append(word[:i]+letters[j]+word[i+1:])
  
    return replace_l

def insert_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []

    for i in range(len(word)+1):
        for j in range(26):
            insert_l.append(word[:i]+letters[j]+word[i:])
        
    return insert_l

def edit_one_letter(word, allow_switches = True):
    edit_one_set = set()
    
    edit_one_set.update(insert_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(delete_letter(word))
    if allow_switches: edit_one_set.update(switch_letter(word))
    
    return set(edit_one_set)

def edit_two_letters(word, allow_switches = True):
    edit_two_set = set()
    
    edit_one = edit_one_letter(word,allow_switches)
    for word in edit_one:
        edit_two_set.update(edit_one_letter(word,allow_switches))

    return set(edit_two_set)