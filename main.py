from auto_complete_data_class import * 
from handle_score import *
from build_tree import *
from load_from_file import load_tree
from datetime import datetime


def online():
    loaded_tree = load_tree()

    while True:
        text = input("The system is ready, please enter your text:\n")
        sentence = ''
        while(text != '#'):
            sentence += text
            top_5_sentences = get_top_5_sentences(sentence, loaded_tree)
            print_sentences(top_5_sentences)
            text = input(sentence)


def main():
   #biuld_tree('Archive')
   online()


if __name__ == '__main__':
    main()
