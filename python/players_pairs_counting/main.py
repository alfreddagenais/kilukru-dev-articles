from count_player_pairs import count_player_pairs, possible_player_pairs

def main():
    print("A,B,C,D ==> " + str(possible_player_pairs(['A', 'B', 'C', 'D'])))
    # Return: ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']

    print("count(4) ==> " + str(count_player_pairs(4)))
    # Return: 6

    print("A,B,C,D,E,F,G,H,I,J ==> " + str(possible_player_pairs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])))
    # Return: ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'EF', 'EG', 'EH', 'EI', 'EJ', 'FG', 'FH', 'FI', 'FJ', 'GH', 'GI', 'GJ', 'HI', 'HJ', 'IJ']
    print("count(10) ==> " + str(count_player_pairs(10)))
    # Return: 45

if __name__ == "__main__":
    main()