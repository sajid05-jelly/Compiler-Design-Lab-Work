def left_factoring(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        productions = grammar[non_terminal]
        prefix_dict = {}

        for prod in productions:
            prefix = prod[0]
            if prefix not in prefix_dict:
                prefix_dict[prefix] = []
            prefix_dict[prefix].append(prod)

        if any(len(v) > 1 for v in prefix_dict.values()):
            new_grammar[non_terminal] = []
            for prefix in prefix_dict:
                if len(prefix_dict[prefix]) > 1:
                    new_nt = non_terminal + "'"
                    new_grammar[non_terminal].append(prefix + new_nt)
                    new_grammar[new_nt] = []

                    for p in prefix_dict[prefix]:
                        new_grammar[new_nt].append(p[1:] if len(p) > 1 else "ε")
                else:
                    new_grammar[non_terminal].append(prefix_dict[prefix][0])
        else:
            new_grammar[non_terminal] = productions

    return new_grammar
