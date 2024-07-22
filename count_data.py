import csv
import os

import matplotlib.pyplot as plt
from matplotlib_venn import venn3
def count_reviews(caminho_type_clones):
    with open(caminho_type_clones, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabeçalho = next(leitor_csv)
        reviews = []
        for linha in leitor_csv:
            if linha[0] not in reviews:
                reviews.append(linha[0])
        return reviews


def count_revisions(caminho_type_clones):
    with open(caminho_type_clones, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabeçalho = next(leitor_csv)
        revisions = []
        for linha in leitor_csv:
            revision = linha[0] + "_" + linha[1]
            if revision not in revisions:
                revisions.append(revision)
        return revisions


def count_interseccion(caminho_type_clones):
    move = 0
    move_and_test = 0
    test = 0
    move_and_diff = 0
    diff = 0
    move_and_diff_and_test = 0
    test_and_diff = 0
    nenhum_dos_3 = 0

    with open(caminho_type_clones, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabeçalho = next(leitor_csv)

        antecessor = None
        index_move = 0
        index_test = 0
        index_diff = 0

        for linha in leitor_csv:
            atual = linha[0] + "_" + linha[1] + "_" + linha[2]
            if antecessor is None:
                antecessor = atual

            if atual != antecessor:
                if index_move == 0 and index_test == 0 and index_diff == 0:
                    nenhum_dos_3 += 1
                elif index_move == 0 and index_test == 0 and index_diff == 1:
                    diff += 1
                elif index_move == 0 and index_test == 1 and index_diff == 0:
                    test += 1
                elif index_move == 0 and index_test == 1 and index_diff == 1:
                    test_and_diff += 1
                elif index_move == 1 and index_test == 0 and index_diff == 0:
                    move += 1
                elif index_move == 1 and index_test == 0 and index_diff == 1:
                    move_and_diff += 1
                elif index_move == 1 and index_test == 1 and index_diff == 0:
                    move_and_test += 1
                elif index_move == 1 and index_test == 1 and index_diff == 1:
                    move_and_diff_and_test += 1

                #print(antecessor + ": " + str(index_move) + "," + str(index_test) + "," + str(index_diff))

                # Reset the indices for the next group
                index_move = 0
                index_test = 0
                index_diff = 0
                antecessor = atual

            # Update the indices based on the current line
            if int(linha[3]) == 1:
                index_move = 1
            if int(linha[4]) == 1:
                index_test = 1
            if int(linha[5]) == 1:
                index_diff = 1

        # Handle the last group after the loop
        if antecessor is not None:
            if index_move == 0 and index_test == 0 and index_diff == 0:
                nenhum_dos_3 += 1
            elif index_move == 0 and index_test == 0 and index_diff == 1:
                diff += 1
            elif index_move == 0 and index_test == 1 and index_diff == 0:
                test += 1
            elif index_move == 0 and index_test == 1 and index_diff == 1:
                test_and_diff += 1
            elif index_move == 1 and index_test == 0 and index_diff == 0:
                move += 1
            elif index_move == 1 and index_test == 0 and index_diff == 1:
                move_and_diff += 1
            elif index_move == 1 and index_test == 1 and index_diff == 0:
                move_and_test += 1
            elif index_move == 1 and index_test == 1 and index_diff == 1:
                move_and_diff_and_test += 1

            #print(antecessor + ": " + str(index_move) + "," + str(index_test) + "," + str(index_diff))

    return move, move_and_test, move_and_diff_and_test, move_and_diff, test_and_diff, nenhum_dos_3, test, diff
def analise_revisions(caminho_type_clones):
    with open(caminho_type_clones, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabeçalho = next(leitor_csv)

        antecessor = None
        index_move = 0
        index_test = 0
        index_diff = 0
        revisions = {}
        for linha in leitor_csv:
            atual = linha[0] + "_" + linha[1]
            if antecessor is None:
                antecessor = atual

            if atual != antecessor:
                revisions[antecessor] = (index_move, index_test, index_diff, antecessor.split("_")[1])
                # Reset the indices for the next group
                index_move = 0
                index_test = 0
                index_diff = 0
                antecessor = atual

            # Update the indices based on the current line
            if int(linha[3]) == 1:
                index_move = 1
            if int(linha[4]) == 1:
                index_test = 1
            if int(linha[5]) == 1:
                index_diff = 1

        # Handle the last group after the loop
        if antecessor is not None:
            revisions[antecessor] = (index_move, index_test, index_test, antecessor.split("_")[1])
            #print(antecessor + ": " + str(index_move) + "," + str(index_test) + "," + str(index_diff))
    return revisions
def write_in_csv(review, type_move, type_test, type_diff , type_plus_revision, type_plus_revision_test, type_plus_revision_diff, no_clone):
    with open("review analysis/" + PROJECT + "(teste).csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([review, type_move,type_test, type_diff, type_plus_revision , type_plus_revision_test, type_plus_revision_diff, no_clone])
def make_csv(reviews,caminho_do_arquivo):
    for chave in reviews:
        save_move = 0
        save_test = 0
        save_diff = 0
        type_plus_revision_move = "None"
        type_plus_revision_test = "None"
        type_plus_revision_diff = "None"
        no_clone = "None"
        type_move = "None"
        type_test = "None"
        type_diff = "None"
        review = chave
        tuplas = reviews[chave]
        last_revision_with_clone = int(tuplas[len(tuplas) - 1][3])
        for tupla in reviews[chave]:
            revision = 0
            print(f'Review: {chave} revision: {revision} tupla {tupla}')
            if tupla[0] == 1 and save_move==0:
                save_move = 1
                revision=int(tupla[3])
                type_move = "moved in revision: " + str(revision)
            if tupla[0] == 0 and save_move==1:
                revision = int(tupla[3])
                type_plus_revision_move = "moved disappeared: " + str(revision)
            if tupla[1] == 1 and save_test == 0:
                save_test = 1
                revision = int(tupla[3])
                type_test = "test in revision: " + str(revision)
            if tupla[1] == 0 and save_test==1:
                revision = int(tupla[3])
                type_plus_revision_move = "test disappeared: " + str(revision)
            if tupla[2] == 1 and save_diff == 0:
                revision = int(tupla[3])
                save_diff = 1
                type_diff = "arquive diff in: " + str(revision)
            if tupla[2] == 0 and save_diff == 1:
                revision = int(tupla[3])
                type_plus_revision_diff = "diff disappeared: " + str(revision)
            if last_revision_with_clone == int(tupla[3]):
                with open(caminho_do_arquivo, newline='') as arquivo_csv:
                    leitor_csv = csv.reader(arquivo_csv)
                    cabeçalho = next(leitor_csv)
                    revision_check = int(tupla[3]) + 1
                    for linha in leitor_csv:
                        if review == linha[1] and str(revision_check) == linha[2]:
                            no_clone = "clone disappeared " + str(revision_check)
        write_in_csv(review, type_move, type_test, type_diff, type_plus_revision_move, type_plus_revision_test, type_plus_revision_diff, no_clone)
def dict_reviews(revisions):
    antecessor = None
    reviews = {}
    L=[]
    for linha in revisions:
        atual = linha.split("_")[0]
        revision = linha.split("_")[1]
        if antecessor is None:
            antecessor = atual

        if atual != antecessor:
            reviews[antecessor] = L
            antecessor = atual
            L = []
        L.append(revisions[antecessor+"_"+revision])


    # Handle the last group after the loop
    if antecessor is not None:
        reviews[antecessor] = L
        L = []
    return reviews

def plot_venn(results):
    move, move_and_test, move_and_diff_and_test, move_and_diff, test_and_diff, nenhum_dos_3, test, diff = results

    # Define the subset sizes for the Venn diagram
    subsets = (
        move,  # Only move
        test,  # Only test
        move_and_test,  # Move and test
        diff,  # Only diff
        move_and_diff,  # Move and diff
        test_and_diff,  # Test and diff
        move_and_diff_and_test  # Move, test, and diff
    )

    # Plot the Venn diagram
    venn = venn3(subsets=subsets, set_labels=('Moved', 'Test', 'Diff'))
    plt.title("Venn Diagram Types of Clones")  # Use plt.title instead of matplotlib.title
    plt.text(0.75, 0.1, f'None of the three: {nenhum_dos_3}', transform=plt.gca().transAxes, fontsize=12)
    plt.show()
PROJECT = "platform.ui"
caminho_do_arquivo = 'metadata/'+ PROJECT +'.csv'
caminho_type_clones = "type_clones/" + PROJECT + ".csv"
if not os.path.exists("review analysis"):
    os.mkdir("review analysis")

if not os.path.isfile("review analysis/" + PROJECT + ".csv"):
    with open("review analysis/" + PROJECT + "(teste).csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        #apareceu no comeco, meio ou fim, ou apareceu e sumiu, tipo pode ser qualquer um dos 3, inclusive com intersecao, ou nenhum dos 3
        writer.writerow(
            ["review_number", "type_move", "type_test", "type_diff", "fades_away_type_move", "fades_away_type_test", "fades_away_type_diff", "no_clone"])
"""
print(len(count_reviews(caminho_type_clones)))
print(len(count_revisions(caminho_type_clones)))
soma = 0
resultados = count_interseccion(caminho_type_clones)
for value in count_interseccion(caminho_type_clones):
    soma+=value
print(resultados)
print(soma)
plot_venn(resultados)
"""
make_csv(dict_reviews(analise_revisions(caminho_type_clones)), caminho_do_arquivo)