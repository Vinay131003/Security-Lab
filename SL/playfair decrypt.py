# Table generation
def generateTable(key):
  key = key.replace(" ", "").upper() 
  key_matrix=[]
  for char in key:
    if char not in key_matrix:
      key_matrix.append(char)
    alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'
  for char in alphabet:
     if char not in key_matrix:
        key_matrix.append(char)
  # Seprate the matrix in 5 x 5
  # print('Mat',key_matrix)
  matrix_size=5
  seprate_matrix=[]
  current_row=[]
  for char in key_matrix:
    current_row.append(char)
    if len(current_row)==matrix_size:
      seprate_matrix.append(current_row)
      current_row=[]
  # print('sperate',seprate_matrix)
  return seprate_matrix

# Finding the char position 
def find_pos(ket_matrix,char):
  row=len(ket_matrix)
  col=len(ket_matrix[0])
  # print('row:col value ',row,col)

  for i in range(row):
    for j in range(col):
      if ket_matrix[i][j] == char:
        return i,j

# Encrypt function
def playFairDecrypt(cipherText,ket_matrix):
  cipherText=cipherText.replace(" ","").upper()
  
  decrypted_text=''
  for i in range(0,len(cipherText),2):
    char1,char2 = cipherText[i],cipherText[i+1]
    row1,col1=find_pos(ket_matrix,char1)
    row2,col2=find_pos(ket_matrix,char2)

    if row1 == row2:
       decrypted_text += ket_matrix[row1][(col1-1)%5]
       decrypted_text += ket_matrix[row2][(col2-1)%5]
    elif col1 == col2:
       decrypted_text += ket_matrix[(row1-1)%5][col1]
       decrypted_text += ket_matrix[(row2-1)%5][col2]
    else:
       decrypted_text += ket_matrix[row1][col2]
       decrypted_text += ket_matrix[row2][col1]
  return  decrypted_text

key = input("Enter the key: ")
cipher = input("Enter the message to decrypt: ")

# Generate key matrix
key_matrix = generateTable(key)

for row in key_matrix:
  print(''.join(row))
print()
decrypt=playFairDecrypt(cipher,key_matrix)
print('Decrypted Message: ',decrypt)