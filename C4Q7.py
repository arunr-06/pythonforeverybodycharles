def compute_grade(score):
    try:
        if float(score) < 1:
            if float(score) >= 0.9:
                print('A')
            elif float(score) >= 0.8:
                print('B')
            elif float(score) >= 0.7:
                print('C')
            elif float(score) >= 0.6:
                print('D')
            elif float(score) < 0.6:
                print('F')
        else:
            print('Bad score')
    except:
        print('Bad score')


compute_grade(input('Provide your input\n'))
