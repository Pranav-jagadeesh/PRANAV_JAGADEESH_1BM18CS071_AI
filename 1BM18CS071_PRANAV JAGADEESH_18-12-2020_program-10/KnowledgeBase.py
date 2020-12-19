import aima.logic
import aima.utils

def get_clauses():
    clauses = list()

    clause = input("New Clause: ")

    while clause != "":
        clauses.append(aima.utils.expr(clause))
        clause = input("New Clause: ")

    print()
    return clauses


def tell_kb(kb):
    tell = input("\nTell: ")

    while tell != "":
        kb.tell(aima.utils.expr(tell))
        tell = input("Tell: ")
    print()


def ask_kb(kb):
    ask = input("\nAsk: ")

    while ask != "":
        print(list(aima.logic.fol_fc_ask(kb, aima.utils.expr(ask))))
        ask = input("Ask: ")
    print()


def main():

    clauses = get_clauses()

    kb = aima.logic.FolKB(clauses)

    menu = "0. Exit.\n1. Tell Knowledge Base.\n2. Ask Knowledge Base.\n"

    entry = input(menu)
    while entry != '0':
        if entry == '1':
            tell_kb(kb)
        elif entry == '2':
            ask_kb(kb)
        else:
            print()
        entry = input(menu)

if __name__ == "__main__":
    
    main()
