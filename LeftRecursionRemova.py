def remove_left_recursion(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        alpha = []  # left recursive parts
        beta = []   # non-left recursive parts

        for production in grammar[non_terminal]:
            if production.startswith(non_terminal):
                alpha.append(production[len(non_terminal):])
            else:
                beta.append(production)

        if alpha:
            new_non_terminal = non_terminal + "'"
            new_grammar[non_terminal] = []
            new_grammar[new_non_terminal] = []

            for b in beta:
                new_grammar[non_terminal].append(b + new_non_terminal)

            for a in alpha:
                new_grammar[new_non_terminal].append(a + new_non_terminal)

            new_grammar[new_non_terminal].append("ε")
        else:
            new_grammar[non_terminal] = grammar[non_terminal]

    return new_grammar
