participants_list_1 = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
first_day = []
for participants in range(0, len(participants_list_1), 2):
    first_day.append(participants_list_1[participants])
print(f"Первый день: {first_day}")