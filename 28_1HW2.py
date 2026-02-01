# כתוב תוכנית שקולטת שני מספרים מהמשתמש:
#
# קלוט lower – מספר נמוך higher – מספר גבוה
#
# כללים:
#
# יש לקלוט את lower לאחר מכן, יש לקלוט את higher בלולאת while True
# אם higher קטן או שווה ל־lower – יש להמשיך לקלוט שוב 2 ערכים
# כאשר higher גדול מ־lower – יוצאים מהלולאה ב break
# לבסוף, הדפס את כל המספרים מ־lower עד higher (כולל) באמצעות for עם range

lower = int(input("Enter lower number: "))

while True:
    higher = int(input("Enter higher number: "))
    if higher > lower:
        break
    else:
       lower = int(input("Enter lower number again: "))
for i in range(lower, higher + 1):
    print(i)
