def str_replace(word, bad_str, good_str):
    # use the replace to fix the mistake
    # debug actions, replace for Meagan
    word = word.replace(bad_str, good_str)
    return word

bad_memo = 'I knew I was always going to be half-bear, half man.  Being mixed race is so meta, I bet Neil would never understand.  What would he know?'
good_memo = str_replace(bad_memo, '  ', ' ')
