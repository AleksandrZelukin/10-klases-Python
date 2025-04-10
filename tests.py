# -*- coding: utf-8 -*-
# Python tests: vārdnīca, darbs ar failiem, CSV
# Izstrādāts interaktīvai komandrindas lietošanai

questions = {
    "Vārdnīca (dict)": [
        {
            "q": "Kā izveidot tukšu vārdnīcu Python valodā?",
            "options": ["[]", "()", "{}", "<>"],
            "answer": 2
        },
        {
            "q": 'Kā iegūt piekļuvi vārdnīcas atslēgas vērtībai? (d = {"vards": "Anna"})',
            "options": ['d["vards"]', "d.vards", 'd->"vards"', 'd.get("Anna")'],
            "answer": 0
        },
        {
            "q": "Kā pievienot jaunu pāri vārdnīcai? (d['vecums'] = 25)",
            "options": ["{'vecums': 25}", "[25]", "('vecums', 25)", "None"],
            "answer": 0
        },
        {
            "q": "Kas notiek, ja mēģināsi piekļūt atslēgai, kas neeksistē?",
            "options": ["Atgriezīs None", "Atgriezīs False", "KeyError kļūda", "Vienkārši izlaidīs"],
            "answer": 2
        },
        {
            "q": "Kura metode droši iegūst vērtību bez kļūdas?",
            "options": ["find()", "get()", "match()", "search()"],
            "answer": 1
        },
        {
            "q": "Kā dzēst pāri no vārdnīcas?",
            "options": ['d.delete("atslega")', 'del d["atslega"]', 'remove(d, "atslega")', 'd.popitem("atslega")'],
            "answer": 1
        },
        {
            "q": "Kā iegūt visas atslēgas no vārdnīcas?",
            "options": ["d.values()", "d.keys()", "d.items()", "list(d.values())"],
            "answer": 1
        },
        {
            "q": "Kāda ir update() metode?",
            "options": ["Aizvieto vienu atslēgu", "Apvieno divas vārdnīcas", "Notīra vārdnīcu", "Atgriež vērtību"],
            "answer": 1
        },
        {
            "q": "Kā noskaidrot vārdnīcas garumu?",
            "options": ["length(d)", "count(d)", "len(d)", "d.size()"],
            "answer": 2
        },
        {
            "q": 'Kas notiek, ja vārdnīcā ieliek {"a": 1, "a": 2}?',
            "options": ["Kļūda", "Abas vērtības saglabāsies", "Pēdējā pārrakstīs pirmo", "Vērtības summēsies"],
            "answer": 2
        }
    ],
    "Darbs ar failiem": [
        {
            "q": 'Kā atvērt failu lasīšanai?',
            "options": ['open("fails.txt", "r")', 'open("fails.txt", "w")', 'open("fails.txt", "x")', 'open("fails.txt", "rw")'],
            "answer": 0
        },
        {
            "q": 'Kā aizvērt failu pēc darba ar to?',
            "options": ["end()", "close()", "stop()", "exit()"],
            "answer": 1
        },
        {
            "q": 'Kas notiek, ja atver failu ar "w"?',
            "options": ["Raksta pievienojot", "Saturs izdzēsts", "Kļūda", "Nekas"],
            "answer": 1
        },
        {
            "q": 'Kā nolasīt visu faila saturu?',
            "options": ["readall()", "f.get()", "f.read()", "f.open()"],
            "answer": 2
        },
        {
            "q": 'Kā pievienot tekstu faila beigās?',
            "options": ['"w+"', '"r"', '"x"', '"a"'],
            "answer": 3
        },
        {
            "q": 'Kas ir with open(...) as f: priekšrocība?',
            "options": ["Automātiski aizver failu", "Raksta ātrāk", "Atver tikai teksta failus", "Palielina izmēru"],
            "answer": 0
        },
        {
            "q": 'Kā nolasīt rindas kā sarakstu?',
            "options": ["f.getlines()", "f.readlines()", "f.all()", "f.readlist()"],
            "answer": 1
        },
        {
            "q": 'Ko dara f.write("teksts")?',
            "options": ["Neko", "Ieraksta rindas nr", "Ieraksta tekstu", "Pievieno paplašinājumu"],
            "answer": 2
        },
        {
            "q": 'Kā pārliecināties, ka fails eksistē?',
            "options": ["os.check()", "os.path.exists()", "sys.exist()", "file.exists()"],
            "answer": 1
        },
        {
            "q": 'Kā pārveidot visu failu uz lielajiem burtiem?',
            "options": ["f.uppercase()", "f.read().upper() + write()", "f.upper().read()", "upper(f)"],
            "answer": 1
        }
    ],
    "CSV datnes": [
        {
            "q": "Kura bibliotēka jāimportē darbam ar CSV?",
            "options": ["text", "csv", "fileio", "data"],
            "answer": 1
        },
        {
            "q": "Kas ir csv.reader()?",
            "options": ["Ieraksta CSV", "Nolasīt rindu pa rindai", "Formatē CSV", "Veido sarakstu"],
            "answer": 1
        },
        {
            "q": "Kā pārlapot CSV rindas?",
            "options": ["for row in reader:", "for line in csv:", "reader.foreach()", "csv.readlines()"],
            "answer": 0
        },
        {
            "q": "Kā nolasīt CSV kā vārdnīcas?",
            "options": ["csv.reader()", "csv.DictReader()", "csv.get_dict()", "csv.map()"],
            "answer": 1
        },
        {
            "q": "Kā pierakstīt CSV failā?",
            "options": ["csv.write()", "csv.writer()", "csv.output()", "csv.add()"],
            "answer": 1
        },
        {
            "q": "Ko dara writer.writerow()?",
            "options": ["Raksta vairākas rindas", "Raksta rindu kā tekstu", "Raksta vienu rindu saraksta formā", "Raksta ar atslēgām"],
            "answer": 2
        },
        {
            "q": "Atšķirība starp writerow() un writerows()?",
            "options": ["Nav", "Viens raksta vienu, otrs vairākas", "Viens - saraksts, otrs - vārdnīca", "writerows ir novecojis"],
            "answer": 1
        },
        {
            "q": "Kā norādīt atdalītāju CSV failam?",
            "options": ['delimiter=";"', 'split=";"', 'sep=";"', 'delim=";"'],
            "answer": 0
        },
        {
            "q": "Kā ierakstīt ar kolonu nosaukumiem?",
            "options": ["DictWriter()", "writeheader()", "Abi", "writekeys()"],
            "answer": 2
        },
        {
            "q": "Kāpēc newline='' jānorāda?",
            "options": ["Lai formatētu", "Lai nebūtu tukšas rindas", "Lai lasītu kā dict", "Nav vajadzīgs"],
            "answer": 1
        }
    ]
}

def run_quiz():
    total = 0
    correct = 0

    for category, qs in questions.items():
        print(f"\n=== {category} ===")
        for i, q in enumerate(qs, 1):
            print(f"\n{i}. {q['q']}")
            for idx, opt in enumerate(q["options"]):
                print(f"   {chr(97+idx)}) {opt}")
            ans = input("Tava atbilde (a/b/c/d): ").strip().lower()
            total += 1
            if ord(ans) - 97 == q["answer"]:
                print("✅ Pareizi!")
                correct += 1
            else:
                pareizais = chr(97 + q["answer"])
                print(f"❌ Nepareizi! Pareizā atbilde: {pareizais}) {q['options'][q['answer']]}")

    print(f"\n=== Tests pabeigts! ===\nTavs rezultāts: {correct}/{total} pareizi ({round(correct/total*100)}%)")

if __name__ == "__main__":
    run_quiz()
