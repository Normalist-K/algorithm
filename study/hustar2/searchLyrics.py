def solution(words, queries):
    answers = []

    words_dict = {}

    for word in words:
        word_len = len(word)
        if word_len not in words_dict.keys():
            words_dict[word_len] = [{word[0]: [word]}, {word[-1]: [word]}, 1]
        else:
            if word[0] not in words_dict[word_len][0].keys():
                words_dict[word_len][0][word[0]] = [word]
            else:
                words_dict[word_len][0][word[0]].append(word)
            if word[-1] not in words_dict[word_len][1].keys():
                words_dict[word_len][1][word[-1]] = [word]
            else:
                words_dict[word_len][1][word[-1]].append(word)
            words_dict[word_len][2] += 1

    for query in queries:
        query_len = len(query)
        wild = 0
        front = True
        for idx, char in enumerate(query):
            if idx == 0:
                if char == '?':
                    front = False
                    wild += 1
            else:
                if char == '?':
                    wild += 1
        if query_len == wild:
            if query_len in words_dict.keys():
                answers.append(words_dict[query_len][2])
            else:
                answers.append(0)
            continue
        else:
            find_str = query[:query_len-wild] if front else query[wild:]

        # print(query_len, find_str, query_len - wild, front)
        answer = 0
        if query_len in words_dict.keys():
            if front == True and find_str[0] in words_dict[query_len][0].keys():
                if len(find_str) == 1:
                    answer = len(words_dict[query_len][0][find_str[0]])
                else:
                    if find_str in words_dict[query_len][0].keys():
                        answer = words_dict[query_len][0][find_str]
                    else:
                        for word in words_dict[query_len][0][find_str[0]]:
                            comp_str = word[:query_len-wild]
                            if find_str == comp_str:
                                answer += 1
                        words_dict[query_len][0][find_str] = answer
            elif front == False and find_str[-1] in words_dict[query_len][1].keys():
                if len(find_str) == 1:
                    answer = len(words_dict[query_len][1][find_str[-1]])
                else:
                    if find_str in words_dict[query_len][1].keys():
                        answer = words_dict[query_len][1][find_str]
                    else:
                        for word in words_dict[query_len][1][find_str[-1]]:
                            comp_str = word[wild:]
                            if find_str == comp_str:
                                answer += 1
                        words_dict[query_len][1][find_str] = answer
        answers.append(answer)

    return answers


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "?????"]))
