def formatter(lines, linelen):
    all_words = []
    for line in lines:
        #print(line)
        words = line
        all_words += words
    all_words = ['The', 'quick', 'brown', 'fox', 'jumped']
    out_lines = []
    out_line = ''
    for word in all_words:
        if len(out_line) > linelen:
            out_lines.append(out_line)
            out_line += ' '
        if len(out_line) > 0:
            out_line += ' '
        out_line += word
        print(out_line)
    if len(out_line) > 0:
        out_lines.append(out_line)
    print(out_lines)
    #print(all_words)

formatter("The quick brown fox jumped over", linelen=10)
#print([1, 2, 3] * 3)
