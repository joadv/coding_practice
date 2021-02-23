import sys
num_words = int(sys.stdin.readline())
for i in range(num_words):
    result = ""
    word = sys.stdin.readline().rstrip()
    word_list = word.split(" ")
    for j in word_list:
        result = result + j[::-1] + " "
    print(result.rstrip())