import pandas as pd

df_upper = pd.read_excel('data/alphabet.xlsx', sheet_name='large', header=None)
df_lower = pd.read_excel('data/alphabet.xlsx', sheet_name='small', header=None)

def convert_alphabet(txt):

    num = 15
    convert = [''] * num
    for i in txt:
        if i.isalpha():
            if i.isupper():
                row = ord(i) - ord('A')
                for j in range(num):
                    # pass
                    convert[j]+=df_upper[j].values[row]
                    if j == num - 1:
                        convert[j] += ' '

            if i.islower():
                row = ord(i) - ord('a')
                for j in range(num):
                    convert[j]+=df_lower[j].values[row]
                    if j == num-1:
                        convert[j]+=' '
                    # convert[i].append(df_upper.iloc[j, ''])
        else:
            for j in range(num):
                convert[j] += i
    re_str = '\n'.join(i for i in convert)
    return re_str