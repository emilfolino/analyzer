#!/usr/bin/env python3

def show_menu(current_file):
    print()
    print("*********************************************")
    print("Välj i menyn nedan:")
    if not current_file:
        base_menu()
        return "Skriv in ett filnamn att analysera eller välj i menyn: "
    else:
        print("lines: Analysera antalet rader i filen " + current_file + "."  )
        print("words: Analysera antalet ord i filen " + current_file + "."  )
        print("letters: Analysera antalet bokstäver i filen " + current_file + "."  )
        print("word_frequency: Analysera ord frekvensen i filen " + current_file + "."  )
        print("letter_frequency: Analysera bokstavsfrekvensen i filen " + current_file + "."  )
        print("all: Analysera " + current_file + "."  )
        print()
        base_menu()
        return "Välj ett sätt att analysera filen: "

def base_menu():
    print("quit: Avsluta programmet")
    print("change: Byt text fil")
    print()
