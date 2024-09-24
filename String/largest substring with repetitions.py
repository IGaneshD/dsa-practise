input_string = "aaabbc abcd abbbbbbc adddddc"

max_count = 0
for i, word in enumerate(input_string.split()):
    current_count = 1
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            current_count+=1
        else:
            if current_count>max_count:
                max_count = current_count
                index = i
            current_count = 1

print("substring with max repetitions-->", input_string.split()[index],"and count is ", max_count)