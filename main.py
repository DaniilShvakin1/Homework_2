a = [{"question": "Куда идти", "answer": [{"текст": "направо", "Link": 1}, {"текст": "налево", "Link": 2}]},
     {"question": "Вы пошли направо", "answer": [{"текст": "направо", "Link": 1}, {"текст": "налево", "Link": 2}]},
     {"question": "Куда идти", "answer": [{"текст": "направо", "Link": 1}, {"текст": "налево", "Link": 2}]}]
current_step = a[0]
while True:
    print(current_step["question"])
    for answer in current_step["answer"]:
        print(answer["текст"])
        str(current_step["answer"].index(answer))
        out = int(input())
        answer = current_step["answer"][out]
        current_step = a[answer["Link"]]
