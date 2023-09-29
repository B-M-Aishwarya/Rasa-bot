import csv

data = []

# Read the CSV file "datas.csv"
with open('data/datas.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 2:
            question = row[0]
            answer = row[1]
            data.append({"text": questiondata, "intent": answerdata})

# Write to nlu.md file
with open('data/nlu.md', 'w', encoding='utf-8') as nlu_file:
    for example in data:
        nlu_file.write(f"## intent:{example['intent']}\n")
        nlu_file.write(f"- {example['text']}\n")
