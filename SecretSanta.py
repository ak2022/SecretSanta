## Secret Santa Python Code

## Import package to do the random number stuff
from random import randint

## Write a function called secretsanta
def secretsanta():
    people = ["Alannah", "Edmund", "Deepak", "Scott", "Denis", "Shane", "Steph", "Cam", "Vasso", "Martin", "Jonathan", "Bosco", "Roula", "Max", "Eva", "Justyna"] ## List of participants

    ## Banned pairings from each year, in the order [Gift giver, gift reciever]
    disallowed2021 = [["Alannah", "Scott"],["Scott", "Eva"],["Eva", "Deepak"], ["Deepak", "Shane"], ["Shane", "Max"], ["Max", "Denis"], ["Denis", "Cam"], ["Cam", "Edmund"], ["Edmund", "Jonathan"], ["Jonathan", "Alannah"], ["Vasso", "Steph"], ["Steph", "Martin"], ["Martin", "Roula"]] 
    disallowed2020 = [["Alannah", "Denis"],["Scott", "Shane"], ["Deepak", "Jonathan"], ["Shane", "Deepak"], ["Denis", "Alannah"], ["Cam", "Steph"], ["Jonathan", "Roula"], ["Vasso", "Denis"], ["Steph", "Scott"], ["Martin", "Cam"], ["Roula", "Vasso"]] 

    pairing = [] ## Create the new object to temporarily store pairs
    pairings_list = [] ## Create another new object to save pairs

    giver = people[randint(0, (len(people) - 1))] ## Choose a random person from the people list
    original_giver = giver ## Mark this person as the original gift giver (the start of the chain)
    people.remove(original_giver) ## Take this person off the list of people, so they can't be selected to receiver a gift - by definition they have to get a gift from the last person in the loop

    while people != []: ## Do this whilst the list of people still has people in it (so those who haven't yet been selected to recieve a gift)

        reciever = people[randint(0, (len(people) - 1))] ## Select a random person to recieve the gift
        pairing = [giver, reciever] ## Put them in a pair
        if pairing not in disallowed2021 and pairing not in disallowed2020 and giver != reciever: # If the pair isn't a disallowed one that's previously come up
            pairings_list.append(pairing) ## Add the pair to the final list of secret santa pairs

            giver = reciever ## The person who recieved the gift in this pair becomes the next giver. This ensures that only one complete loop forms. 
            people.remove(reciever) ## Take the person who recieved a gift this round off the list of people

    original_pair = [reciever, original_giver] ## The pair that closes the loop - the original giver, and the final reciever 
    pairings_list.append(original_pair) ## Add it to the final list of pairs

    for i,v in enumerate(pairings_list): ## Go through each pair in the list
        datafile = open(f"SecretSanta_{pairings_list[i][0]}.txt", "w") ## Open a text file called SecretSanta_NameOfGifter.txt
        datafile.write(f"Hi {pairings_list[i][0]}, you are buying a gift for {pairings_list[i][1]}. Love Alannah's Secret Santa Bot") ## Write a message in the file with the name of the person who's being bought a gift
        datafile.close() ## Close the file


if __name__ == "__main__": ## Run the function
    secretsanta() ## Thank your local bioinformatician