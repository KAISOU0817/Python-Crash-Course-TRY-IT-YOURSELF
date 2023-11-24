def print_models(unprinted_designs,completed_modles):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("printing models: "+current_design)
        completed_modles.append(current_design)


def show_completed_models(completed_models):
    print('the following models have been printed:')
    for completed_models in completed_models:
        print(completed_models)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)