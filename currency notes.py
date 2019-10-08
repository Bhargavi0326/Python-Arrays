def currencyNotes(amount): 
      
    notes = [1000,500,100,50,10,1] 
                 
    get_notes = [0, 0, 0, 0, 0, 0] 
    no_of_notes=0
    
    for i, j in zip(notes, get_notes): 
        if amount >= i: 
            j = amount // i 
            amount = amount - j * i 
            no_of_notes+=j
    print(no_of_notes)
            
amount = int(input())
currencyNotes(amount) 
